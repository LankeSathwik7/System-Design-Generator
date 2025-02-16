# utils/ai_processor.py
from typing import Any, Dict
import groq
import streamlit as st
import json
import re

class AIProcessor:
    def __init__(self):
        self.client = groq.Client(api_key=st.secrets["GROQ_API_KEY"])
    
    def analyze_process(self, requirements):
        prompt = self._generate_prompt(requirements)
        
        try:
            completion = self.client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="llama-3.3-70b-versatile",
                temperature=0.1,
                max_tokens=4000,
            )
            
            response_text = completion.choices[0].message.content
            return self._parse_response(response_text)
            
        except Exception as e:
            raise Exception(f"Analysis error: {str(e)}")
    
    def _generate_prompt(self, requirements: Dict[str, Any]) -> str:
        return f"""Analyze this system design requirement and provide a detailed technical implementation flow. Format the response as a structured JSON document.

    System Requirements:
    {requirements['description']}

    Create a comprehensive system design with these key focus areas:
    1. Scalability & Performance
    2. Reliability & Fault Tolerance
    3. Security & Data Protection
    4. Monitoring & 
    
    Focus on these architectural patterns:
    - Microservices Communication
    - Event-Driven Architecture
    - CQRS Pattern (if applicable)
    - Circuit Breaker Pattern
    - Rate Limiting & Throttling
    - Data Partitioning Strategy
    - Caching Hierarchy
    - Security Measures

    Include specific details for:
    1. Data Validation & Sanitization
    2. Error Handling & Recovery
    3. Performance Optimization
    4. Security Implementation
    5. Monitoring & Alerting
    6. Deployment Strategy
    7. Scaling Approach
    8. Disaster Recovery Plan

    Diagram Requirements:
    1. Use Mermaid.js flowchart syntax
    2. Include these critical aspects:
    - User interactions
    - Authentication & Authorization
    - API Gateway & Load Balancing
    - Service Components
    - Database Operations
    - Caching Strategy
    - Error Handling
    - Monitoring & Logging

    For the diagram field, follow these strict Mermaid syntax rules:
        1. Always start with 'graph TD' (top-down) or 'graph LR' (left-right)
        2. Use simple node definitions: A[Label] for boxes, A((Label)) for circles, A[(Label)] for databases
        3. Use simple arrows: --> for connections, -->|text| for labeled connections
        4. Avoid special characters in labels
        5. Use straightforward flow patterns
        6. Keep node names simple (A, B, C, etc)
        7. Separate nodes and connections with line breaks (\\n)
        8. Follow this pattern for each connection: NodeA -->|Action| NodeB
        9. Use consistent spacing and formatting
        10. Test the syntax at https://mermaid.live before using

    Return the response in this exact JSON structure:

    {{
        "overview": "Comprehensive overview of the system architecture and design principles",
        "components": [
            {{
                "name": "Component name (Start with user interaction, follow the data flow through the system, and end with user feedback where applicable)",
                "purpose": "Detailed purpose and responsibility of this component",
                "steps": [
                    {{
                        "step": "1",
                        "action": "Specific action or operation",
                        "details": [
                            "Implementation detail with specific technology/algorithm (e.g., 'JWT for authentication using RS256 algorithm')",
                            "Configuration or setup detail with example (e.g., 'Redis cache with 1 hour TTL, LRU eviction')"
                        ]
                    }}
                ],
                "technologies": [
                    {{
                        "name": "Technology name (specific version if relevant)",
                        "purpose": "Specific use case and benefits",
                        "configuration": "Detailed configuration with examples"
                    }}
                ],
                "data_flow": {{
                    "input": "Incoming data format and validation requirements",
                    "process": "Data transformation and business logic",
                    "output": "Response format and error handling"
                }}
            }}
        ],
        "flow_steps": [
            {{
                "step": "1",
                "title": "Clear step title",
                "description": "Detailed process description",
                "technical_details": [
                    "Specific implementation detail with technology choice",
                    "Configuration or setup requirement with example"
                ]
            }}
        ],
        "diagram": "mermaid flowchart code"
    }}

    DIAGRAM SECTION:
The diagram must be comprehensive and include ALL of these components and their interactions:

1. Client-Side Flow:
   - User Interface (React/Frontend)
   - Form Validation
   - Client-Side Caching
   - Error Handling

2. Network Layer:
   - Load Balancer
   - API Gateway
   - CDN
   - SSL/TLS

3. Authentication & Authorization:
   - Auth Service
   - JWT/Token Management
   - OAuth Flow
   - Session Management

4. Application Services:
   - Business Logic Layer
   - Service Discovery
   - Message Queues
   - Event Bus

5. Data Layer:
   - Primary Database
   - Cache Layer
   - Read Replicas
   - Data Backup

6. Monitoring & Logging:
   - Logging Service
   - Metrics Collection
   - Alert Management
   - Tracing System

7. Security & Protection:
   - WAF
   - DDoS Protection
   - Rate Limiting
   - Data Encryption

8. Scaling & Recovery:
   - Auto Scaling
   - Failover Mechanisms
   - Disaster Recovery
   - Backup Systems

For the diagram field, use this exact structure:
1. Start with client components
2. Connect to network layer
3. Show all authentication flows
4. Connect to all application services
5. Show all data layer interactions
6. Include ALL monitoring and logging connections
7. Show ALL security measures
8. Include ALL scaling and recovery paths

The diagram must include these components with ALL possible interactions:
1. Multiple client applications (web, mobile, desktop)
2. Multiple CDN edges and caching layers
3. Complete security stack (WAF, DDoS, IDS/IPS, SIEM)
4. Load balancers and API gateways
5. Authentication services (OAuth, SAML, JWT)
6. Service mesh and service discovery
7. Multiple business logic services
8. Caching layers and Redis clusters
9. Message queues and dead letter queues
10. Worker services and background processors
11. Database primary and replicas
12. Search services and analytics
13. Storage solutions (S3, archives)
14. ML services and MLOps
15. Monitoring and logging stack
16. CI/CD and DevOps tools

Example partial diagram structure (extend this with ALL components above):
The diagram must follow this exact Mermaid syntax:
---
    config:
        look: handDrawn
        theme: neutral
        flowchart:
            htmlLabels: true
            curve: basis
            defaultRenderer: elk
---
graph TD
    %% Client Entry Points
    Client[Client] -->|Submit Request| CDN[CDN]
    Client -->|Direct API Call| WAF[WAF]
    Client -->|WebSocket| WS[WebSocket Service]
    
    %% CDN Paths
    CDN -->|Cache Hit| Client
    CDN -->|Cache Miss| WAF
    CDN -->|Invalid Request| EH1[Error Handler - Invalid Request]
    
    %% Security Layer
    WAF -->|Clean Traffic| LB[Load Balancer]
    WAF -->|Attack Detected| DDOS[DDoS Protection]
    WAF -->|Suspicious IP| IPS[Intrusion Prevention]
    
    %% DDoS Handling
    DDOS -->|Blocked| EH2[Error Handler - Security Block]
    DDOS -->|Rate Limited| RL[Rate Limiter]
    DDOS -->|Allowed| LB
    
    %% Load Balancer Paths
    LB -->|Health Check Failed| HC[Health Checker]
    LB -->|Server Available| AG[API Gateway]
    LB -->|Circuit Open| CB[Circuit Breaker]
    
    %% API Gateway Paths
    AG -->|Validate Token| Auth[Auth Service]
    AG -->|Rate Limited| EH3[Error Handler - Rate Limit]
    AG -->|Route Request| SM[Service Mesh]
    
    %% Authentication Flows
    Auth -->|Token Invalid| EH4[Error Handler - Auth]
    Auth -->|Token Expired| RT[Refresh Token]
    Auth -->|Token Valid| SM
    Auth -->|Needs 2FA| MFA[Multi-Factor Auth]
    
    %% MFA Paths
    MFA -->|2FA Success| SM
    MFA -->|2FA Failed| EH5[Error Handler - MFA]
    MFA -->|2FA Timeout| EH6[Error Handler - Timeout]
    
    %% Service Mesh Routes
    SM -->|Service Lookup| SD[Service Discovery]
    SM -->|Circuit Open| CB
    SM -->|Route Request| BL[Business Logic]
    
    %% Service Discovery
    SD -->|Service Not Found| EH7[Error Handler - Service]
    SD -->|Service Found| BL
    SD -->|Service Unhealthy| HC
    
    %% Business Logic Paths
    BL -->|Validate Input| VS[Validation Service]
    BL -->|Process Data| Worker[Worker Service]
    BL -->|Cache Check| Cache[Cache Layer]
    
    %% Validation Paths
    VS -->|Invalid Data| EH8[Error Handler - Validation]
    VS -->|Valid Data| Worker
    VS -->|Need Enrichment| EN[Data Enrichment]
    
    %% Cache Operations
    Cache -->|Cache Hit| Client
    Cache -->|Cache Miss| DB[Database]
    Cache -->|Cache Error| EH9[Error Handler - Cache]
    
    %% Database Operations
    DB -->|Read Success| Cache
    DB -->|Write Success| MQ[Message Queue]
    DB -->|Replication Lag| DR[Disaster Recovery]
    DB -->|Query Timeout| EH10[Error Handler - DB Timeout]
    
    %% Message Queue Flows
    MQ -->|Process Message| Worker
    MQ -->|Message Failed| DLQ[Dead Letter Queue]
    MQ -->|Queue Full| EH11[Error Handler - Queue]
    
    %% Worker Processing
    Worker -->|Process Success| ES[Event Store]
    Worker -->|Process Failed| DLQ
    Worker -->|Need ML| ML[ML Service]
    
    %% ML Service Paths
    ML -->|Prediction Success| BL
    ML -->|Model Error| EH12[Error Handler - ML]
    ML -->|Need Training| MLOps[ML Operations]
    
    %% Storage Operations
    ES -->|Store Success| S3[Object Storage]
    ES -->|Index Data| SE[Search Engine]
    ES -->|Archive Data| DW[Data Warehouse]
    
    %% Analytics Flow
    DW -->|Process Data| AP[Analytics Pipeline]
    AP -->|Generate Report| BI[BI Dashboard]
    AP -->|Data Alert| AM[Alert Manager]
    
    %% Monitoring Paths
    HC -->|Health Alert| AM
    CB -->|Circuit Alert| AM
    DR -->|Recovery Alert| AM
    
    %% Error Handling
    EH1 -->|Log Error| Logger[Logger Service]
    EH2 -->|Security Alert| SIEM[SIEM]
    EH3 -->|Rate Alert| AM
    
    %% Return Paths
    Logger -->|Index Log| ELK[ELK Stack]
    SIEM -->|Security Report| Admin[Admin Dashboard]
    AM -->|Alert Notification| Client
    BI -->|Dashboard View| Client
    Admin -->|Security Alert| Client

    %% Monitoring & Tracing
    DT[Distributed Tracing] -->|Trace| AG
    DT -->|Trace| BL
    DT -->|Trace| Worker
    DT -->|Visualize| Grafana[Grafana]

    %% Maintenance Flows
    Backup[Backup Service] -->|Backup| DB
    Backup -->|Archive| S3
    MLOps -->|Deploy Model| ML
    MLOps -->|Monitor| Grafana

IMPORTANT: The final diagram must include ALL components listed above with their interconnections. Don't truncate or simplify the diagram. Show every possible connection and interaction path."""


    def _parse_response(self, response_text):
        """
        More robust response parser that handles different diagram formats
        """
        try:
            # First, let's print the raw response for debugging
            st.write("Raw response received:")
            st.code(response_text[:200] + "...", language="text")

            # Remove markdown code blocks
            cleaned_text = re.sub(r'```(?:json|mermaid)?\s*|\s*```', '', response_text)
            
            # Replace backtick-wrapped diagram with proper JSON string
            cleaned_text = re.sub(r':\s*`\s*(graph TD[\s\S]*?)`\s*([,}])', r': "\1"\2', cleaned_text)
            
            # Find the JSON content between first { and last }
            start_idx = cleaned_text.find("{")
            end_idx = cleaned_text.rfind("}")
            
            if start_idx == -1 or end_idx == -1:
                raise ValueError("No valid JSON structure found")
            
            json_str = cleaned_text[start_idx:end_idx + 1]
            
            # Normalize whitespace
            json_str = re.sub(r'\s+', ' ', json_str)
            
            # Handle escaped quotes
            json_str = json_str.replace('\\"', '"')
            json_str = json_str.replace('""', '"')
            
            try:
                # Try to parse JSON
                data = json.loads(json_str)
            except json.JSONDecodeError as e:
                # If parsing fails, show context around error
                st.error(f"JSON Parse Error at position {e.pos}:")
                context_start = max(0, e.pos - 100)
                context_end = min(len(json_str), e.pos + 100)
                st.code(f"...{json_str[context_start:context_end]}...", language="json")
                
                # Additional cleanup for another attempt
                json_str = re.sub(r':\s*"([^"]*?graph TD[^"]*?)"', r': "\1"', json_str)
                json_str = json_str.replace('\n', ' ')
                data = json.loads(json_str)  # Try one more time
                
            # Clean up diagram if present
            if 'diagram' in data:
                diagram = data['diagram']
                
                # Remove any surrounding quotes or backticks
                diagram = diagram.strip('"`\'')
                
                # Ensure proper line breaks
                diagram = diagram.replace('\\n', '\n')
                
                # Ensure it starts with graph TD
                if not diagram.strip().startswith('graph'):
                    diagram = 'graph TD\n' + diagram
                
                # Add style definitions if not present
                style_defs = '''    %% Style definitions
        classDef default fill:#f9f9f9,stroke:#333,stroke-width:1px;
        classDef subgraphStyle fill:#e8e8e8,stroke:#666,stroke-width:2px;
    '''
                if '%% Style definitions' not in diagram:
                    diagram = diagram.replace('graph TD', f'graph TD\n{style_defs}')
                
                # Clean up formatting
                diagram = '\n'.join(line.strip() for line in diagram.split('\n'))
                
                # Store cleaned diagram
                data['diagram'] = diagram
                
                # Display the diagram code
                st.write("Diagram code:")
                st.code(diagram, language="mermaid")
            
            return data
            
        except json.JSONDecodeError as e:
            st.error(f"JSON Parse Error: {str(e)}")
            st.code(json_str, language="json")
            raise ValueError(f"Invalid JSON format: {str(e)}")
        except Exception as e:
            st.error(f"Error: {str(e)}")
            st.write("Response text that caused the error:")
            st.code(response_text[:500] + "...", language="text")
            raise ValueError(f"Error processing response: {str(e)}")

    def _validate_keywords(self, diagram):
        """
        Separate keyword validation logic
        """
        # Define key components that should be present
        required_components = {
            "Frontend": ["Client", "UI", "Frontend", "Web", "Mobile"],
            "Network": ["CDN", "Load Balancer", "API Gateway", "WAF"],
            "Security": ["Auth", "OAuth", "JWT", "WAF", "DDoS"],
            "Application": ["Service", "Microservice", "API", "Business Logic"],
            "Data": ["Database", "Cache", "Storage", "Redis"],
            "Messaging": ["Queue", "Message", "Event", "Stream"],
            "Processing": ["Worker", "Processor", "Handler", "Service"],
            "Monitoring": ["Monitor", "Log", "Trace", "Alert"],
            "DevOps": ["Deploy", "CI/CD", "Container", "Pipeline"]
        }
        
        missing = {}
        for category, keywords in required_components.items():
            missing_keywords = [k for k in keywords if k.lower() not in diagram.lower()]
            if missing_keywords:
                missing[category] = missing_keywords
        
        if missing:
            st.warning("Missing Components:")
            for category, keywords in missing.items():
                st.write(f"- {category}: {', '.join(keywords)}")
        
        return missing
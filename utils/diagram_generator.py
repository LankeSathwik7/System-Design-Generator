# utils/diagram_generator.py
class DiagramGenerator:
    def __init__(self):
        self.node_counter = 0
        self.component_keywords = {
            'frontend': [
                'frontend', 'ui', 'interface', 'client', 'browser', 'web', 
                'react', 'angular', 'vue', 'webpage', 'website', 'spa', 
                'form', 'input', 'display', 'view', 'page', 'component',
                'screen', 'template', 'render'
            ],
            'api': [
                'api', 'gateway', 'endpoint', 'rest', 'graphql', 'http', 
                'route', 'router', 'routing', 'proxy', 'request', 'response',
                'service', 'microservice', 'middleware', 'controller'
            ],
            'lambda': [
                'lambda', 'function', 'serverless', 'compute', 'processor',
                'handler', 'executor', 'worker', 'task', 'job', 'process',
                'service', 'backend', 'calculation', 'operation'
            ],
            'database': [
                'database', 'db', 'storage', 'store', 'dynamodb', 'mongodb',
                'postgresql', 'mysql', 'aurora', 'rds', 'persistence',
                'repository', 'table', 'collection', 'document', 'record'
            ],
            'cache': [
                'cache', 'redis', 'memcached', 'caching', 'temporary',
                'memory', 'inmemory', 'volatile', 'elasticache', 'session',
                'buffer', 'fast access', 'quick retrieval'
            ]
        }

    def generate_diagram(self, analysis_data):
        try:
            # Start with basic diagram configuration
            diagram_lines = [
                "%%{init: {",
                "  'theme': 'base',",
                "  'themeVariables': {",
                "    'fontFamily': 'monospace',",
                "    'fontSize': '14px'",
                "  }",
                "}}%%",
                "graph TD",
                ""
            ]
            
            nodes = []
            connections = []
            node_registry = {}
            
            # Process components
            components = analysis_data.get('components', [])
            for component in components:
                node_id = self._generate_node_id(component['name'])
                node_registry[component['name']] = node_id
                # Remove any special characters from the component name
                clean_name = component['name'].replace('[', '').replace(']', '')
                nodes.append(f"{node_id}[{clean_name}]")
            
            # Add nodes
            diagram_lines.extend([f"    {node}" for node in nodes])
            diagram_lines.append("")
            
            # Process connections
            for i, component in enumerate(components):
                curr_id = node_registry[component['name']]
                
                # Connect to next component
                if i < len(components) - 1:
                    next_id = node_registry[components[i + 1]['name']]
                    connections.append(f"{curr_id} --> {next_id}")
                
                # Special handling for Lambda
                if 'lambda' in component['name'].lower():
                    for other_name, other_id in node_registry.items():
                        if 'dynamodb' in other_name.lower():
                            connections.append(f"{curr_id} --> {other_id}")
                        elif 'redis' in other_name.lower():
                            connections.append(f"{curr_id} --> {other_id}")
                        elif 'cache' in other_name.lower():
                            connections.append(f"{curr_id} --> {other_id}")
            
            # Add connections
            diagram_lines.extend([f"    {conn}" for conn in connections])
            
            # Add styling
            diagram_lines.extend([
                "",
                "    classDef default fill:#E6E6FA,stroke:#6528F7,stroke-width:2px;",
                f"    class {' '.join(node_registry.values())} default;"
            ])
            
            return '\n'.join(diagram_lines)
            
        except Exception as e:
            return f"""graph TD
    Error["{str(e)}"]
    style Error fill:#ffcccc,stroke:#ff0000"""

    def _generate_node_id(self, name):
        """Generate a valid node ID"""
        self.node_counter += 1
        # Remove any special characters and make safe for mermaid
        safe_name = ''.join(c if c.isalnum() else '_' for c in name.lower())
        safe_name = safe_name.replace('[', '').replace(']', '')
        return f"n{self.node_counter}_{safe_name}"
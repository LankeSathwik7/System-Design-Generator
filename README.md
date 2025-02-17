# 🏗️ System Design Generator

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://system-design-generator.streamlit.app)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

An AI-powered system design generator that leverages Groq API and Mermaid.js to create comprehensive technical architecture diagrams and implementation plans. Input your system requirements and get detailed architectural diagrams, component breakdowns, and technical specifications.

## ✨ Features

- **AI-Powered Analysis**: Utilizes Groq's LLM for processing technical requirements and generating detailed system designs
- **Interactive Diagrams**: Creates dynamic Mermaid.js flowcharts showing component interactions and data flow
- **Comprehensive Planning**: Provides detailed implementation steps, technology recommendations, and best practices
- **Multi-Cloud Support**: Generates architectures compatible with AWS, Google Cloud, and Azure
- **Technical Depth**: Includes component-level details, data flow specifications, and scalability considerations
- **Error Handling**: Built-in validation and error handling for robust diagram generation
- **Customizable Output**: Adjust technical preferences for frontend, database, cloud provider, and caching strategies

## 🛠️ Technical Architecture

- **AI Engine**: Groq API with Llama 3.3 70B model
- **Visualization**: Mermaid.js for diagram rendering
- **Frontend**: Streamlit for interactive web interface
- **Language**: Python 3.11+
- **Deployment**: Streamlit Community Cloud

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/lankesathwik7/system-design-generator.git
   cd system-design-generator
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the project root
   - Add your Groq API key:
     ```env
     GROQ_API_KEY=your_api_key_here
     ```

## 🚀 Usage

1. Start the application:
   ```bash
   streamlit run streamlit_app.py
   ```

2. Input your system requirements. Example:
   ```
   Design a real-time chat application that supports:
   - 1 million concurrent users
   - Message persistence
   - Read receipts
   - Push notifications
   - File sharing up to 100MB
   ```

3. Configure technical preferences:
   - Select frontend framework
   - Choose database system
   - Pick cloud provider
   - Set caching strategy

4. Click "Generate Design" to create:
   - System architecture diagram
   - Component breakdowns
   - Implementation details
   - Technology recommendations

## ⚙️ Configuration Options

| Category | Available Options |
|----------|------------------|
| Frontend Framework | React, Angular, Vue.js, Next.js |
| Database Systems | DynamoDB, PostgreSQL, MongoDB, Redis |
| Cloud Providers | AWS, Google Cloud, Azure |
| Caching Strategies | Redis, Memcached, CDN |

## 🗂️ Project Structure

```
system-design-generator/
├── streamlit_app.py          # Main application
├── utils/
│   ├── ai_processor.py       # Groq API integration
│   └── diagram_generator.py  # Mermaid.js generation
├── .devcontainer/            # Development container settings
├── .github/                  # GitHub configurations
├── requirements.txt          # Python dependencies
└── LICENSE                   # Apache 2.0 license
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch:
   ```bash
   git checkout -b feature/new-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m 'Add new feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature/new-feature
   ```
5. Open a Pull Request

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- [Groq](https://groq.com/) for AI inference acceleration
- [Streamlit](https://streamlit.io/) for the web application framework
- [Mermaid.js](https://mermaid.js.org/) for diagram generation
- The open-source community for various tools and libraries

## 📝 Note

This tool is designed for generating system architecture diagrams and technical implementation plans. While it provides comprehensive suggestions, always review and adapt the output based on your specific requirements and constraints.
# QA API Automation Framework

## 📌 Overview
This project is a Python-based API automation framework built with Pytest to validate a multi-tenant REST API service.

The framework was designed to test: 
- Authentication
- Contract compliance with OpenAPI specifications
- Tenant isolation
- Functional API behavior
- Response schema validation
- Load/performance handling

The framework follows scalable automation design principles and supports self-contained execution using Docker.


# ⚙️ Tech Stack
- Python 3.10+
- Pytest
- Requests
- Docker & Docker Compose
- JSONSchema
- Locust
- Pytest HTML Reports


# 🚀 Setup Instructions
1. Clone the Repository
git clone https://github.com/miracleCA/python-Automation-test 
cd python-Automation-test

2. Create a Virtual Environment
macOS/Linux: 
- python3 -m venv venv   
- source venv/bin/activate

Windows: 
- python -m venv venv
- venv\Scripts\activate

3. Install Dependencies
- pip install -r requirements.txt

# 🐳 Docker Setup 
The API service is provided as a Docker image.

Start the service using:
- docker-compose up -d

Stop the service using:
- docker-compose down

The API runs on: <br>
http://localhost:8080

# Swagger documentation 
http://localhost:8080/swagger/index.html#/

# 🧪 Running the Test Suite
Recommended (Single Command)
- bash run_tests.sh

This command will:
- Start the Docker container
- Execute all tests
- Generate test reports
- Stop the Docker container automatically

# Run Tests Manually
Run all tests: 
- pytest -v

Run a specific test file: 
- pytest tests/test_contract.py -v

Run a specific test: 
- pytest tests/test_auth.py::test_invalid_auth -v

# 📊 Test Reports
Reports are generated automatically after execution. <br>

Location: 
- reports/

Generated reports:
- report.html
- junit.xml

Open HTML report in browser:
- open reports/report.html


# 🔥 Load Testing
Load testing is implemented using Locust. <br>

Run Locust: 
- locust -f load_tests/locustfile.py <br>

Open Locust UI:
- http://localhost:8089

The framework is designed to validate API behavior under high request volume.


# 🔐 Authentication Testing
The API uses Basic Authentication. <br>

Preconfigured test users: 
Username	Password
- test1	    test123 
- test2	    test456  <br>

Authentication scenarios tested:
- Valid credentials
- Invalid credentials
- Unauthorized access

# 🧩 Test Coverage
The framework currently validates: <br>

Functional Tests:
- Integration listing
- Integration creation
- Asset retrieval
- Asset validation

Contract Tests:
- Response schema validation
- JSON structure validation
- API contract enforcement

Security Tests:
- Basic authentication
- Unauthorized access checks

Tenant Isolation Tests:
- Multi-tenant segregation validation
- Cross-tenant access prevention

Performance Tests:
- Load testing with Locust


# ⚠️ Known Issue Detected
The framework identified a contract violation in the API: <br>

Issues: <br>
GET /integrations returns: 
- null 

instead of: 
- [] 

Impact:
- Violates OpenAPI contract expectations
- Breaks consumers expecting array responses
- Causes schema validation failure

The failing test correctly detects and reports this behavior.


# 🧠 Framework Design Principles
This framework was designed with:
- Separation of concerns 
- Reusable API clients 
- Centralized configuration 
- Scalable architecture 
- Extendable test structure 
- Self-contained execution 
- CI/CD readiness


# ✅ Key Features
- Pytest-based automation
- Dockerized execution
- Contract validation
- Schema validation
- HTML reporting
- JUnit XML reporting
- Load testing support
- Tenant isolation validation 
- Modular client architecture


# 📦 Dependency Installation
If dependencies are missing: 
- pip install -r requirements.txt

🚫 Git Ignore
The following are excluded from version control: 
- venv/
- reports/
- __pycache__/
- .pytest_cache/
- .DS_Store
- .idea/
- .vscode/


# 🏁 Single Command Execution

The full framework can be executed using: 
- bash run_tests.sh

This satisfies the self-contained execution requirement.

# 👨‍💻 Author
Miracle Chukwuebuka Anyiam <br>
Senior Software Engineer | QA Automation Engineer <br>
📞 +2348146713301 <br>
🌎 https://www.linkedin.com/in/chukwuebuka-miracle-anyiam-879a2b177
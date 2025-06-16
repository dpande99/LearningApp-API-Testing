# AI Onboarding Platform – API Testing Suite

This repository contains Python scripts to test the endpoints of the **AI Onboarding Platform** hosted on AWS API Gateway. The API provides capabilities such as document generation, RAG-based question answering, and more, tailored to user roles and experience levels.

## Repository Structure

api-testing/
├── test.py # Main script to run API tests
├── README.md # Project documentation

## Features Tested

- `GET /api/query` – General query endpoint
- `POST /generate-document` – Generate text document based on user input
- `POST /generate-document-secure` – (Alias of above, potentially future expansion)
- `POST /rag/query` – Ask question using Retrieval-Augmented Generation
- `POST /rag/refresh` – Refresh RAG document sources
- `POST /generate-document-html` – Generate HTML-based response
- `GET /api/query-secure` – Placeholder (Not implemented)


## Authentication

All endpoints require a Bearer Token (JWT) for authentication. Update the token in `test.py`:

```python
BEARER_TOKEN = "your_token_here"
AUTH_HEADER = {"Authorization": f"Bearer {BEARER_TOKEN}"}

User Role & Experience Requirements
Some endpoints validate user role and experience before processing the request.

### Allowed Roles ####
Data Engineer
Data Analyst
Business Analyst
UI/UX Designer
UI/UX Developer
Test Engineer
Other

#### Allowed Experience Levels ###
Beginner
Intermediate
Advanced
Expert

# Update these in test.py:

selected_user_role = "Data Analyst"
selected_experience = "Intermediate"

### If invalid values are used (e.g., "DevOps" or "5 years"), related tests will be skipped with a warning.


>>> how to run?
## Install dependencies:
pip install requests

From your terminal, run:
python test.py

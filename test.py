import requests
import json

#  Set your Bearer Token here
BEARER_TOKEN = "token_here"
AUTH_HEADER = {"Authorization": f"Bearer {BEARER_TOKEN}"}

# Allowed values
allowed_user_roles = {
    "Data Engineer", "Data Analyst", "Business Analyst",
    "UI/UX Designer", "UI/UX Developer", "Test Engineer", "Other"
}

allowed_experience_levels = {
    "Beginner", "Intermediate", "Advanced", "Expert"
}

# Input values
selected_user_role = "DevOps"
selected_experience = "5 years"

def is_valid_user(role, experience):
    if role not in allowed_user_roles:
        print(f" Invalid user_role: '{role}' not in allowed list.")
        return False
    if experience not in allowed_experience_levels:
        print(f" Invalid experience: '{experience}' not in allowed list.")
        return False
    return True

# Test 1: GET - api-query
def test_api_query():
    url = "https://12t9dib3g9.execute-api.us-east-1.amazonaws.com/jwt/ec2/api/query"
    params = {"q": "data engineer"}
    response = requests.get(url, params=params, headers=AUTH_HEADER)
    print("api-query:", response.status_code, response.text[:100])


# Test 2: POST - generate-document
def test_generate_document():
    if not is_valid_user(selected_user_role, selected_experience):
        return
    url = "https://12t9dib3g9.execute-api.us-east-1.amazonaws.com/jwt/ec2/generate-document"
    headers = {"Content-Type": "application/json", **AUTH_HEADER}
    payload = {
        "user_query": "AWS Cloud vs Azure vs gcp vs container vs Cloud",
        "user_persona": {"user_role": selected_user_role, "experience": selected_experience}
    }
    response = requests.post(url, headers=headers, json=payload)
    print("generate-document:", response.status_code, response.text[:100])


# Test 3: POST - generate-document-secure
def test_generate_document_secure():
    test_generate_document()  # Same as generate-document


# Test 4: POST - rag-query
def test_rag_query():
    url = "https://12t9dib3g9.execute-api.us-east-1.amazonaws.com/jwt/ec2/rag/query"
    headers = {"Content-Type": "application/json", **AUTH_HEADER}
    payload = {"question": "what is s3 bucket ?"}
    response = requests.post(url, headers=headers, json=payload)
    print("rag-query:", response.status_code, response.text[:100])


# Test 5: POST - rag-refresh
def test_rag_refresh():
    url = "https://12t9dib3g9.execute-api.us-east-1.amazonaws.com/jwt/ec2/rag/refresh"
    headers = {"Content-Type": "application/json", **AUTH_HEADER}
    response = requests.post(url, headers=headers)
    print("rag-refresh:", response.status_code, response.text[:100])


# Test 6: POST - generate-document-html
def test_generate_document_html():
    if not is_valid_user(selected_user_role, selected_experience):
        return
    url = "https://12t9dib3g9.execute-api.us-east-1.amazonaws.com/jwt/ec2/generate-document-html"
    headers = {"Content-Type": "application/json", **AUTH_HEADER}
    payload = {
        "user_query": "AWS Cloud vs Azure vs gcp vs container vs CloudComputing",
        "user_persona": {"user_role": selected_user_role, "experience": selected_experience}
    }
    response = requests.post(url, headers=headers, json=payload)
    print("generate-document-html:", response.status_code, response.text[:100])


# Test 7: GET - api-query-secure (incomplete in Postman, placeholder function)
def test_api_query_secure():
    print("api-query-secure: Not implemented in Postman JSON")


# Run all API tests
if __name__ == "__main__":
    print("Running API tests...\n")
    test_api_query()
    test_generate_document()
    test_generate_document_secure()
    test_rag_query()
    test_rag_refresh()
    test_generate_document_html()
    test_api_query_secure()

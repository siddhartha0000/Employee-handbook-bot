import requests

ENDEE_URL = "http://localhost:8080"

def create_index(index_name: str):
    payload = {
        "name": index_name,
        "dimension": 384,
        "space_type": "cosine",
        "precision": "fp32"
    }

    r = requests.post(
        f"{ENDEE_URL}/api/v1/index/create",
        json=payload
    )

    print("Status Code:", r.status_code)
    print("Response:", r.text)


if __name__ == "__main__":
    create_index("employee_policies")

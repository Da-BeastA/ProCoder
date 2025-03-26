import requests

def test_analyze_endpoint():
    sample_code = "def greet():\n    print('Hello, World!')\ngreet()"
    response = requests.post("http://127.0.0.1:8000/analyze/", json={"code": sample_code})
    assert response.status_code == 200
    data = response.json()
    assert "analysis" in data

if __name__ == "__main__":
    test_analyze_endpoint()
    print("Test passed!")

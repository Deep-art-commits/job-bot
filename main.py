import requests

def check_environment():
    print("✅ Python environment is working!")
    print(f"Requests library version: {requests.__version__}")

def test_connection():
    url = "https://httpbin.org/get"
    response = requests.get(url)
    
    if response.status_code == 200:
        print(f"✅ Connected successfully! Status code: {response.status_code}")
        data = response.json()
        print(f"Your IP (as seen by server): {data['origin']}")
    else:
        print(f"❌ Something went wrong. Status code: {response.status_code}")

if __name__ == "__main__":
    print("=== Job Bot - Environment Test ===\n")
    check_environment()
    print()
    test_connection()
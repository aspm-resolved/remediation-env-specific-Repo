# vulnerable_secrets.py
# This file intentionally contains hardcoded secrets for Gitleaks testing

AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

GITHUB_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz1234567890"
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"

DATABASE_PASSWORD = "P@ssw0rd123!"
JWT_SECRET = "my_super_secret_jwt_key"

def connect_to_service():
    print("Connecting with hardcoded credentials...")
    # Simulated usage of secrets
    return True
    
USER_PASSWORD = "P@ssw0rd1234!"

if __name__ == "__main__":
    connect_to_service()

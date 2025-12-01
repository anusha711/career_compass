import os
from google import genai
from kaggle_secrets import UserSecretsClient

def setup_api_key():
    """
    Try Kaggle Secrets first, otherwise rely on existing env var.
    Do NOT hardcode the key in code or commit it to GitHub.
    """
    # Kaggle-style secret
    try:
        kaggle_key = UserSecretsClient().get_secret("GOOGLE_API_KEY")
        os.environ["GOOGLE_API_KEY"] = kaggle_key
        print("✅ Authentication successful via Kaggle Secrets.")
    except Exception as e:
        # Kaggle may not exist outside Kaggle environment
        if os.getenv("GOOGLE_API_KEY"):
            print("✅ Authentication via existing GOOGLE_API_KEY env var.")
        else:
            print(f"⚠️ Auth Warning: Could not find 'GOOGLE_API_KEY'. {e}")

def get_client():
    """Initializes the GenAI client."""
    key = os.getenv("GOOGLE_API_KEY")
    if not key:
        print("❌ Error: No API Key found.")
        return None
    return genai.Client(api_key=key)

def load_resume_text(path):
    """Loads resume text from a file, or falls back to dummy text."""
    try:
        with open(path, "r") as f:
            resume_text = f.read()
        print(f"📄 Resume loaded from {path}")
        return resume_text
    except FileNotFoundError:
        print("⚠️ File not found. Using dummy resume data for demonstration.")
        return (
            "Experienced Python Developer with 5 years in AWS, Docker, "
            "and Kubernetes. Strong communicator."
        )

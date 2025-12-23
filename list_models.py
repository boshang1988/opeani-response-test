import os
import json
from dotenv import load_dotenv
from openai import OpenAI

# Load credentials from .env
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# List all models
models = client.models.list()

# Format as JSON
output = {
    "object": "list",
    "data": [
        {
            "id": model.id,
            "object": model.object,
            "created": model.created,
            "owned_by": model.owned_by
        }
        for model in models.data
    ]
}

print(json.dumps(output, indent=2))

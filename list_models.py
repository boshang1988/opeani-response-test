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

# Filter for latest GPT-5.x models (5.2, 5.3, etc.)
latest_gpt5 = []
for model in models.data:
    model_id = model.id
    # Match gpt-5.2, gpt-5.3, gpt-5.4, etc. (not gpt-5 or gpt-5.1)
    if model_id.startswith('gpt-5.') and not model_id.startswith('gpt-5.1'):
        latest_gpt5.append({
            "id": model.id,
            "object": model.object,
            "created": model.created,
            "owned_by": model.owned_by
        })

# Sort by created date (newest first)
latest_gpt5.sort(key=lambda x: x['created'], reverse=True)

output = {
    "object": "list",
    "data": latest_gpt5
}

print(json.dumps(output, indent=2))

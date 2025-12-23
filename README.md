# OpenAI Model List

List latest GPT-5.2+ models available on your OpenAI account.

## Setup

1. Install dependencies:
```bash
pip install openai python-dotenv
```

2. Create `.env` file:
```
OPENAI_API_KEY=sk-proj-xxx
```

## Usage

```bash
python3 list_models.py
```

## Output

```json
{
  "object": "list",
  "data": [
    {"id": "gpt-5.2-chat-latest", "object": "model", "created": 1765344352, "owned_by": "system"},
    {"id": "gpt-5.2-pro", "object": "model", "created": 1765343983, "owned_by": "system"},
    {"id": "gpt-5.2-pro-2025-12-11", "object": "model", "created": 1765343959, "owned_by": "system"},
    {"id": "gpt-5.2", "object": "model", "created": 1765313051, "owned_by": "system"},
    {"id": "gpt-5.2-2025-12-11", "object": "model", "created": 1765313028, "owned_by": "system"}
  ]
}
```
mkvenv() {
  python3 -m venv venv && source venv/bin/activate
}

alias v='mkvenv'

"""Choosing a Model 3 — Watch your tokens. Cost AND the context window are measured in TOKENS,
and every response reports its usage. This is how you keep an AI feature's bill predictable."""
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(base_url="https://api.groq.com/openai/v1", api_key=os.environ["GROQ_API_KEY"])

resp = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[{"role": "user", "content": "Explain load balancing in 3 sentences."}],
)

print(resp.choices[0].message.content)

# The API tells you exactly how many tokens you spent:
u = resp.usage
print(f"\n[tokens]  prompt={u.prompt_tokens}  completion={u.completion_tokens}  total={u.total_tokens}")
print("→ Cost and the context limit are counted in these tokens, not words.")
print("→ Big prompts (whole log files, long chats) = more tokens = more cost. Budget them.")

"""Choosing a Model 1 — Same code, any model. Only base_url + model change.
Swap provider or size freely; your app code stays identical. Watch the SPEED difference."""
import os, time
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# A "provider" is just a base_url + api_key. The OpenAI SDK talks to all of them:
GROQ = dict(base_url="https://api.groq.com/openai/v1", api_key=os.environ["GROQ_API_KEY"])
# OPENAI = dict(base_url="https://api.openai.com/v1",  api_key=os.environ.get("OPENAI_API_KEY"))
# OLLAMA = dict(base_url="http://localhost:11434/v1",  api_key="ollama")   # local · free · private

client = OpenAI(**GROQ)
prompt = "In one line: what does a 502 Bad Gateway mean?"

# Same call, two model sizes — note how much faster the small one is.
for model in ["openai/gpt-oss-20b", "openai/gpt-oss-120b"]:
    t0 = time.time()
    out = client.chat.completions.create(model=model, messages=[{"role": "user", "content": prompt}])
    print(f"\n=== {model}   ({time.time() - t0:.2f}s) ===")
    print(out.choices[0].message.content)

"""Choosing a Model 2 — Right model for the job. Fast+cheap for simple, big for complex.
Don't pay for (and wait on) a 120B model to do a job a 20B model does perfectly."""
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(base_url="https://api.groq.com/openai/v1", api_key=os.environ["GROQ_API_KEY"])

FAST  = "openai/gpt-oss-20b"      # cheap & fast   → high-volume simple tasks
SMART = "openai/gpt-oss-120b"     # slower & pricier → complex reasoning


def run(model, prompt):
    return client.chat.completions.create(
        model=model, messages=[{"role": "user", "content": prompt}]
    ).choices[0].message.content


# A simple, high-volume task → the FAST model is plenty.
print("=== FAST model · simple task (classify) ===")
print(run(FAST, "Classify severity as P1/P2/P3: 'nightly backup ran 15% slower'. Answer in one word."))

# A complex, multi-step task → reach for the SMART model.
print("\n=== SMART model · complex task (triage) ===")
print(run(SMART, "Checkout is slow, 504s are rising, a deploy went out 10 min ago, the DB is fine. "
                 "Reason step by step, then give the single most likely root cause."))

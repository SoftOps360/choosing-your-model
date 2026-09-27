# AI for DevOps — Ep 5: Choosing Your Model

Part of **SoftOps 360 · AI for DevOps (Hands-On)**.

"Which model should I use?" is a real engineering decision — it drives your **cost, speed, quality, and privacy**. This episode gives you the mental model and the numbers, so you pick deliberately instead of always reaching for the biggest one.

## The four dials
- **Closed vs open** — GPT/Claude (top quality, API-only) vs Llama/Qwen/Mistral (you can self-host).
- **Hosted vs local** — a cloud API (fast to start) vs your own box (private, no per-token bill).
- **Size** — small (8B: fast, cheap) vs large (70B+: smarter, slower, pricier).
- **Cost & context** — both counted in **tokens**, not words.

## What you run
| File | Shows |
|---|---|
| `01_same_code_any_model.py` | one prompt, two model sizes — **same code**, and the speed gap |
| `02_right_tool_for_the_job.py` | fast 8B for a simple classify · smart 70B for incident reasoning |
| `03_check_usage.py` | read `response.usage` — your real **token** (= cost) spend |

## Setup (free)
1. Free Groq key: https://console.groq.com/keys
2. `pip install -r requirements.txt`
3. Copy `.env.example` → `.env`, paste your key
4. `python 01_same_code_any_model.py`

## Decision cheat-sheet (for Ops)
| Situation | Pick |
|---|---|
| High-volume simple tasks (classify/route alerts) | **small & fast** (e.g. 8B) |
| Incident reasoning, root-cause, planning | **large** (70B+ / frontier) |
| Prod logs, secrets, private data | **local / self-hosted** (Ollama — next episode) |
| Prototyping, learning | **free API** (Groq) |
| Lowest latency in a chat UI | small model + **streaming** |

## The big lessons
- **Bigger isn't always better** — match the model to the task; you save real money and latency.
- **Everything is tokens** — cost and context are token-counted; big prompts cost more.
- **The code doesn't change** — swapping model/provider is `base_url` + `model`, so you're never locked in.

## Misconceptions cleared
- "Always use the best model." — Wasteful; an 8B model nails most simple ops tasks.
- "Local models are toys." — Modern open models are production-capable — and private (next episode).

## Next → Ep 6: Running Models Locally (Ollama)
Keep your infra data on your own machine — run a model locally with the same code.

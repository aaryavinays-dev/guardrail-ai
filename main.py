from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "GuardRail AI is running"}

@app.post("/analyze")
def analyze_prompt(data: dict):

    prompt = data.get("prompt", "")

    word_count = len(prompt.split())
    character_count = len(prompt)

    uppercase_prompt = prompt.upper()
    lowercase_prompt = prompt.lower()
    reversed_prompt = prompt[::-1]
    no_space_prompt = prompt.replace(" ", "")
    character_without_spaces = len(prompt.replace(" ", ""))

    estimated_tokens = int(word_count * 1.3)

    optimized_prompt = prompt.replace("Best regards", "")
    optimized_prompt = optimized_prompt.replace("Please kindly", "")
    optimized_prompt = optimized_prompt.replace("thank you", "")
    optimized_prompt = optimized_prompt.replace("Sincerely", "")
    optimized_prompt = optimized_prompt.strip()
    optimized_tokens = int(len(optimized_prompt.split()) * 1.3)

    tokens_saved = estimated_tokens - optimized_tokens

    return {
        "prompt": prompt,
        "word_count": word_count,
        "character_count": character_count,
        "uppercase_prompt": uppercase_prompt,
        "lowercase_prompt":prompt.lower,
        "no_space_prompt": no_space_prompt,
        "character_without_spaces": character_without_spaces,
        "reversed_prompt": reversed_prompt,
        "optimized_prompt": optimized_prompt,
        "optimized_tokens": optimized_tokens,
         "tokens_saved": tokens_saved,
         "estimated_tokens": estimated_tokens
    }
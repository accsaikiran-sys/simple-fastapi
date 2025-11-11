from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Word Reversal API. Use /reverse/{word} to reverse a word."}

@app.get("/reverse/{word}")
async def reverse_word(word: str):
    """
    Reverses the input word.
    """
    reversed_word = word[::-1]
    return {"original_word": word, "reversed_word": reversed_word}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
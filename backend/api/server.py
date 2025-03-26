from fastapi import FastAPI
from pydantic import BaseModel
from backend.models.ollama_client import get_ollama_response

app = FastAPI()

class CodeRequest(BaseModel):
    code: str

@app.post("/analyze/")
async def analyze_code(request: CodeRequest):
    """
    API endpoint to analyze code using Mistral 7B.
    """
    prompt = (
        "You are an AI code assistant. Review, explain, debug, and provide improvements for the following code:\n\n"
        f"{request.code}"
    )
    response = get_ollama_response(prompt)
    return {"analysis": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

import ollama

def get_ollama_response(prompt: str) -> str:
    """
    Calls the Ollama API to interact with Mistral 7B.
    """
    try:
        response = ollama.chat(model="mistral", messages=[{"role": "user", "content": prompt}])
        return response['message']['content']
    except Exception as e:
        return f"Error calling Ollama model: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(get_ollama_response("Explain the Python print function."))

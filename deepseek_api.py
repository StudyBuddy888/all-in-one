import requests
from config import OPENAI_API_KEY

def openai_query(text):
    """Send user query to OpenAI API"""
    url = "https://api.openai.com/v1/chat/completions"
    headers = {"Authorization": f"Bearer {OPENAI_API_KEY}", "Content-Type": "application/json"}
    
    data = {
        "model": "gpt-3.5-turbo",  # Change to "gpt-4" if needed
        "messages": [{"role": "user", "content": text}],
        "temperature": 0.7
    }
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        response_data = response.json()
        return response_data["choices"][0]["message"]["content"]  # ✅ Corrected parsing
    else:
        return f"Error: {response.status_code} - {response.text}"

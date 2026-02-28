"""Optional Gemini API integration."""

import os


class GeminiIntegration:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        self.client = None

    def query(self, prompt: str, context: list = None) -> str:
        """Send a prompt to Gemini with context and return the response."""
        if not self.api_key:
            return "Error: No Gemini API key configured"
            
        import urllib.request
        import json
        
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={self.api_key}"
        parts = []
        if context:
            for msg in context:
                parts.append({"text": msg})
        parts.append({"text": prompt})
        
        data = {
            "contents": [{"parts": parts}]
        }
        req = urllib.request.Request(
            url, 
            data=json.dumps(data).encode("utf-8"), 
            headers={'Content-Type': 'application/json'}
        )
        try:
            with urllib.request.urlopen(req) as response:
                result = json.loads(response.read().decode())
                return result['candidates'][0]['content']['parts'][0]['text']
        except Exception as e:
            return f"Error querying Gemini: {e}"

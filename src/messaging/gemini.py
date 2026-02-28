"""Optional Gemini API integration."""

import os


class GeminiIntegration:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        self.client = None

    def query(self, prompt: str) -> str:
        """Send a prompt to Gemini and return the response."""
        if not self.api_key:
            return "Error: No Gemini API key configured"
        # actual implementation would use google-generativeai
        return "Placeholder response"

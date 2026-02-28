"""Environment configuration loader."""

import os
from dotenv import load_dotenv


class Config:
    def __init__(self):
        load_dotenv()
        self.gemini_api_key = os.getenv("GEMINI_API_KEY")
        self.tcp_port = int(os.getenv("TCP_PORT", 7777))
        self.multicast_group = os.getenv("MCAST_GRP", "239.255.42.99")
        self.multicast_port = int(os.getenv("MCAST_PORT", 6000))

    def is_gemini_available(self):
        return bool(self.gemini_api_key)

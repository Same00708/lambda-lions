#!/usr/bin/env python3
"""Setup script for Archipel P2P Network."""

from setuptools import setup, find_packages

setup(
    name="archipel",
    version="0.1.0",
    description="P2P Encrypted Network Protocol (Zero-Internet, Decentralized)",
    author="Archipel Team",
    author_email="team@archipel.local",
    packages=find_packages(),
    install_requires=[
        "pynacl==1.5.0",
        "pycryptodome==3.20.0",
        "cryptography==43.0.0",
        "aiohttp==3.9.0",
        "click==8.1.7",
        "rich==13.7.0",
        "msgpack==1.0.8",
        "google-generativeai==0.3.2",
        "python-dotenv==1.0.0",
        "loguru==0.7.2",
        "psutil==5.9.8",
        "pytest==8.0.0",
        "pytest-asyncio==0.23.0",
        "pytest-cov==4.1.0",
    ],
    extras_require={
        "dev": [
            "pytest>=8.0.0",
            "pytest-asyncio>=0.23.0",
            "pytest-cov>=4.1.0",
        ]
    },
    python_requires=">=3.10",
    entry_points={
        "console_scripts": [
            "archipel=src.cli.commands:cli",
        ]
    },
)

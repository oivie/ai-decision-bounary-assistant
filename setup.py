#!/usr/bin/env python3
"""
Setup script for AI Decision Boundary Assistant
"""

from setuptools import setup, find_packages

# Read requirements from requirements.txt
with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith("#")]

# Read README for long description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="ai-decision-boundary-assistant",
    version="0.1.0",
    author="Elena Pashkova",
    description="Transform messy conversations into structured decision documentation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/elenapashkova/ai-decision-boundary-assistant",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
            "pre-commit>=2.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "ai-decision-assistant=ai_decision_assistant.ui.app:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)

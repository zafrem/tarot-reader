from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="tarot-reader",
    version="0.0.1",
    author="Tarot Reader",
    author_email="contact@example.com",
    description="A lightweight tarot reading package that doubles as a powerful random content generator with personal seed support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/tarot-reader",
    packages=find_packages(),
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
        "Programming Language :: Python :: 3.12",
        "Topic :: Games/Entertainment",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=[],
    keywords="tarot, cards, random, generator, llm, content, seed, entertainment",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/tarot-reader/issues",
        "Source": "https://github.com/yourusername/tarot-reader",
    },
)
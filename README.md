# Hugging_Face_LLM_2025
[![](https://img.shields.io/badge/Python-3.11.11-yellow.svg)](https://www.python.org/downloads/)
[![](https://img.shields.io/badge/docker-blue.svg)](https://www.docker.com/) 
[![](https://img.shields.io/badge/Hugging-Face-yellow.svg)](https://huggingface.co/arnir0/Tiny-LLM) 

> Experimenting with: **Tiny Large Language Models**.

## Setup and Use

```bash
docker compose up
```

1. http://localhost:8000/public/index.html
2. http://localhost:8000/api/llm?prompt=abcdefghijklmnopqrstuvwxyz

## Warning

1. This is a simple example (**NOT** Production-worthy) and basic safeguards (like input field validation, param sanitization, and the like) are mostly omitted here.
    * There's not a tremendous one can do within the context of *this* simple demo to break things/be malicious.
    * But the design pattern *should* be avoided in Production *as is* (without the addition of typical Production security mechanisms)!

## Resources and Links

1. https://huggingface.co/arnir0/Tiny-LLM
2. https://huggingface.co/learn/llm-course/
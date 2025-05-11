#!/usr/bin/env bash

echo "Generating text from prompt..." && python llm/_tiny_llm.py --prompt "$1" &
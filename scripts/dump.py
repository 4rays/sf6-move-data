#!/usr/bin/env python3

import toml
import os

moves_path = os.path.join(os.path.dirname(__file__), "../moves")

# Dump all move inputs, uniqued
inputs = []

for filename in os.listdir(moves_path):
    if filename.endswith(".toml"):
        with open(os.path.join(moves_path, filename)) as move_file:
            moves = toml.load(move_file)
            for move in moves["moves"]:
                input = move.get("input", None)
                if input not in inputs:
                        inputs.append(input)

print(inputs)

#!/usr/bin/env python3

import toml
import os


def validate(move, file_name):
    """Validate TOML data against schema"""
    match move:
        case {
            "name": str(),
            "name_ja": str(),
            "slug": str(),
            "characterId": int(),
            "type": str(),
        }:
            pass
        case _:
            print("❗ Validation error: {} on {}".format(move["name"], file_name))
            return False

    if move["type"] not in [
        "normal",
        "commandNormal",
        "targetCombo",
        "special",
        "super1",
        "super2",
        "super3",
        "throw",
    ]:
        print(
            "❗ Validation error: Move type for {} should be one of normal, commandNormal, targetCombo, special, super1, super2, super3, or throw.".format(
                move["name"]
            )
        )
        return False

    if abbreviation := move.get("abbreviation"):
        match abbreviation:
            case str():
                pass
            case _:
                print(
                    "❗ Validation error: abbreviation on {} should be a string.".format(
                        move["name"]
                    )
                )
                return False

    if japanese_abbreviation := move.get("abbreviation_ja"):
        match japanese_abbreviation:
            case str():
                pass
            case _:
                print(
                    "❗ Validation error: abbreviation_ja on {} should be a string.".format(
                        move["name"]
                    )
                )
                return False

    if block_type := move.get("blockType"):
        if block_type not in ["high", "low", "overhead", "jump-in"]:
            print(
                "❗ Validation error: blockType on {} should be one of the following values: high, low, overhead, jump-in.".format(
                    move["name"]
                )
            )
            return False

    if frame_count := move.get("frameCount"):
        match frame_count:
            case list():
                pass
            case _:
                print(
                    "❗ Validation error: frameCount on {} should be a list.".format(
                        move["name"]
                    )
                )
                return False
    else:
        print("🚧 Validation warning: frameCount missing on {}.".format(move["name"]))

    return True


# Load all character moves
moves_path = os.path.join(os.path.dirname(__file__), "moves")

for filename in os.listdir(moves_path):
    if filename.endswith(".toml"):
        with open(os.path.join(moves_path, filename)) as move_file:
            moves = toml.load(move_file)
            for move in moves["moves"]:
                print("Validating {}...".format(filename))
                if not validate(move, filename):
                    exit(1)
                else:
                    print("✅ {} validated!".format(filename))

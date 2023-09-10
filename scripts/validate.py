#!/usr/bin/env python3

import toml
import os


def validate(move, file_name):
    """Validate TOML data against schema"""
    match move:
        case {
            "name": str(),
            "name_ja": str(),
            "input": str(),
            "slug": str(),
            "type": str(),
        }:
            pass
        case _:
            print("❗ Validation error: Missing name, name_ja, input, slug, or type on {} for {}".format(move["name"], file_name))
            return False

    if characterId := move.get("characterId"):
        match characterId:
            case int():
                pass
            case _:
                print(
                    "❗ Validation error: characterId on {} should be an integer.".format(
                        move["name"]
                    )
                )
                return False

    if move["type"] not in [
        "normal",
        "commandNormal",
        "commandThrow",
        "action",
        "followUp",
        "targetCombo",
        "special",
        "super1",
        "super2",
        "super3",
        "throw",
    ]:
        print(
            "❗ Validation error: Move type for {} should be one of normal, commandNormal, commandThrow, action, followUp, targetCombo, special, super1, super2, super3, or throw.".format(
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
        if block_type not in ["high", "low", "mid", "midHigh"]:
            print(
                "❗ Validation error: blockType on {} should be one of the following values: high, low, midHigh, or mid.".format(
                    move["name"]
                )
            )
            return False

    if damage := move.get("damage"):
        match damage:
            case int():
                pass
            case _:
                print(
                    "❗ Validation error: damage on {} should be an integer.".format(
                        move["name"]
                    )
                )
                return False

    if startup := move.get("startup"):
        match startup:
            case int():
                pass
            case _:
                print(
                    "❗ Validation error: startup on {} should be an integer.".format(
                        move["name"]
                    )
                )
                return False

    if active := move.get("active"):
        match active:
            case list():
                for frame in active:
                    match frame:
                        case int():
                            pass
                        case _:
                            print(
                                "❗ Validation error: active on {} should be a list of integers.".format(
                                    move["name"]
                                )
                            )
                            return False
            case _:
                print(
                    "❗ Validation error: active on {} should be a list.".format(
                        move["name"]
                    )
                )
                return False
    
    if cancel := move.get("cancel"):
        match cancel:
            case str():
                if cancel not in ["C", "SA", "SA2", "SA3", "J", "*"]:
                    print(
                        "Property cancel on {} of `{}` should be C, SA, SA2, SA3, J, or *".format(
                            move["name"], cancel
                        )
                    )
                    pass
                else:
                    pass

    if properties := move.get("properties"):
        match properties:
            case list():
                for property in properties:
                    match property:
                        case str():
                            if property not in [
                                "canCrossUp",
                                "armorBreak",
                                "tumble",
                                "juggle",
                                "crumple",
                                "knockdown",
                                "forcesStanding",
                                "stockIncrement",
                                "stockDecrement",
                                "chargeable",
                                "chainable",
                            ]:
                                print(
                                    "❗ Validation error: property on {} should be one of the following values: canCrossUp, armorBreak, tumble, crumple, juggle, knockdown, forcesStanding, chargeable, stockIncrement, or stockDecrement but was {} instead.".format(
                                        move["name"], property
                                    )
                                )
                                return False
                            else:
                                pass
                        case _:
                            print(
                                "❗ Validation error: properties on {} should be a list of strings.".format(
                                    move["name"]
                                )
                            )
                            return False
            case _:
                print(
                    "❗ Validation error: properties on {} should be a list.".format(
                        move["name"]
                    )
                )
                return False
    return True


# Load all character moves
moves_path = os.path.join(os.path.dirname(__file__), "../moves")

for filename in os.listdir(moves_path):
    if filename.endswith(".toml"):
        with open(os.path.join(moves_path, filename)) as move_file:
            try:
                moves = toml.load(move_file)
                for move in moves["moves"]:
                    if not validate(move, filename):
                        exit(1)
                    else:
                        print("✅ {} - {} validated!".format(filename, move["name"]))
            except toml.decoder.TomlDecodeError as e:
                print("❗ Validation error for {}: {}".format(filename, e))
                exit(1)

# Validate that move slugs are unique
slugs = []

for filename in os.listdir(moves_path):
    if filename.endswith(".toml"):
        with open(os.path.join(moves_path, filename)) as move_file:
            moves = toml.load(move_file)
            for move in moves["moves"]:
                if move["slug"] in slugs:
                    print(
                        "❗ Validation error: Move slug {} is not unique.".format(
                            move["slug"]
                        )
                    )
                    exit(1)
                else:
                    slugs.append(move["slug"])

# Validate that move names are unique per character
names = []

for filename in os.listdir(moves_path):
    if filename.endswith(".toml"):
        with open(os.path.join(moves_path, filename)) as move_file:
            moves = toml.load(move_file)
            for move in moves["moves"]:
                move_name_with_id = "{}-{}".format(
                    move["name"], move.get("characterId")
                )

                if move_name_with_id in names:
                    print(
                        "❗ Validation error: Move name {} is not unique.".format(
                            move["name"]
                        )
                    )
                    exit(1)
                else:
                    names.append(move_name_with_id)

# Validate that move japanese name (name_ja) is unique per character
names_ja = []

for filename in os.listdir(moves_path):
    if filename.endswith(".toml"):
        with open(os.path.join(moves_path, filename)) as move_file:
            moves = toml.load(move_file)
            for move in moves["moves"]:
                move_name_with_id = "{}-{}".format(
                    move["name_ja"], move.get("characterId")
                )

                if move_name_with_id in names_ja:
                    print(
                        "❗ Validation error: Move name_ja {} is not unique.".format(
                            move["name_ja"]
                        )
                    )
                    exit(1)
                else:
                    names_ja.append(move_name_with_id)

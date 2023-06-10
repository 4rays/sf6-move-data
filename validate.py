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
        "action",
        "actionMove",
        "targetCombo",
        "special",
        "super1",
        "super2",
        "super3",
        "throw",
    ]:
        print(
            "❗ Validation error: Move type for {} should be one of normal, commandNormal, action, actionMove, targetCombo, special, super1, super2, super3, or throw.".format(
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
                for frame in frame_count:
                    match frame:
                        case str():
                            frameData = frame.split("-")
                            if len(frameData) == 2:
                                if frameData[0] not in ["S", "R", "A", "PA"]:
                                    print(
                                        "❗ Validation error: frameCount identifier on {} should be S, R, A, or PA but was {} instead".format(
                                            move["name"], frameData[0]
                                        )
                                    )
                                    return False
                                if not frameData[1].isdigit():
                                    print(
                                        "❗ Validation error: frameCount count on {} should be a number but was {} instead".format(
                                            move["name"], frameData[1]
                                        )
                                    )
                                    return False

                                pass
                            else:
                                print(
                                    "❗ Validation error: frameCount on {} should be of format Identifier-count but was {} instead.".format(
                                        move["name"], frame
                                    )
                                )
                                return False

                        case _:
                            print(
                                "❗ Validation error: frameCount on {} should be a list of strings.".format(
                                    move["name"]
                                )
                            )
                            return False
            case _:
                print(
                    "❗ Validation error: frameCount on {} should be a list.".format(
                        move["name"]
                    )
                )
                return False
    else:
        print("🚧 Validation warning: frameCount missing on {}.".format(move["name"]))

    if cancelsInto := move.get("cancelsInto"):
        match cancelsInto:
            case list():
                for cancel in cancelsInto:
                    match cancel:
                        case str():
                            if cancel not in [
                                "chain",
                                "special",
                                "super",
                                "jump",
                                "targetCombo",
                                "super1",
                                "super2",
                                "super3"
                            ]:
                                print(
                                    "❗ Validation error: cancelsInto on {} should be a one of the following values: chain, special, super, jump, targetCombo, super1, super2, or super3 but was {} instead".format(
                                        move["name"], cancel
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
                                "knockdown",
                                "forcesStanding",
                                "stockIncrement",
                                "stockDecrement",
                                "chargeable"
                            ]:
                                print(
                                    "❗ Validation error: property on {} should be one of the following values: canCrossUp, armorBreak, tumble, juggle, knockdown, forcesStanding, chargeable, stockIncrement, or stockDecrement but was {} instead.".format(
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

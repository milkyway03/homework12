import json


def get_candidates():
    with open("homework12/candidates.json", "r") as fp:
        candidates = json.load(fp)
    return candidates


def get_settings():
    with open("homework12/settings.json", "r") as fp:
        settings = json.load(fp)
    return settings



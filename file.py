import json


def get_candidates():
    with open("data/candidates.json", "r", encoding="utf-8") as fp:
        candidates = json.load(fp)
    return candidates


def get_candidate_by_id(can_id):
    candidates = get_candidates()
    for can in candidates:
        if can_id == can["id"]:
            return can


def get_settings():
    with open("data/settings.json", "r", encoding="utf-8") as fp:
        settings = json.load(fp)
    return settings


def get_candidate_by_name(name):
    candidates = get_candidates()
    settings = get_settings()

    candidates_found = []

    for can in candidates:

        if settings["case-sensitive"]:
            if name in can["name"]:
                candidates_found.append(can)
        else:
            if name.lower() in can["name"].lower():
                candidates_found.append(can)

    return candidates_found


def get_candidate_by_skill(skill_name):
    candidates = get_candidates()
    settings = get_settings()

    candidates_found = []

    for can in candidates:

        if settings["case-sensitive"]:
            if skill_name in can["skills"]:
                candidates_found.append(can)
        else:
            if skill_name.lower() in can["skills"].lower():
                candidates_found.append(can)

    return candidates_found

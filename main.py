from flask import Flask, request, render_template
import json


def get_candidates():
    with open("homework12/candidates.json", "r") as fp:
        candidates = json.load(fp)
    return candidates


def get_settings():
    with open("homework12/settings.json", "r") as fp:
        settings = json.load(fp)
    return settings


app = Flask(__name__)


@app.route('/')
def page_index():

    settings = get_settings()
    online = settings.get("online")
    if online:
        return "Приложение работает"
    return "Приложение не работает"


app.run()

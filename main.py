from flask import Flask, request, render_template
from file import get_settings, get_candidates, get_candidate_by_id, get_candidate_by_name, get_candidate_by_skill


app = Flask(__name__)


@app.route('/')
def page_index():

    settings = get_settings()
    online = settings.get("online")
    if online:
        return "Приложение работает"
    return "Приложение не работает"


@app.route("/list")
def page_list_of_candidates():

    cans = get_candidates()
    return render_template("list.html", cans=cans)


@app.route('/candidate/<int:can_id>')
def page_single_candidate(can_id):

    can = get_candidate_by_id(can_id)

    return render_template("candidates.html", can=can)


@app.route('/search')
def page_search_by_name():
    name = request.args['name']

    cans = get_candidate_by_name(name)
    cans_count = len(cans)

    return render_template("search.html", cans=cans, cans_count=cans_count)


@app.route('/skill/<skill_name>')
def page_search_by_skill(skill_name):
    cans = get_candidate_by_skill(skill_name)
    cans_count = len(cans)

    return render_template("skill.html", skill_name=skill_name, cans=cans, cans_count=cans_count)


app.run()

"""Flask application for Bavly Kamel's personal portfolio."""

from flask import Flask, abort, jsonify, render_template

from projects import PROJECTS, get_project

app = Flask(__name__)


@app.get("/")
def home():
    featured_projects = PROJECTS[:3]
    return render_template("index.html", projects=featured_projects)


@app.get("/projects")
def projects():
    return render_template("projects.html", projects=PROJECTS)


@app.get("/projects/<slug>")
def project_detail(slug):
    project = get_project(slug)
    if project is None:
        abort(404)
    return render_template("project.html", project=project)


@app.get("/api/projects")
def projects_api():
    """Expose project data for a future interactive data/ML experience."""
    return jsonify([
        {key: value for key, value in project.items() if key != "sections"}
        for project in PROJECTS
    ])


@app.errorhandler(404)
def not_found(_error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)

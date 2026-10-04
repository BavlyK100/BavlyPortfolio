"""Flask application for Bavly Kamel's personal portfolio."""

import os

from flask import Flask, abort, jsonify, redirect, render_template, send_from_directory, url_for

from projects import PROJECTS, get_project

# Vercel serves files in public/ directly from its CDN. Disable Flask's default
# /static route and use this fallback only for local development.
app = Flask(__name__, static_folder=None)

# Set TRUSTED_HOSTS to a comma-separated list of exact public hostnames in
# production. Leave unset for local development and preview environments.
trusted_hosts = os.environ.get("TRUSTED_HOSTS")
if trusted_hosts:
    app.config["TRUSTED_HOSTS"] = [
        host.strip() for host in trusted_hosts.split(",") if host.strip()
    ]


@app.after_request
def add_security_headers(response):
    """Set browser protections on dynamic pages and local static assets."""
    response.headers.setdefault(
        "Content-Security-Policy",
        "default-src 'self'; script-src 'self'; style-src 'self' https://fonts.googleapis.com; "
        "font-src 'self' https://fonts.gstatic.com; img-src 'self'; connect-src 'self'; "
        "base-uri 'self'; form-action 'self'; frame-ancestors 'none'; object-src 'none'",
    )
    response.headers.setdefault("X-Content-Type-Options", "nosniff")
    response.headers.setdefault("X-Frame-Options", "DENY")
    response.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
    response.headers.setdefault(
        "Permissions-Policy", "camera=(), microphone=(), geolocation=()"
    )
    return response


@app.get("/")
def home():
    return render_template("index.html", projects=PROJECTS)


@app.get("/projects")
def projects():
    return render_template("projects.html", projects=PROJECTS)


@app.get("/projects/<slug>")
def project_detail(slug):
    project = get_project(slug)
    if project is None and slug == "file-organizer":
        return redirect(url_for("project_detail", slug="10-day-goal-tracker"), code=301)
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


@app.get("/<path:asset_path>")
def public_asset(asset_path):
    """Serve public assets when running locally; Vercel serves them directly."""
    return send_from_directory(f"{app.root_path}/public", asset_path)


@app.errorhandler(404)
def not_found(_error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    # Keep Flask's interactive debugger disabled outside an explicit local setup.
    app.run()

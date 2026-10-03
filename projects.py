"""Single source of truth for Bavly Kamel's published project."""

PROJECTS = [
    {
        "slug": "file-organizer",
        "number": "01",
        "featured": True,
        "name": "File Organizer",
        "category": "Python · Automation",
        "status": "Existing project",
        "status_kind": "available",
        "summary": "A Python utility that sorts files into folders based on their extensions, making a cluttered directory easier to manage.",
        "technologies": ["Python", "OS", "Automation"],
        "features": ["Groups files by extension", "Automates repetitive file management"],
        "sections": [
            ("Problem", "Sorting files by hand is repetitive and makes busy folders difficult to navigate."),
            ("Approach", "Use Python's operating-system tools to inspect file extensions and move files into matching folders."),
            ("Implementation", "The project uses Python to organize files into folders based on their extensions."),
            ("What I learned", "[Add a short note about what you learned while building this project.]"),
        ],
        "github": "https://github.com/BavlyK100/tracker_app",
        "linkedin": "https://lnkd.in/p/eVyAKW4x",
        "demo": None,
    },
]


def get_project(slug):
    return next((project for project in PROJECTS if project["slug"] == slug), None)

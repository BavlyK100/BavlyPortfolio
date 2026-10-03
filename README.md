# BavlyPortfolio

A personal portfolio website for Bavly Kamel, a Data Science & AI student at Zewail City of Science and Technology. Built with Python, Flask, semantic HTML, CSS, and vanilla JavaScript.

## Features

- Responsive portfolio with Home, About, Skills, Projects, Education, Experience, and Contact sections
- Dark-first design with a persistent light/dark theme toggle
- Featured project layout controlled by project data
- Dedicated detail pages for each project
- Published File Organizer project plus four clearly labeled upcoming project plans
- Project descriptions and repository links without invented results
- Flask routes for the home page, project listing, project details, and a JSON projects API
- Accessible mobile navigation, keyboard focus states, reduced-motion support, and project status labels
- Basic SEO and Open Graph metadata

## Run locally

1. Clone this repository and enter the `BavlyPortfolio` directory.
2. Create and activate a virtual environment:

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Install the dependency:

   ```powershell
   pip install -r requirements.txt
   ```

4. Start Flask:

   ```powershell
   python app.py
   ```

5. Open <http://127.0.0.1:5000>.

Flask's development server is intended for local development. Vercel detects the Flask app in `app.py` and deploys it as a Python Function. Static assets live in `public/`, where Vercel serves them through its CDN; a Flask fallback route serves the same files during local development.

## Project structure

```text
BavlyPortfolio/
├── app.py
├── projects.py
├── requirements.txt
├── templates/
│   ├── 404.html
│   ├── base.html
│   ├── index.html
│   ├── project_card.html
│   ├── project.html
│   └── projects.html
└── public/
    ├── css/style.css
    ├── images/favicon.svg
    └── js/script.js
```

## Content to personalize

- Add future projects to `projects.py` only when they are ready to share.
- Add actual internship responsibilities and dates when available.
- The LinkedIn profile, Zewail City, Banque Misr certificate, File Organizer repository, and File Organizer LinkedIn post links use the supplied URLs.

No contact form is included because no email delivery service was provided. The email link opens the visitor's email application and the site does not store messages.

## Future improvements

- Add future projects and their verified repository/live demo links when ready.
- Add project notebooks, charts, and model evaluation once the work exists.
- Add an email delivery provider if a contact form is needed.
- Add a model-backed `/api/predict` endpoint when a trained and evaluated model is available.

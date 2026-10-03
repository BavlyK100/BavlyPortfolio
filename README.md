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

Flask's development server is intended for local development and starts with debug mode disabled. Vercel detects the Flask app in `app.py` and deploys it as a Python Function. Static assets live in `public/`, where Vercel serves them through its CDN; a Flask fallback route serves the same files during local development. `vercel.json` applies browser security headers to deployed pages and assets, while Flask applies the same headers to local responses.

## Project structure

```text
BavlyPortfolio/
├── app.py
├── projects.py
├── requirements.txt
├── vercel.json
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
    └── js/
        ├── script.js
        └── theme-init.js
```

## Content to personalize

- Add future projects to `projects.py` only when they are ready to share.
- Add actual internship responsibilities and dates when available.
- The LinkedIn profile, Zewail City, Banque Misr certificate, File Organizer repository, and File Organizer LinkedIn post links use the supplied URLs.

No contact form is included because no email delivery service was provided. The email address is displayed as plain text and does not open an email application.

## Security notes

- Flask debug mode is disabled when running `app.py`.
- Security headers include a restrictive Content Security Policy, MIME sniffing protection, clickjacking protection, a limited referrer policy, and disabled unused browser permissions.
- The Content Security Policy permits only this site plus Google Fonts for CSS and font files. Keep third-party scripts, inline scripts, and inline styles out unless the policy is reviewed and updated deliberately.
- Set the `TRUSTED_HOSTS` environment variable to a comma-separated list of exact public hostnames for production (for example, `example.com,www.example.com`). Flask rejects requests sent to other hostnames when this is set. Leave it unset for local development or previews whose hostnames change.
- GitHub profile and File Organizer links use fixed internal redirect paths. Only destinations in the allowlist are accepted; unknown destinations return 404.
- The site has no login, database, message form, or server-side user data storage, so there are no credentials or user records to protect in this app.

## Future improvements

- Add future projects and their verified repository/live demo links when ready.
- Add project notebooks, charts, and model evaluation once the work exists.
- Add an email delivery provider if a contact form is needed.
- Add a model-backed `/api/predict` endpoint when a trained and evaluated model is available.

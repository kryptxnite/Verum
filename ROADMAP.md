# Roadmap

Planned work for Verum, in order of priority.

## 1. Tests and CI
- [ ] Add tests for models, views, search and comments (pytest-django)
- [ ] Set up GitHub Actions: run tests and a linter (ruff) on every push

## 2. Security and configuration
- [ ] Split settings into base / development / production
- [ ] Load all configuration from environment variables, add `.env.example`
- [ ] Add spam protection and moderation for comments (honeypot field, rate limiting, approve-before-publish)
- [ ] Collect only the minimum data in the comment form (email optional)

## 3. Docker and deployment
- [ ] Add Dockerfile and docker-compose (Django + PostgreSQL)
- [ ] Serve static files properly (WhiteNoise)
- [ ] Deploy a public demo with sample data and add a deployment guide to the README

## 4. Performance and features
- [ ] Optimize database queries (`select_related` / `prefetch_related`)
- [ ] Add RSS feed and sitemap.xml

## 5. Documentation
- [ ] Move README screenshots into `docs/` so they display for everyone
- [ ] Describe the data model and project structure in the README

# Xintian Shi — portfolio website

Source for [sxt2918.github.io](https://sxt2918.github.io/), a static portfolio focused
on data analytics, data science, and ML engineering work.

## Principles

- Project claims link to inspectable repositories or dashboards.
- Experimental estimates are labeled as sample results, not production impact.
- Skills are connected to evidence rather than numerical self-ratings.
- Motion respects `prefers-reduced-motion`.

## Local preview and checks

```bash
python -m http.server 8000
python scripts/check_local_assets.py
```

GitHub Actions validates the HTML and verifies that local images, video, and resume links
exist. Media should be compressed before committing; maintain one authoritative source
for resume content and update both exported role-specific PDFs together.

## Updating claims

Quantitative claims should include their population, time period, method, and limitations
in the linked project. Do not describe sample transaction value as prevented loss or an
offline dataset analysis as a production deployment.

## Why

The movies app currently serves 7 templates with zero CSS, no semantic HTML structure, and no accessibility support. Pages render as plain unstyled text on a white background, making the app feel unfinished and unusable on mobile devices. This overhaul brings the frontend to a professional baseline without touching any backend logic.

## What Changes

- **New static asset infrastructure**: Add `apps/movies/static/movies/css/` directory with a single external stylesheet (`style.css`) linked from all templates.
- **Semantic HTML overhaul**: Replace raw `<div>`-like structures in all 7 templates with `<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`, and `<article>` tags.
- **Responsive layout**: Apply Flexbox (and/or CSS Grid) with media queries to support mobile-first and desktop breakpoints across all pages.
- **Accessibility improvements**: Add explicit `<label>` elements for all form inputs, `aria` attributes where appropriate, visible `:focus` indicators, and sufficient color contrast.
- **No backend changes**: Views, forms, models, and URLs remain untouched.

## Capabilities

### New Capabilities

- `movies-static-assets`: CSS file structure, naming conventions, and base layout system for the movies app frontend.
- `movies-responsive-design`: Responsive layout rules, breakpoints, and media query patterns applied across all movies app pages.
- `movies-accessibility`: Accessibility requirements (labels, focus states, ARIA, contrast) for all movies app templates and forms.

### Modified Capabilities

- `movie-views`: Template markup changes (semantic HTML structure) affect the rendering contract for home, list, reserve, and confirmation pages. No URL or view logic changes.
- `user-forms`: Form templates receive explicit `<label>` elements and accessibility attributes. No form logic or validation changes.
- `movie-search`: Search page template receives semantic HTML and accessibility markup. No search behavior changes.

## Impact

- **Code**: All 7 templates in `apps/movies/templates/movies/` are modified. One new file created: `apps/movies/static/movies/css/style.css`.
- **Dependencies**: None added. No new packages or frameworks required.
- **APIs**: None. This is a purely frontend/template change.
- **Risk**: Low. No backend logic is modified. Template rendering paths are unchanged.

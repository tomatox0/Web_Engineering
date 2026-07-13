## 1. Static Asset Infrastructure

- [x] 1.1 Create directory structure `apps/movies/static/movies/css/`
- [x] 1.2 Create `apps/movies/static/movies/css/style.css` with CSS custom properties (`:root` variables for colors, spacing, typography)
- [x] 1.3 Add base body, typography, and link styles to `style.css`

## 2. Semantic HTML — Home Page

- [x] 2.1 Refactor `templates/movies/home.html`: add `<header>` with site title, `<nav>` with navigation links, `<main>` with welcome content, `<footer>` with copyright
- [x] 2.2 Add `{% load static %}` and `<link>` tag for `style.css` in `home.html`

## 3. Semantic HTML — Movie List Page

- [x] 3.1 Refactor `templates/movies/list.html`: add `<header>`, `<nav>`, `<main>` containing `<article>` elements for each movie, `<footer>`
- [x] 3.2 Add `{% load static %}` and `<link>` tag for `style.css` in `list.html`

## 4. Semantic HTML — Search Page

- [x] 4.1 Refactor `templates/movies/search.html`: add `<header>`, `<nav>`, `<main>`, `<footer>`; replace `{{ form.as_p }}` with explicit `<label>` + `<input>` rendering for the search field
- [x] 4.2 Add `{% load static %}` and `<link>` tag for `style.css` in `search.html`

## 5. Semantic HTML — Form Pages (Login, Register, Reserve)

- [x] 5.1 Refactor `templates/movies/login.html`: add semantic structure; replace `{{ form.as_p }}` with explicit `<label>` + `<input>` rendering with `for`/`id` bindings
- [x] 5.2 Add `{% load static %}` and `<link>` tag for `style.css` in `login.html`
- [x] 5.3 Refactor `templates/movies/register.html`: add semantic structure; replace `{{ form.as_p }}` with explicit `<label>` + `<input>` rendering with `for`/`id` bindings
- [x] 5.4 Add `{% load static %}` and `<link>` tag for `style.css` in `register.html`
- [x] 5.5 Refactor `templates/movies/reserve.html`: add semantic structure; replace `{{ form.as_p }}` with explicit `<label>` + `<input>` rendering with `for`/`id` bindings
- [x] 5.6 Add `{% load static %}` and `<link>` tag for `style.css` in `reserve.html`

## 6. Semantic HTML — Confirmation Page

- [x] 6.1 Refactor `templates/movies/confirmation.html`: add `<header>`, `<nav>`, `<main>`, `<footer>` semantic structure
- [x] 6.2 Add `{% load static %}` and `<link>` tag for `style.css` in `confirmation.html`

## 7. Responsive Layout CSS

- [x] 7.1 Add header/nav styles with Flexbox (horizontal on desktop, stacked on mobile via media query at 768px)
- [x] 7.2 Add movie list grid layout (single column mobile, multi-column desktop via CSS Grid)
- [x] 7.3 Add form page layout styles (centered form containers with max-width)
- [x] 7.4 Add footer styles

## 8. Accessibility CSS

- [x] 8.1 Add visible `:focus` outline styles for all interactive elements (`a`, `button`, `input`, `select`, `textarea`)
- [x] 8.2 Add form error styling with `aria-describedby` association support
- [x] 8.3 Verify color contrast ratios meet WCAG AA (4.5:1) for all text/background combinations

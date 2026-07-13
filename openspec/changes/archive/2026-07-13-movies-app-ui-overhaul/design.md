## Context

The movies app (`apps/movies`) has 7 Django templates that render as bare HTML with no styling, no semantic structure, and no accessibility support. The backend (views, forms, models, URLs) is complete and working. The templates use Django's `{{ form.as_p }}` shortcut for forms, which wraps each field in `<p>` tags with auto-generated labels. All templates follow the same pattern: standalone `<!DOCTYPE html>` pages with `<head>` containing only a `<title>` and `<body>` containing raw `<h1>`, `<p>`, `<ul>`, and `<a>` elements.

The app has no static file infrastructure yet. Django's `STATICFILES_DIRS` and `static/` app directory conventions need to be established.

## Goals / Non-Goals

**Goals:**
- Create a single external CSS file with a cohesive design system (colors, typography, spacing, components)
- Restructure all 7 templates using semantic HTML5 elements
- Apply responsive Flexbox/Grid layouts with mobile-first media queries
- Add accessibility: explicit form labels, visible focus indicators, ARIA landmarks, sufficient contrast
- Establish the static file convention for future Django apps in this project

**Non-Goals:**
- Backend logic changes (views, forms, models, URLs stay untouched)
- JavaScript interactivity or client-side frameworks
- Dark mode or theme switching
- Third-party CSS frameworks (Bootstrap, Tailwind, etc.)
- Template inheritance refactoring (each page remains self-contained for now)
- New Django apps or features

## Decisions

### 1. Single CSS file vs. multiple files / CSS preprocessor

**Decision**: One CSS file at `apps/movies/static/movies/css/style.css`.

**Rationale**: The app is small (7 pages). One file keeps things simple, avoids build tooling, and matches the project's straightforward Django stack. If the app grows, CSS can be split later. No Sass/Less/PostCSS — plain CSS is sufficient for the scope.

**Alternatives considered**:
- Multiple CSS files per page: Adds HTTP requests with no real benefit at this scale.
- CSS preprocessor (Sass): Unnecessary complexity for ~500 lines of CSS. Can be added later.

### 2. Flexbox vs. CSS Grid for layout

**Decision**: Flexbox for component-level layout (navbars, card rows, form groups). CSS Grid for page-level layout (header/main/footer stacking, movie card grids on list page).

**Rationale**: Grid excels at 2D page layouts and card grids. Flexbox is simpler for 1D alignment in navbars and form layouts. Using both where each is strongest.

**Alternatives considered**:
- Flexbox only: Would require more nesting for the movie card grid layout.
- CSS Grid only: Overkill for simple navbar alignment.

### 3. Responsive breakpoints

**Decision**: Two breakpoints — mobile (default, < 768px) and desktop (≥ 768px).

**Rationale**: The app has simple content. Two breakpoints cover phone vs. desktop/laptop without over-engineering. The movie list grid collapses from multi-column (desktop) to single-column (mobile).

**Alternatives considered**:
- Three breakpoints (phone/tablet/desktop): Unnecessary complexity for this content.
- Container queries: Not widely supported enough for a Django template project.

### 4. Template structure approach

**Decision**: Each template remains standalone (no `{% extends %}` base template). Add a `<link>` tag and semantic structure to each file individually.

**Rationale**: The user explicitly asked not to change backend logic, and template inheritance is a structural refactor. Keeping templates independent avoids introducing a `base.html` dependency. Template inheritance can be a follow-up change.

**Alternatives considered**:
- Create `base.html` with `{% block %}` tags: Cleaner long-term but out of scope. Changes the template loading contract.

### 5. Form accessibility with `{{ form.as_p }}`

**Decision**: Replace `{{ form.as_p }}` with individual `{{ form.field }}` rendering wrapped in explicit `<label>` and `<div>` containers on all form pages.

**Rationale**: `form.as_p` generates `<p><label>...</label> <input></p>` but doesn't allow custom CSS class hooks or ARIA attributes on the wrapper. Explicit rendering gives full control over accessibility markup and styling.

**Alternatives considered**:
- Keep `form.as_p` and style with `:has()` selectors: Fragile, poor browser support.
- Custom form template filter: Adds Python code for minimal benefit.

### 6. Color and contrast

**Decision**: Use a limited palette — dark navy (`#1a1a2e`) for headers, white backgrounds, accent blue (`#0f3460`) for links/buttons, light gray (`#f5f5f5`) for card backgrounds. All text meets WCAG AA contrast ratio (4.5:1 minimum).

**Rationale**: Professional, clean appearance. High contrast ensures readability. No need for a design system library.

## Risks / Trade-offs

- **[Risk] Template drift from views**: Changing template structure could expose template variable issues not visible in current raw HTML. **Mitigation**: Templates only reference the same context variables; no new variables are introduced. Verify each page renders correctly after changes.
- **[Risk] `form.as_p` replacement is verbose**: Explicitly rendering each form field means more HTML per form page. **Mitigation**: Forms are small (2-4 fields each). The verbosity is manageable and justified by accessibility gains.
- **[Trade-off] No base template**: Duplicated `<head>`, nav, and footer markup across pages. **Mitigation**: Acceptable for 7 pages. Template inheritance is a natural follow-up.
- **[Trade-off] No CSS preprocessor**: Some repeated values (colors, spacing) will appear in multiple places. **Mitigation**: Use CSS custom properties (`:root` variables) to centralize design tokens without build tooling.

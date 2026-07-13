## ADDED Requirements

### Requirement: CSS file location and linking

The system SHALL serve a single CSS file at `apps/movies/static/movies/css/style.css` linked from all movies app templates via the `{% static %}` template tag.

#### Scenario: CSS file exists at expected path
- **WHEN** the Django static file system resolves `movies/css/style.css`
- **THEN** the file is found at `apps/movies/static/movies/css/style.css`

#### Scenario: CSS is linked in all templates
- **WHEN** any of the 7 movies app templates renders
- **THEN** the HTML `<head>` contains a `<link rel="stylesheet" href="{% static 'movies/css/style.css' %}">` tag

### Requirement: CSS design tokens via custom properties

The system SHALL define all colors, spacing, and typography values as CSS custom properties on the `:root` selector.

#### Scenario: Custom properties are defined
- **WHEN** the CSS file is parsed
- **THEN** `:root` contains CSS custom properties for at minimum: `--color-primary`, `--color-accent`, `--color-bg`, `--color-text`, `--spacing-sm`, `--spacing-md`, `--spacing-lg`, `--font-family-base`

### Requirement: Base component styles

The system SHALL provide base styles for the following elements: `body`, `h1`-`h3`, `a`, `button`, `form`, `input`, `nav`, `main`, `section`, `header`, `footer`.

#### Scenario: Body has base typography
- **WHEN** the CSS file is applied
- **THEN** `body` has a `font-family`, `line-height`, `color`, and `background-color` set

#### Scenario: Links have consistent styling
- **WHEN** the CSS file is applied
- **THEN** all `a` elements use `--color-accent` for color and show an underline on hover

## MODIFIED Requirements

### Requirement: Movie search
The system SHALL provide a movie search page at `/search/` that accepts a `q` query parameter via GET, filters `Movie` records by title (case-insensitive contains) or description (case-insensitive contains), and renders matching results inside semantic HTML structure with an explicit `<label>` for the search input.

#### Scenario: Search finds results
- **WHEN** a user submits a GET request to `/search/?q=inception`
- **THEN** the system returns HTTP 200 and renders `movies/search.html` with a list of movies whose title or description contains "inception"

#### Scenario: Search returns no results
- **WHEN** a user submits a GET request to `/search/?q=zzzzznotfound`
- **THEN** the system returns HTTP 200 and renders `movies/search.html` with an empty results message

#### Scenario: Empty query
- **WHEN** a user navigates to `/search/` without a `q` parameter or with an empty `q`
- **THEN** the system returns HTTP 200 and renders `movies/search.html` with an empty form and no results

#### Scenario: Search form has accessible label
- **WHEN** the search page renders
- **THEN** the search input field has a visible `<label>` element with `for` attribute matching the input's `id`

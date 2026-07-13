## ADDED Requirements

### Requirement: Mobile-first responsive layout

The system SHALL use a mobile-first approach where the base CSS targets small screens and `@media (min-width: 768px)` rules adapt the layout for desktop.

#### Scenario: Mobile layout renders single column
- **WHEN** the viewport width is less than 768px
- **THEN** all page content stacks in a single column with full-width elements

#### Scenario: Desktop layout renders multi-column where appropriate
- **WHEN** the viewport width is 768px or greater
- **THEN** the movie list displays movies in a multi-column grid (2-3 columns) and nav items align horizontally

### Requirement: Page layout structure

The system SHALL render each page with a consistent vertical flow: `<header>` (site title + nav) → `<main>` (page content) → `<footer>` (copyright/links), stacked vertically.

#### Scenario: Header-main-footer stacking
- **WHEN** any page renders
- **THEN** the layout shows header at top, main content in the middle, and footer at bottom in a vertical stack

### Requirement: Movie list grid layout

The system SHALL display movie entries in the list page using a CSS Grid (or Flexbox) that shows 1 column on mobile and 2-3 columns on desktop.

#### Scenario: Single column on mobile
- **WHEN** the movie list renders on a viewport < 768px
- **THEN** each movie entry occupies the full width

#### Scenario: Multi-column grid on desktop
- **WHEN** the movie list renders on a viewport >= 768px
- **THEN** movie entries are arranged in a grid with 2-3 columns

### Requirement: Navigation bar responsiveness

The system SHALL render navigation links in a horizontal row on desktop and in a stacked/vertical layout on mobile.

#### Scenario: Horizontal nav on desktop
- **WHEN** the viewport >= 768px
- **THEN** navigation links display in a horizontal row

#### Scenario: Stacked nav on mobile
- **WHEN** the viewport < 768px
- **THEN** navigation links stack vertically

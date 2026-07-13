# Movies Accessibility

Accessibility requirements for the movies app UI.

## Requirements

### Requirement: Explicit form labels

The system SHALL render a visible `<label>` element with a `for` attribute matching the input's `id` for every form input on registration, login, search, and reservation pages.

#### Scenario: Every input has a matching label

- **WHEN** any form page renders (register, login, search, reserve)
- **THEN** each `<input>` (and `<select>`, `<textarea>`) has a corresponding `<label for="<input-id>">` element

### Requirement: Visible focus indicators

The system SHALL display a visible focus ring (outline) on all interactive elements (`a`, `button`, `input`, `select`, `textarea`) when they receive keyboard focus.

#### Scenario: Focus ring visible on keyboard focus

- **WHEN** a user tabs to an interactive element
- **THEN** a visible outline (not `outline: none`) appears around the element with sufficient contrast against the background

### Requirement: ARIA landmarks

The system SHALL include ARIA landmark roles on semantic HTML elements: `<header>` as `banner`, `<nav>` as `navigation`, `<main>` as `main`, `<footer>` as `contentinfo`.

#### Scenario: Landmark roles present

- **WHEN** any page renders
- **THEN** the HTML contains `<header>`, `<nav>`, `<main>`, and `<footer>` elements (implicit ARIA roles apply)

### Requirement: Sufficient color contrast

The system SHALL ensure all text meets WCAG AA contrast ratio (4.5:1 for normal text, 3:1 for large text) against its background.

#### Scenario: Normal text contrast

- **WHEN** text renders in the default color against the default background
- **THEN** the contrast ratio is at least 4.5:1

### Requirement: Form error accessibility

The system SHALL display form validation errors in a manner that is associated with the relevant input field (via `aria-describedby` or an error message element linked to the input).

#### Scenario: Error message linked to input

- **WHEN** a form submission fails validation
- **THEN** each error message is programmatically associated with its input field (e.g., via `aria-describedby`)

## 1. Home Page Template Update

- [x] 1.1 Add login link to `apps/movies/templates/movies/home.html` using `{% url 'login' %}`
- [x] 1.2 Add register link to `apps/movies/templates/movies/home.html` using `{% url 'register' %}`
- [x] 1.3 Add search link to `apps/movies/templates/movies/home.html` using `{% url 'movie-search' %}`

## 2. Verification

- [x] 2.1 Run the dev server and confirm all three links render correctly
- [x] 2.2 Click each link to verify it navigates to the correct page
- [x] 2.3 Run `pytest` to confirm no existing tests are broken

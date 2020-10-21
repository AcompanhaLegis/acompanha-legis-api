# Project description

This is a project for compile data from Dados Abertos da Camara and serve though API to [Camara data portal](https://github.com/AcompanhaLegis/camara-data-portal).

The project uses `Django`.

:sparkles: Contributions are welcomed!

## Highlights on our internal libs

Here we list some of the libraries we use, so you can get familiar with them:

- [Django](https://www.djangoproject.com/) - DjangoThe web framework for perfectionists with deadlines.
- [Django REST framework](https://www.django-rest-framework.org/) -Django REST framework is a powerful and flexible toolkit for building Web APIs.

## Commit messages

We follow this convention to add make the commit messages standard:

All first lines of the commit messages should fit in 50 (70 if you REALLY need it) characters, use the second line and beyond to make any further explanations.
Use the correct emoji as the first thing on the commit message followed by the mentioned starting word (e.g. :bulb: Add my awesome feature)

- When adding a new feature/component/etc: `:bulb:` :bulb: Add ...
- When fixing a bug: `:bug:` :bug: Fix...
- For documentation: `:book:` :book: Docs (for/about/etc)...
- For improvements and updates: `:arrow_up:` :arrow_up: Upgrade/Improve...
- For CI/CD matters: `:cyclone:` :cyclone: No specific words here
- For maintenance: `:wrench:` :wrench: ?
- For removing code: `:fire:` :fire: Remove...

## Issues

When opening issues, try to make your self clear, give examples and/or code snippets. You can either write it in English (preferred) or Portguese, if there's further interest of people that can only understand one of these languages, let us know on the issue and we will try to translate it.

> If you would like to suggest some templates, go ahead, we didn't make time for it yet.

You can suggest implementations approaches, fixes, etc. Sometimes we need to make tough decisions on either implement something or not, but since the
project is open source, you can have your own fork within your more urgent or "refused" ideas.

:warning: Overall, be respectful while discussing the issues, it should be a friendly environment for anyone interested on the project.

# Testing

If you are writing new code, remember adding tests to confirm your code behaves as expected. Same is valid when you are refactoring or changing old code, but also make sure you had run previous tests to guarantee your changes didn't affect the application unexpectedly.

To execute tests, run:

```bash
  $ docker-compose exec api python manage.py test
```

Not familiar with tests? We recommend starting with these Django testing tutorials - [Testing in Django](https://docs.djangoproject.com/en/dev/topics/testing/) and [Testing tutorial](https://docs.djangoproject.com/en/dev/intro/tutorial05/)

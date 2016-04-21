[ ![Codeship Status for Kagiso-Future-Media/kagiso_smart_404](https://codeship.com/projects/40725960-e9d1-0133-fac7-4afac8d396b8/status?branch=master)](https://codeship.com/projects/147691)
[![codecov.io](https://codecov.io/github/Kagiso-Future-Media/kagiso_smart_404/coverage.svg?branch=master)](https://codecov.io/github/Kagiso-Future-Media/kagiso_smart_404?branch=master)

# kagiso_smart_404
Recommend similar pages if a given page is not found.

If a page is not found, looks up the pages in the database
and returns any page with a similarly spelt slug, using trigrams for matching

## Installation
`pip install kagiso_smart_404`

Add `kagiso_smart_404` to your `INSTALLED_APPS` in your `settings.py`.

`python manage.py migrate`

Add the following to `urls.py`:
`handler404 = 'kagiso_smart_404.views.not_found`

## Sample 404 Page
```html
{% extends "core/base.html" %}
{% load staticfiles %}
{% load wagtailcore_tags %}
{% load core_tags %}

{% block title %}404 error{% endblock %}

{% block body_class %}template-404{% endblock %}

{% block content %}
  <section class="error-page-wrapper error-404">
    <div class="error-message-block">
      <h1 class="error-title">404 Error</h1>
      <h4 class="error-subtitle">frequency not found</h4>
      {% if suggested_page %}
      <p>Were you looking for
        <a style="color: white; text-decoration: underline" href="{% pageurl suggested_page %}">
          {{ suggested_page.title }}?
        </a>
      </p>
      {% else %}
        <p>The page you were looking for could not be found.</p>
      {% endif %}
    </div>
  </section>

{% endblock %}
```

## Running the tests
```
py.test
```

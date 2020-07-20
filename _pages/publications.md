---
layout: archive
title: "Selected Publications"
permalink: /publications/
author_profile: true
---

A complete list of publications can be found on my [google scholar](https://scholar.google.com/citations?user=bGjqBxIAAAAJ&hl=en&authuser=1) page.

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}

---
layout: page
permalink: /group/
title: group
description: the Tianyi Lab — current Ph.D. students, alumni, and close collaborators.
nav: true
nav_order: 3
---

<ul class="stat-strip" aria-label="Group statistics">
  <li><a href="#current-phd-students"><span class="stat-value">{{ site.data.group.current | size }}</span><span class="stat-label">current Ph.D. students</span></a></li>
  <li><a href="#alumni"><span class="stat-value">{{ site.data.group.alumni | size }}</span><span class="stat-label">alumni</span></a></li>
  <li><a href="#collaborating-phd-students"><span class="stat-value">{{ site.data.group.collaborators | size }}</span><span class="stat-label">collaborating Ph.D. students</span></a></li>
</ul>

<div class="callout" markdown="1">
**Prospective students and interns.** I work with Ph.D. students, visiting students and interns on LLM reasoning, multimodal and agentic models, data-centric learning and human–AI alignment. If you would like to work with me, please email your CV, a short note on which of our [papers](/publications/) you would build on, and links to any code or writing of yours. I read every message but can only reply to those that fit the group's current directions.
</div>

## Current Ph.D. students

<div class="people-grid">
{% for p in site.data.group.current %}
  <div class="person-card">
    <img class="person-photo" src="{{ p.photo | default: 'placeholder.svg' | prepend: '/assets/img/people/' | relative_url }}" alt="{{ p.name }}" loading="lazy">
    <div class="person-name">{% if p.url %}<a href="{{ p.url }}">{{ p.name }}</a>{% else %}{{ p.name }}{% endif %}</div>
    {% if p.note %}<div class="person-note">{{ p.note }}</div>{% endif %}
  </div>
{% endfor %}
</div>

## Alumni

<div class="people-grid">
{% for p in site.data.group.alumni %}
  <div class="person-card">
    <img class="person-photo" src="{{ p.photo | default: 'placeholder.svg' | prepend: '/assets/img/people/' | relative_url }}" alt="{{ p.name }}" loading="lazy">
    <div class="person-name">{% if p.url %}<a href="{{ p.url }}">{{ p.name }}</a>{% else %}{{ p.name }}{% endif %}</div>
    {% if p.note %}<div class="person-note">{{ p.note }}</div>{% endif %}
  </div>
{% endfor %}
</div>

## Collaborating Ph.D. students

<p class="text-muted">Students at other groups and institutions I work closely with.</p>
<ul class="collab-list">
{% for p in site.data.group.collaborators %}
  <li>{% if p.url %}<a href="{{ p.url }}">{{ p.name }}</a>{% else %}{{ p.name }}{% endif %}{% if p.note %} — {{ p.note }}{% endif %}</li>
{% endfor %}
</ul>

## Code, data and models

Our releases live at [github.com/tianyi-lab](https://github.com/tianyi-lab) and [huggingface.co/umd-zhou-lab](https://huggingface.co/umd-zhou-lab).

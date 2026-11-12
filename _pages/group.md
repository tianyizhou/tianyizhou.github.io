---
layout: page
permalink: /group/
title: group
description: the Tianyi Lab — current Ph.D. students, alumni, mentored students and collaborators.
nav: true
nav_order: 3
---

<ul class="stat-strip" aria-label="Group statistics">
  <li><a href="#current-phd-students"><span class="stat-value">{{ site.data.group.current | size }}</span><span class="stat-label">current Ph.D. students</span></a></li>
  <li><a href="#phd-alumni"><span class="stat-value">{{ site.data.group.phd_alumni | size | plus: site.data.group.ms_alumni.size }}</span><span class="stat-label">Ph.D. and M.S. alumni</span></a></li>
  <li><a href="#mentored-students"><span class="stat-value">{{ site.data.group.mentored | size }}</span><span class="stat-label">mentored students</span></a></li>
  <li><a href="#collaborating-students"><span class="stat-value">{{ site.data.group.collaborators | size }}</span><span class="stat-label">collaborating students</span></a></li>
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

## Ph.D. alumni
{: #phd-alumni}

<p class="text-muted">Graduated from UMD.</p>
<div class="people-grid">
{% for p in site.data.group.phd_alumni %}
  <div class="person-card">
    <img class="person-photo" src="{{ p.photo | default: 'placeholder.svg' | prepend: '/assets/img/people/' | relative_url }}" alt="{{ p.name }}" loading="lazy">
    <div class="person-name">{% if p.url %}<a href="{{ p.url }}">{{ p.name }}</a>{% else %}{{ p.name }}{% endif %}</div>
    {% if p.note %}<div class="person-note">{{ p.note }}</div>{% endif %}
  </div>
{% endfor %}
</div>

## M.S. alumni
{: #ms-alumni}

<div class="people-grid">
{% for p in site.data.group.ms_alumni %}
  <div class="person-card">
    <img class="person-photo" src="{{ p.photo | default: 'placeholder.svg' | prepend: '/assets/img/people/' | relative_url }}" alt="{{ p.name }}" loading="lazy">
    <div class="person-name">{% if p.url %}<a href="{{ p.url }}">{{ p.name }}</a>{% else %}{{ p.name }}{% endif %}</div>
    {% if p.note %}<div class="person-note">{{ p.note }}</div>{% endif %}
  </div>
{% endfor %}
</div>

## Mentored students
{: #mentored-students}

<p class="text-muted">Ph.D. students at other groups whose thesis work I closely mentored.</p>
<div class="people-grid">
{% for p in site.data.group.mentored %}
  <div class="person-card">
    <img class="person-photo" src="{{ p.photo | default: 'placeholder.svg' | prepend: '/assets/img/people/' | relative_url }}" alt="{{ p.name }}" loading="lazy">
    <div class="person-name">{% if p.url %}<a href="{{ p.url }}">{{ p.name }}</a>{% else %}{{ p.name }}{% endif %}</div>
    {% if p.note %}<div class="person-note">{{ p.note }}</div>{% endif %}
  </div>
{% endfor %}
</div>

## Collaborating students
{: #collaborating-students}

<ul class="collab-list">
{% for p in site.data.group.collaborators %}
  <li>{% if p.url %}<a href="{{ p.url }}">{{ p.name }}</a>{% else %}{{ p.name }}{% endif %}{% if p.note %} ({{ p.note }}){% endif %}</li>
{% endfor %}
</ul>

## Code, data and models

Our releases live at [github.com/tianyi-lab](https://github.com/tianyi-lab) and [huggingface.co/umd-zhou-lab](https://huggingface.co/umd-zhou-lab).

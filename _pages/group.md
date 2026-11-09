---
layout: page
permalink: /group/
title: group
description: the Tianyi Lab at UMD — current students, alumni, and collaborators.
nav: true
nav_order: 3
toc:
  sidebar: left
---

<div class="alert alert-secondary p-3 mb-4" markdown="1" style="border-left: 4px solid var(--global-theme-color); border-radius: .35rem;">
**Prospective students.** I recruit Ph.D. students every year through the [UMD CS Ph.D. program](https://www.cs.umd.edu/grad/phd-program) (apply by the December deadline and list me as a potential advisor). I am also happy to work with current UMD students and with strong visiting students or interns on LLM reasoning, multimodal/agentic models, data-centric learning and alignment. If you email me, please include your CV, a short note on which of our [papers](/publications/) you would want to build on, and links to any code or writing of yours. I read every message but can only reply to those that fit the group's current directions.
</div>

## Current Ph.D. students

<div class="row row-cols-1 row-cols-md-2 g-3 mb-4">
{% assign students = site.data.group.current %}
{% for p in students %}
  <div class="col">
    <div class="card h-100 hoverable">
      <div class="card-body py-3">
        <h5 class="card-title mb-1">{% if p.url %}<a href="{{ p.url }}">{{ p.name }}</a>{% else %}{{ p.name }}{% endif %}</h5>
        {% if p.note %}<p class="card-text small text-muted mb-0">{{ p.note }}</p>{% endif %}
      </div>
    </div>
  </div>
{% endfor %}
</div>

## Alumni

<ul class="mb-4">
{% for p in site.data.group.alumni %}
  <li>{% if p.url %}<a href="{{ p.url }}">{{ p.name }}</a>{% else %}{{ p.name }}{% endif %}{% if p.note %} — {{ p.note }}{% endif %}</li>
{% endfor %}
</ul>

## Collaborating Ph.D. students

<p class="text-muted small">Students at other groups and institutions I work closely with.</p>
<ul class="mb-4">
{% for p in site.data.group.collaborators %}
  <li>{% if p.url %}<a href="{{ p.url }}">{{ p.name }}</a>{% else %}{{ p.name }}{% endif %}{% if p.note %} — {{ p.note }}{% endif %}</li>
{% endfor %}
</ul>

## Code, data and models

Our releases live at [github.com/tianyi-lab](https://github.com/tianyi-lab) and [huggingface.co/umd-zhou-lab](https://huggingface.co/umd-zhou-lab). We are also part of [TurningPoint AI](https://www.turningpoint-ai.com/), a multi-university team (UMD, UCLA, PSU, Google) on multimodal agents.

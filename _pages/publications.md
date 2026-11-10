---
layout: page
permalink: /publications/
title: publications
description: peer-reviewed conference and journal papers, by year. Oral / Spotlight / award papers are badged; GitHub stars and citation counts are shown where available. Preprints are listed by topic on the research page.
nav: true
nav_order: 1
---

{% include pub_stats.liquid %}

{% include bib_search.liquid %}

<div class="publications">

{% bibliography --query @*[keywords ~= status:published;] %}

</div>

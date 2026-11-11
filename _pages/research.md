---
layout: page
permalink: /research/
title: research
description: our papers organized by topic, preprints first, then published work. The same papers listed by year are on the publications page.
nav: true
nav_order: 2
---

<nav class="topic-nav" aria-label="Research topics">
  <div class="topic-nav-total"><strong>{{ site.data.pubstats.published | plus: site.data.pubstats.preprints }}</strong> papers &nbsp;·&nbsp; {{ site.data.pubstats.published }} published &nbsp;·&nbsp; {{ site.data.pubstats.preprints }} preprints</div>
  <a class="topic-nav-section" href="#large-language-models">Large Language Models <span class="nav-count">{{ site.data.pubstats.sections.llm }}</span></a>
  <a class="topic-nav-section" href="#multimodal-models">Multimodal Models <span class="nav-count">{{ site.data.pubstats.sections.mllm }}</span></a>
  <a class="topic-nav-section" href="#agents-world-models">Agents & World Models <span class="nav-count">{{ site.data.pubstats.sections.agents }}</span></a>
  <a class="topic-nav-section" href="#learning-paradigms">Learning Paradigms <span class="nav-count">{{ site.data.pubstats.sections.paradigms }}</span></a>
  <a class="topic-nav-section" href="#foundations-earlier-work">Foundations & Earlier Work <span class="nav-count">{{ site.data.pubstats.sections.foundations }}</span></a>
</nav>

<p class="research-hint">Click a topic to expand its papers. <button type="button" class="expand-all" id="expand-all">Expand all</button></p>

<h2 id="large-language-models" class="research-section">Large Language Models</h2>
<div class="subtopic-chips"><a href="#large-language-models-data-selection-curriculum-synthetic-data">Data Selection, Curriculum & Synthetic Data</a><a href="#large-language-models-post-training-reasoning">Post-training & Reasoning</a><a href="#large-language-models-human-ai-alignment-reward-hacking">Human–AI Alignment & Reward Hacking</a><a href="#large-language-models-generalization-memorization-architecture">Generalization, Memorization & Architecture</a><a href="#large-language-models-prompting-test-time-optimization">Prompting & Test-time Optimization</a><a href="#large-language-models-in-context-learning">In-context Learning</a><a href="#large-language-models-efficient-decoding">Efficient Decoding</a><a href="#large-language-models-retrieval-embeddings">Retrieval & Embeddings</a><a href="#large-language-models-safety-jailbreaking">Safety & Jailbreaking</a><a href="#large-language-models-benchmarks-evaluation">Benchmarks & Evaluation</a></div>

<details id="large-language-models-data-selection-curriculum-synthetic-data" class="research-sub">
<summary>Data Selection, Curriculum & Synthetic Data</summary>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:llm__data-selection-training-curriculum-and-synthetic-data;] --group_by none %}
{% bibliography --query @*[keywords ~= published:llm__data-selection-training-curriculum-and-synthetic-data;] --group_by none %}
</div>
</details>

<details id="large-language-models-post-training-reasoning" class="research-sub">
<summary>Post-training & Reasoning</summary>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:llm__post-training-and-reasoning;] --group_by none %}
{% bibliography --query @*[keywords ~= published:llm__post-training-and-reasoning;] --group_by none %}
</div>
</details>

<details id="large-language-models-human-ai-alignment-reward-hacking" class="research-sub">
<summary>Human–AI Alignment & Reward Hacking</summary>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:llm__human-ai-alignment-and-reward-hacking;] --group_by none %}
{% bibliography --query @*[keywords ~= published:llm__human-ai-alignment-and-reward-hacking;] --group_by none %}
</div>
</details>

<details id="large-language-models-generalization-memorization-architecture" class="research-sub">
<summary>Generalization, Memorization & Architecture</summary>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:llm__generalization;] --group_by none %}
{% bibliography --query @*[keywords ~= published:llm__generalization;] --group_by none %}
</div>
</details>

<details id="large-language-models-prompting-test-time-optimization" class="research-sub">
<summary>Prompting & Test-time Optimization</summary>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:llm__prompting-and-test-time-optimization;] --group_by none %}
{% bibliography --query @*[keywords ~= published:llm__prompting-and-test-time-optimization;] --group_by none %}
</div>
</details>

<details id="large-language-models-in-context-learning" class="research-sub">
<summary>In-context Learning</summary>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:llm__in-context-learning;] --group_by none %}
{% bibliography --query @*[keywords ~= published:llm__in-context-learning;] --group_by none %}
</div>
</details>

<details id="large-language-models-efficient-decoding" class="research-sub">
<summary>Efficient Decoding</summary>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:llm__decoding;] --group_by none %}
{% bibliography --query @*[keywords ~= published:llm__decoding;] --group_by none %}
</div>
</details>

<details id="large-language-models-retrieval-embeddings" class="research-sub">
<summary>Retrieval & Embeddings</summary>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:llm__retrieval-augmented-generation;] --group_by none %}
{% bibliography --query @*[keywords ~= published:llm__retrieval-augmented-generation;] --group_by none %}
</div>
</details>

<details id="large-language-models-safety-jailbreaking" class="research-sub">
<summary>Safety & Jailbreaking</summary>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:llm__safety;] --group_by none %}
{% bibliography --query @*[keywords ~= published:llm__safety;] --group_by none %}
</div>
</details>

<details id="large-language-models-benchmarks-evaluation" class="research-sub">
<summary>Benchmarks & Evaluation</summary>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:llm__benchmarks-and-evaluation;] --group_by none %}
{% bibliography --query @*[keywords ~= published:llm__benchmarks-and-evaluation;] --group_by none %}
</div>
</details>

<h2 id="multimodal-models" class="research-section">Multimodal Models</h2>
<div class="subtopic-chips"><a href="#multimodal-models-architectures-unified-models">Architectures & Unified Models</a><a href="#multimodal-models-post-training-alignment">Post-training & Alignment</a><a href="#multimodal-models-benchmarks-hallucination-evaluation">Benchmarks, Hallucination & Evaluation</a><a href="#multimodal-models-test-time-optimization">Test-time Optimization</a><a href="#multimodal-models-diffusion-models">Diffusion Models</a></div>

<details id="multimodal-models-architectures-unified-models" class="research-sub">
<summary>Architectures & Unified Models</summary>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:mllm__model-architecture-and-training-recipe;] --group_by none %}
{% bibliography --query @*[keywords ~= published:mllm__model-architecture-and-training-recipe;] --group_by none %}
</div>
</details>

<details id="multimodal-models-post-training-alignment" class="research-sub">
<summary>Post-training & Alignment</summary>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:mllm__post-training;] --group_by none %}
{% bibliography --query @*[keywords ~= published:mllm__post-training;] --group_by none %}
</div>
</details>

<details id="multimodal-models-benchmarks-hallucination-evaluation" class="research-sub">
<summary>Benchmarks, Hallucination & Evaluation</summary>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:mllm__benchmarks-and-evaluation;] --group_by none %}
{% bibliography --query @*[keywords ~= published:mllm__benchmarks-and-evaluation;] --group_by none %}
</div>
</details>

<details id="multimodal-models-test-time-optimization" class="research-sub">
<summary>Test-time Optimization</summary>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:mllm__test-time-optimization;] --group_by none %}
{% bibliography --query @*[keywords ~= published:mllm__test-time-optimization;] --group_by none %}
</div>
</details>

<details id="multimodal-models-diffusion-models" class="research-sub">
<summary>Diffusion Models</summary>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:diffusion-models;] --group_by none %}
{% bibliography --query @*[keywords ~= published:diffusion-models;] --group_by none %}
</div>
</details>

<h2 id="agents-world-models" class="research-section">Agents & World Models</h2>
<div class="subtopic-chips"><a href="#agents-world-models-agents-world-models-embodied-ai">Agents, World Models & Embodied AI</a><a href="#agents-world-models-reinforcement-learning">Reinforcement Learning</a></div>

<details id="agents-world-models-agents-world-models-embodied-ai" class="research-sub">
<summary>Agents, World Models & Embodied AI</summary>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:agents-and-world-models;] --group_by none %}
{% bibliography --query @*[keywords ~= published:agents-and-world-models;] --group_by none %}
</div>
</details>

<details id="agents-world-models-reinforcement-learning" class="research-sub">
<summary>Reinforcement Learning</summary>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:reinforcement-learning;] --group_by none %}
{% bibliography --query @*[keywords ~= published:reinforcement-learning;] --group_by none %}
</div>
</details>

<h2 id="learning-paradigms" class="research-section">Learning Paradigms</h2>
<div class="subtopic-chips"><a href="#learning-paradigms-curriculum-learning-data-selection">Curriculum Learning & Data Selection</a><a href="#learning-paradigms-data-augmentation-synthesis">Data Augmentation & Synthesis</a><a href="#learning-paradigms-continual-learning">Continual Learning</a><a href="#learning-paradigms-transfer-multi-task-meta-learning">Transfer, Multi-task & Meta-learning</a><a href="#learning-paradigms-federated-collaborative-learning">Federated & Collaborative Learning</a></div>

<details id="learning-paradigms-curriculum-learning-data-selection" class="research-sub">
<summary>Curriculum Learning & Data Selection</summary>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:curriculum-learning-and-data-selection;] --group_by none %}
{% bibliography --query @*[keywords ~= published:curriculum-learning-and-data-selection;] --group_by none %}
</div>
</details>

<details id="learning-paradigms-data-augmentation-synthesis" class="research-sub">
<summary>Data Augmentation & Synthesis</summary>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:data-augmentation-and-synthesis;] --group_by none %}
{% bibliography --query @*[keywords ~= published:data-augmentation-and-synthesis;] --group_by none %}
</div>
</details>

<details id="learning-paradigms-continual-learning" class="research-sub">
<summary>Continual Learning</summary>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:continual-learning-plasticity-stability-trade-off;] --group_by none %}
{% bibliography --query @*[keywords ~= published:continual-learning-plasticity-stability-trade-off;] --group_by none %}
</div>
</details>

<details id="learning-paradigms-transfer-multi-task-meta-learning" class="research-sub">
<summary>Transfer, Multi-task & Meta-learning</summary>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:transfer-learning-multi-task-learning-meta-learning;] --group_by none %}
{% bibliography --query @*[keywords ~= published:transfer-learning-multi-task-learning-meta-learning;] --group_by none %}
</div>
</details>

<details id="learning-paradigms-federated-collaborative-learning" class="research-sub">
<summary>Federated & Collaborative Learning</summary>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:distributed-and-collaborative-learning;] --group_by none %}
{% bibliography --query @*[keywords ~= published:distributed-and-collaborative-learning;] --group_by none %}
</div>
</details>

<h2 id="foundations-earlier-work" class="research-section">Foundations & Earlier Work</h2>
<div class="subtopic-chips"><a href="#foundations-earlier-work-attention-nlp-pre-llm">Attention & NLP (pre-LLM)</a><a href="#foundations-earlier-work-matrix-factorization-disentanglement">Matrix Factorization & Disentanglement</a><a href="#foundations-earlier-work-compressed-sensing-sparse-learning">Compressed Sensing & Sparse Learning</a><a href="#foundations-earlier-work-optimization">Optimization</a></div>

<details id="foundations-earlier-work-attention-nlp-pre-llm" class="research-sub">
<summary>Attention & NLP (pre-LLM)</summary>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:natural-language-processing;] --group_by none %}
{% bibliography --query @*[keywords ~= published:natural-language-processing;] --group_by none %}
</div>
</details>

<details id="foundations-earlier-work-matrix-factorization-disentanglement" class="research-sub">
<summary>Matrix Factorization & Disentanglement</summary>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:matrix-factorization-and-feature-disentanglement;] --group_by none %}
{% bibliography --query @*[keywords ~= published:matrix-factorization-and-feature-disentanglement;] --group_by none %}
</div>
</details>

<details id="foundations-earlier-work-compressed-sensing-sparse-learning" class="research-sub">
<summary>Compressed Sensing & Sparse Learning</summary>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:compressed-sensing-sparse-dimension-reduction;] --group_by none %}
{% bibliography --query @*[keywords ~= published:compressed-sensing-sparse-dimension-reduction;] --group_by none %}
</div>
</details>

<details id="foundations-earlier-work-optimization" class="research-sub">
<summary>Optimization</summary>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:optimization;] --group_by none %}
{% bibliography --query @*[keywords ~= published:optimization;] --group_by none %}
</div>
</details>

<script>
  (function () {
    function openTarget() {
      var id = decodeURIComponent(location.hash.slice(1));
      var el = id && document.getElementById(id);
      if (el && el.tagName === "DETAILS") { el.open = true; el.scrollIntoView(); }
    }
    window.addEventListener("hashchange", openTarget);
    document.addEventListener("DOMContentLoaded", function () {
      openTarget();
      var btn = document.getElementById("expand-all");
      btn.addEventListener("click", function () {
        var all = document.querySelectorAll("details.research-sub");
        var open = btn.textContent === "Expand all";
        all.forEach(function (d) { d.open = open; });
        btn.textContent = open ? "Collapse all" : "Expand all";
      });
    });
  })();
</script>

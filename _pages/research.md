---
layout: page
permalink: /research/
title: research
description: our papers organized by topic, preprints first, then published work. The same papers listed by year are on the publications page.
nav: true
nav_order: 2
---

{% include pub_stats.liquid %}

<nav class="topic-nav" aria-label="Research topics">
  <a class="topic-nav-section" href="#large-language-models">Large Language Models</a>
  <a class="topic-nav-section" href="#multimodal-models">Multimodal Models</a>
  <a class="topic-nav-section" href="#agents-world-models">Agents & World Models</a>
  <a class="topic-nav-section" href="#learning-paradigms">Learning Paradigms</a>
  <a class="topic-nav-section" href="#foundations-earlier-work">Foundations & Earlier Work</a>
</nav>

<h2 id="large-language-models" class="research-section">Large Language Models</h2>
<div class="subtopic-chips"><a href="#large-language-models-data-selection-curriculum-synthetic-data">Data Selection, Curriculum & Synthetic Data</a><a href="#large-language-models-post-training-reasoning">Post-training & Reasoning</a><a href="#large-language-models-human-ai-alignment-reward-hacking">Human–AI Alignment & Reward Hacking</a><a href="#large-language-models-generalization-memorization-architecture">Generalization, Memorization & Architecture</a><a href="#large-language-models-prompting-test-time-optimization">Prompting & Test-time Optimization</a><a href="#large-language-models-in-context-learning">In-context Learning</a><a href="#large-language-models-efficient-decoding">Efficient Decoding</a><a href="#large-language-models-retrieval-embeddings">Retrieval & Embeddings</a><a href="#large-language-models-safety-jailbreaking">Safety & Jailbreaking</a><a href="#large-language-models-benchmarks-evaluation">Benchmarks & Evaluation</a></div>

<h3 id="large-language-models-data-selection-curriculum-synthetic-data" class="research-subsection">Data Selection, Curriculum & Synthetic Data</h3>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:llm__data-selection-training-curriculum-and-synthetic-data;] --group_by none %}
{% bibliography --query @*[keywords ~= published:llm__data-selection-training-curriculum-and-synthetic-data;] --group_by none %}
</div>

<h3 id="large-language-models-post-training-reasoning" class="research-subsection">Post-training & Reasoning</h3>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:llm__post-training-and-reasoning;] --group_by none %}
{% bibliography --query @*[keywords ~= published:llm__post-training-and-reasoning;] --group_by none %}
</div>

<h3 id="large-language-models-human-ai-alignment-reward-hacking" class="research-subsection">Human–AI Alignment & Reward Hacking</h3>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:llm__human-ai-alignment-and-reward-hacking;] --group_by none %}
{% bibliography --query @*[keywords ~= published:llm__human-ai-alignment-and-reward-hacking;] --group_by none %}
</div>

<h3 id="large-language-models-generalization-memorization-architecture" class="research-subsection">Generalization, Memorization & Architecture</h3>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:llm__generalization;] --group_by none %}
{% bibliography --query @*[keywords ~= published:llm__generalization;] --group_by none %}
</div>

<h3 id="large-language-models-prompting-test-time-optimization" class="research-subsection">Prompting & Test-time Optimization</h3>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:llm__prompting-and-test-time-optimization;] --group_by none %}
{% bibliography --query @*[keywords ~= published:llm__prompting-and-test-time-optimization;] --group_by none %}
</div>

<h3 id="large-language-models-in-context-learning" class="research-subsection">In-context Learning</h3>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:llm__in-context-learning;] --group_by none %}
{% bibliography --query @*[keywords ~= published:llm__in-context-learning;] --group_by none %}
</div>

<h3 id="large-language-models-efficient-decoding" class="research-subsection">Efficient Decoding</h3>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:llm__decoding;] --group_by none %}
{% bibliography --query @*[keywords ~= published:llm__decoding;] --group_by none %}
</div>

<h3 id="large-language-models-retrieval-embeddings" class="research-subsection">Retrieval & Embeddings</h3>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:llm__retrieval-augmented-generation;] --group_by none %}
{% bibliography --query @*[keywords ~= published:llm__retrieval-augmented-generation;] --group_by none %}
</div>

<h3 id="large-language-models-safety-jailbreaking" class="research-subsection">Safety & Jailbreaking</h3>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:llm__safety;] --group_by none %}
{% bibliography --query @*[keywords ~= published:llm__safety;] --group_by none %}
</div>

<h3 id="large-language-models-benchmarks-evaluation" class="research-subsection">Benchmarks & Evaluation</h3>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:llm__benchmarks-and-evaluation;] --group_by none %}
{% bibliography --query @*[keywords ~= published:llm__benchmarks-and-evaluation;] --group_by none %}
</div>

<h2 id="multimodal-models" class="research-section">Multimodal Models</h2>
<div class="subtopic-chips"><a href="#multimodal-models-architectures-unified-models">Architectures & Unified Models</a><a href="#multimodal-models-post-training-alignment">Post-training & Alignment</a><a href="#multimodal-models-benchmarks-hallucination-evaluation">Benchmarks, Hallucination & Evaluation</a><a href="#multimodal-models-test-time-optimization">Test-time Optimization</a><a href="#multimodal-models-diffusion-models">Diffusion Models</a></div>

<h3 id="multimodal-models-architectures-unified-models" class="research-subsection">Architectures & Unified Models</h3>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:mllm__model-architecture-and-training-recipe;] --group_by none %}
{% bibliography --query @*[keywords ~= published:mllm__model-architecture-and-training-recipe;] --group_by none %}
</div>

<h3 id="multimodal-models-post-training-alignment" class="research-subsection">Post-training & Alignment</h3>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:mllm__post-training;] --group_by none %}
{% bibliography --query @*[keywords ~= published:mllm__post-training;] --group_by none %}
</div>

<h3 id="multimodal-models-benchmarks-hallucination-evaluation" class="research-subsection">Benchmarks, Hallucination & Evaluation</h3>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:mllm__benchmarks-and-evaluation;] --group_by none %}
{% bibliography --query @*[keywords ~= published:mllm__benchmarks-and-evaluation;] --group_by none %}
</div>

<h3 id="multimodal-models-test-time-optimization" class="research-subsection">Test-time Optimization</h3>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:mllm__test-time-optimization;] --group_by none %}
{% bibliography --query @*[keywords ~= published:mllm__test-time-optimization;] --group_by none %}
</div>

<h3 id="multimodal-models-diffusion-models" class="research-subsection">Diffusion Models</h3>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:diffusion-models;] --group_by none %}
{% bibliography --query @*[keywords ~= published:diffusion-models;] --group_by none %}
</div>

<h2 id="agents-world-models" class="research-section">Agents & World Models</h2>
<div class="subtopic-chips"><a href="#agents-world-models-agents-world-models-embodied-ai">Agents, World Models & Embodied AI</a><a href="#agents-world-models-reinforcement-learning">Reinforcement Learning</a></div>

<h3 id="agents-world-models-agents-world-models-embodied-ai" class="research-subsection">Agents, World Models & Embodied AI</h3>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:agents-and-world-models;] --group_by none %}
{% bibliography --query @*[keywords ~= published:agents-and-world-models;] --group_by none %}
</div>

<h3 id="agents-world-models-reinforcement-learning" class="research-subsection">Reinforcement Learning</h3>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:reinforcement-learning;] --group_by none %}
{% bibliography --query @*[keywords ~= published:reinforcement-learning;] --group_by none %}
</div>

<h2 id="learning-paradigms" class="research-section">Learning Paradigms</h2>
<div class="subtopic-chips"><a href="#learning-paradigms-curriculum-learning-data-selection">Curriculum Learning & Data Selection</a><a href="#learning-paradigms-data-augmentation-synthesis">Data Augmentation & Synthesis</a><a href="#learning-paradigms-continual-learning">Continual Learning</a><a href="#learning-paradigms-transfer-multi-task-meta-learning">Transfer, Multi-task & Meta-learning</a><a href="#learning-paradigms-federated-collaborative-learning">Federated & Collaborative Learning</a></div>

<h3 id="learning-paradigms-curriculum-learning-data-selection" class="research-subsection">Curriculum Learning & Data Selection</h3>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:curriculum-learning-and-data-selection;] --group_by none %}
{% bibliography --query @*[keywords ~= published:curriculum-learning-and-data-selection;] --group_by none %}
</div>

<h3 id="learning-paradigms-data-augmentation-synthesis" class="research-subsection">Data Augmentation & Synthesis</h3>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:data-augmentation-and-synthesis;] --group_by none %}
{% bibliography --query @*[keywords ~= published:data-augmentation-and-synthesis;] --group_by none %}
</div>

<h3 id="learning-paradigms-continual-learning" class="research-subsection">Continual Learning</h3>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:continual-learning-plasticity-stability-trade-off;] --group_by none %}
{% bibliography --query @*[keywords ~= published:continual-learning-plasticity-stability-trade-off;] --group_by none %}
</div>

<h3 id="learning-paradigms-transfer-multi-task-meta-learning" class="research-subsection">Transfer, Multi-task & Meta-learning</h3>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:transfer-learning-multi-task-learning-meta-learning;] --group_by none %}
{% bibliography --query @*[keywords ~= published:transfer-learning-multi-task-learning-meta-learning;] --group_by none %}
</div>

<h3 id="learning-paradigms-federated-collaborative-learning" class="research-subsection">Federated & Collaborative Learning</h3>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:distributed-and-collaborative-learning;] --group_by none %}
{% bibliography --query @*[keywords ~= published:distributed-and-collaborative-learning;] --group_by none %}
</div>

<h2 id="foundations-earlier-work" class="research-section">Foundations & Earlier Work</h2>
<div class="subtopic-chips"><a href="#foundations-earlier-work-attention-nlp-pre-llm">Attention & NLP (pre-LLM)</a><a href="#foundations-earlier-work-matrix-factorization-disentanglement">Matrix Factorization & Disentanglement</a><a href="#foundations-earlier-work-compressed-sensing-sparse-learning">Compressed Sensing & Sparse Learning</a><a href="#foundations-earlier-work-optimization">Optimization</a></div>

<h3 id="foundations-earlier-work-attention-nlp-pre-llm" class="research-subsection">Attention & NLP (pre-LLM)</h3>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:natural-language-processing;] --group_by none %}
{% bibliography --query @*[keywords ~= published:natural-language-processing;] --group_by none %}
</div>

<h3 id="foundations-earlier-work-matrix-factorization-disentanglement" class="research-subsection">Matrix Factorization & Disentanglement</h3>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:matrix-factorization-and-feature-disentanglement;] --group_by none %}
{% bibliography --query @*[keywords ~= published:matrix-factorization-and-feature-disentanglement;] --group_by none %}
</div>

<h3 id="foundations-earlier-work-compressed-sensing-sparse-learning" class="research-subsection">Compressed Sensing & Sparse Learning</h3>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:compressed-sensing-sparse-dimension-reduction;] --group_by none %}
{% bibliography --query @*[keywords ~= published:compressed-sensing-sparse-dimension-reduction;] --group_by none %}
</div>

<h3 id="foundations-earlier-work-optimization" class="research-subsection">Optimization</h3>
<div class="publications research-list">
{% bibliography --query @*[keywords ~= preprint:optimization;] --group_by none %}
{% bibliography --query @*[keywords ~= published:optimization;] --group_by none %}
</div>

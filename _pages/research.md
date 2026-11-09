---
layout: page
permalink: /research/
title: research
description: our papers organized by topic. The same papers, listed by year, are under publications.
nav: true
nav_order: 2
toc:
  sidebar: left
---

<img src="{{ '/assets/img/topics.webp' | relative_url }}" alt="Current research topics of the Tianyi Lab" class="img-fluid rounded z-depth-1" style="width:100%; height:auto;" loading="lazy">


## Large Language Models (LLMs)

### Data Selection, Training Curriculum, and Synthetic Data
<div class="publications">
{% bibliography --query @*[keywords ~= topic:llm__data-selection-training-curriculum-and-synthetic-data;] --group_by none %}
</div>

### Post-training and Reasoning
<div class="publications">
{% bibliography --query @*[keywords ~= topic:llm__post-training-and-reasoning;] --group_by none %}
</div>

### Generalization
<div class="publications">
{% bibliography --query @*[keywords ~= topic:llm__generalization;] --group_by none %}
</div>

### In-Context Learning
<div class="publications">
{% bibliography --query @*[keywords ~= topic:llm__in-context-learning;] --group_by none %}
</div>

### Prompting and Test-Time Optimization
<div class="publications">
{% bibliography --query @*[keywords ~= topic:llm__prompting-and-test-time-optimization;] --group_by none %}
</div>

### Human-AI Alignment and Reward Hacking
<div class="publications">
{% bibliography --query @*[keywords ~= topic:llm__human-ai-alignment-and-reward-hacking;] --group_by none %}
</div>

### Benchmarks and Evaluation
<div class="publications">
{% bibliography --query @*[keywords ~= topic:llm__benchmarks-and-evaluation;] --group_by none %}
</div>

### Safety
<div class="publications">
{% bibliography --query @*[keywords ~= topic:llm__safety;] --group_by none %}
</div>

### Decoding
<div class="publications">
{% bibliography --query @*[keywords ~= topic:llm__decoding;] --group_by none %}
</div>

### Retrieval-Augmented Generation (RAG)
<div class="publications">
{% bibliography --query @*[keywords ~= topic:llm__retrieval-augmented-generation;] --group_by none %}
</div>

## Multimodal Large Language Models (MLLMs)

### Model Architecture and Training Recipe
<div class="publications">
{% bibliography --query @*[keywords ~= topic:mllm__model-architecture-and-training-recipe;] --group_by none %}
</div>

### Post-Training
<div class="publications">
{% bibliography --query @*[keywords ~= topic:mllm__post-training;] --group_by none %}
</div>

### Test-Time Optimization
<div class="publications">
{% bibliography --query @*[keywords ~= topic:mllm__test-time-optimization;] --group_by none %}
</div>

### Benchmarks and Evaluation
<div class="publications">
{% bibliography --query @*[keywords ~= topic:mllm__benchmarks-and-evaluation;] --group_by none %}
</div>

## Diffusion Models
<div class="publications">
{% bibliography --query @*[keywords ~= topic:diffusion-models;] --group_by none %}
</div>

## Agents and World Models
<div class="publications">
{% bibliography --query @*[keywords ~= topic:agents-and-world-models;] --group_by none %}
</div>

## Curriculum Learning and Data Selection
<div class="publications">
{% bibliography --query @*[keywords ~= topic:curriculum-learning-and-data-selection;] --group_by none %}
</div>

## Reinforcement Learning
<div class="publications">
{% bibliography --query @*[keywords ~= topic:reinforcement-learning;] --group_by none %}
</div>

## Natural Language Processing (pre-LLM)
<div class="publications">
{% bibliography --query @*[keywords ~= topic:natural-language-processing;] --group_by none %}
</div>

## Distributed and Collaborative (Federated, Decentralized) Learning
<div class="publications">
{% bibliography --query @*[keywords ~= topic:distributed-and-collaborative-learning;] --group_by none %}
</div>

## Data Augmentation and Synthesis
<div class="publications">
{% bibliography --query @*[keywords ~= topic:data-augmentation-and-synthesis;] --group_by none %}
</div>

## Continual Learning, Plasticity-Stability Trade-off
<div class="publications">
{% bibliography --query @*[keywords ~= topic:continual-learning-plasticity-stability-trade-off;] --group_by none %}
</div>

## Transfer Learning, Multi-task Learning, Meta-Learning
<div class="publications">
{% bibliography --query @*[keywords ~= topic:transfer-learning-multi-task-learning-meta-learning;] --group_by none %}
</div>

## Optimization
<div class="publications">
{% bibliography --query @*[keywords ~= topic:optimization;] --group_by none %}
</div>

## Matrix Factorization and Feature Disentanglement
<div class="publications">
{% bibliography --query @*[keywords ~= topic:matrix-factorization-and-feature-disentanglement;] --group_by none %}
</div>

## Compressed Sensing, Sparse Dimension Reduction
<div class="publications">
{% bibliography --query @*[keywords ~= topic:compressed-sensing-sparse-dimension-reduction;] --group_by none %}
</div>


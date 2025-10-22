---
layout: single
title: "Research"
permalink: /research/
author_profile: false
---

Our research explores how structured light interacts with complex systems, from atomic physics to imaging and optomechanics.  
Below are the five main themes we are currently developing.

---


<div class="research-grid">

{% assign topics = site.pages | where_exp: "page", "page.url contains '/research/'" | reject: "url", "/research/" | sort: "order" %}
{% for topic in topics %}
  {% if topic.thumbnail %}
  <div class="research-card">
    <a href="{{ topic.url | relative_url }}">
      <img src="{{ topic.thumbnail | relative_url }}" alt="{{ topic.title }}">
      <h3>{{ topic.title }}</h3>
      <p>{{ topic.excerpt | default: topic.description }}</p>
    </a>
  </div>
  {% endif %}
{% endfor %}
</div>

<style>
.research-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 1.5rem;
}
.research-card {
  border: 1px solid #ddd;
  border-radius: 10px;
  overflow: hidden;
  background-color: #fff;
  transition: 0.25s ease;
}
.research-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}
.research-card img {
  width: 100%;
  height: 160px;
  object-fit: cover;
}
.research-card h3 {
  margin: 0.6em;
}
.research-card p {
  margin: 0 0.8em 0.8em;
  color: #555;
}
</style>
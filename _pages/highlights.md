---
layout: home
title: "Highlights"
permalink: /highlights/
author_profile: false
---

Our most recent updates, papers, and announcements.

---


<style>
.highlights-list {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.highlight-item {
  display: flex;
  align-items: center; /* ✅ centers image and text vertically */
  gap: 1rem;
  border-bottom: 1px solid #ddd;
  padding-bottom: 1rem;
  padding-top: 0.5rem;
}

.highlight-thumb {
  flex-shrink: 0;
  display: flex;
  align-items: center; /* ✅ centers image inside container */
  justify-content: center;
  height: 120px; /* consistent visual height */
  width: 160px;
}

.highlight-thumb img {
  max-width: 100%;
  max-height: 100%;
  border-radius: 8px;
  object-fit: cover;
}

.highlight-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 3rem;
  color: #888;
  width: 160px;
  height: 120px;
  text-align: center;
}

.highlight-text {
  flex: 1;
}

.highlight-text h3 {
  margin-top: 0;
  margin-bottom: 0.3rem;
}

.highlight-text small {
  color: #666;
  display: block;
  margin-bottom: 0.5rem;
}

.highlight-item:hover {
  background-color: #fafafa;
  border-radius: 8px;
  transition: 0.2s ease;
}

@media (max-width: 700px) {
  .highlight-item {
    flex-direction: column;
    align-items: flex-start;
  }
  .highlight-thumb, .highlight-icon {
    width: 100%;
    height: auto;
    margin-bottom: 0.5rem;
  }
}
</style>

<div class="highlights-list">
{% assign highlights = site.posts | where_exp:"post", "post.categories contains 'highlights'" %}
{% for post in highlights %}
  <div class="highlight-item">
    {% if post.thumbnail %}
      <div class="highlight-thumb">
        <img src="{{ post.thumbnail | relative_url }}" alt="{{ post.title }}">
      </div>
    {% elsif post.icon %}
      <div class="highlight-icon">
        <i class="{{ post.icon }}"></i>
      </div>
    {% endif %}
    <div class="highlight-text">
      <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
      <small>{{ post.date | date: "%B %d, %Y" }}</small>
      <p>{{ post.excerpt | markdownify }}</p>
      <a href="{{ post.url | relative_url }}">Read more →</a>
    </div>
  </div>
{% endfor %}
</div>
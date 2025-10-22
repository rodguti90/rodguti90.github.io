---
layout: single
author_profile: false
title: "Structuring Light's Propagation"
classes: wide
---

<!-- ✅ HERO OVERLAY SECTION -->
<div class="hero-header" style="
  position: relative;
  height: 45vh;
  background: url('/assets/images/bckgd.jpg') center/cover no-repeat;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  text-align: center;
">
  <div style="
    background-color: rgba(0,0,0,0.45);
    padding: 2rem;
    border-radius: 1rem;
    max-width: 800px;
  ">
    <h1 style="font-size: 2.5rem; margin-bottom: 0.5rem;">Structuring Light's Propagation</h1>
    <p style="font-size: 1.2rem; font-weight: 300;">Controlling light–matter interactions by shaping light</p>
  </div>
</div>


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


**Structuring Light's propagation** is an experimental and theoretical group at the LuMIn laboratory at the [Paris-Saclay University](https://www.universite-paris-saclay.fr/), [ENS Paris-Saclay](https://ens-paris-saclay.fr/) and [Centrale Supélec](https://www.centralesupelec.fr/). 
We aim at studying and harnessing structured light for various applications, ranging from controlling its propagation in complex media to developing super-resolution imaging techniques. 
Our work integrates experimental optics, computational methods, and theory to control and understand structured light.
The group is led by Dr. Rodrigo Gutiérrez-Cuevas, an Associate Professor at Paris-Saclay University. 

If you are interested in our work do not hesitate to get in touch via mail at <a href="mailto:rodrigo.gutierrez&#64;ens-paris-saclay.fr">
  rodrigo.gutierrez&#64;ens-paris-saclay.fr
</a>
<!-- [rodrigo.gutierrez@ens-paris-saclay.fr](mailto:rodrigo.gutierrez@ens-paris-saclay.fr) -->

<!-- If you are interested in joining our group do not hesitate to get in touch We are always looking for talented people to join our group, take a look at our open positions -->

<!-- Welcome to the **Structuring Light for Complex Systems** research group, led by Rodrigo Gutiérrez Cuevas.  
We study how structured light interacts with complex optical systems — from adaptive wavefront shaping to photonic disorder and beyond. -->


<!-- 
🧠 **Research themes**
- Wavefront shaping and adaptive optics  
- Light propagation in complex media  
- Computational imaging and optical design   -->

<!-- --- -->

## Recent Highlights

{% assign highlights = site.posts | where_exp:"post", "post.categories contains 'highlights'" | slice: 0, 3 %}
<div class="highlights-list">
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


Visit the [**Highlights page →**](/highlights/) to see all updates.

<style>
/* Make homepage content span full width */
.page__content,
.page,
.page__inner-wrap {
  max-width: 100% !important;
  width: 100% !important;
  padding-left: 0 !important;
  margin-left: 0 !important;
}

/* Remove sidebar space */
.sidebar {
  display: none !important;
}

/* Ensure hero and highlights use full width */
.hero-header {
  width: 100vw;
  margin-left: calc(-50vw + 50%);
}
</style>

<style>
/* Hide page title (e.g., "Structuring Light's Propagation") on homepage */
.page__title {
  display: none !important;
}
</style>

<style>
.hero-header {
  width: 100vw;
  margin-left: calc(-50vw + 50%);
  margin-bottom: 2rem; /* 👈 adds vertical space below the image */
}
</style>
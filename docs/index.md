---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
title: Cacca
titleTemplate: Workflow Framework

hero:
  name: "Cacca"
  text: "Workflow Framework"
  tagline: A workflow framework, easy as shit.

  actions:
    - theme: brand
      text: Documentation
      link: /docs

    - theme: alt
      text: View On GitHub
      link: https://github.com/airscripts/cacca

  image:
    src: https://raw.githubusercontent.com/airscripts/cacca/main/assets/images/logo.png
    alt: Cacca

features:
  - title: Feature A
    details: Lorem ipsum dolor sit amet, consectetur adipiscing elit
  - title: Feature B
    details: Lorem ipsum dolor sit amet, consectetur adipiscing elit
  - title: Feature C
    details: Lorem ipsum dolor sit amet, consectetur adipiscing elit
---
<style>
:root {
  --vp-home-hero-name-color: transparent;
  --vp-home-hero-name-background: -webkit-linear-gradient(120deg, #fcd9c2 30%, #261b00);
  --vp-home-hero-image-background-image: linear-gradient(-45deg, #fcd9c2 50%, #261b00 50%);
  --vp-home-hero-image-filter: blur(40px);
}

@media (min-width: 640px) {
  :root {
    --vp-home-hero-image-filter: blur(56px);
  }
}

@media (min-width: 960px) {
  :root {
    --vp-home-hero-image-filter: blur(72px);
  }
}
</style>

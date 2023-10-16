import { defineConfig } from 'vitepress'

const LOGO = 'https://raw.githubusercontent.com/airscripts/cacca/main/assets/images/logo.png'
const OG_DESCRIPTION = 'A workflow framework, easy as shit.'
const OG_IMAGE = 'https://raw.githubusercontent.com/airscripts/cacca/main/assets/images/og-cover.png'
const OG_TITLE = 'Cacca'
const OG_URL = 'https://cacca.airscript.it'

export default defineConfig({
  lang: 'en-US',
  title: "Cacca",
  description: "Workflow Framework",

  head: [
    ['link', { rel: 'icon', type: 'image/png', href: LOGO }],
    ['meta', { name: 'theme-color', content: '#c8866a' }],
    ['meta', { property: 'og:type', content: 'website' }],
    ['meta', { property: 'og:title', content: OG_TITLE }],
    ['meta', { property: 'og:image', content: OG_IMAGE }],
    ['meta', { property: 'og:url', content: OG_URL }],
    ['meta', { property: 'og:description', content: OG_DESCRIPTION }],
    ['meta', { name: 'twitter:card', content: 'summary_large_image' }],
    ['meta', { name: 'twitter:site', content: '@airscript' }],
  ],

  themeConfig: {
    logo: {
      width: 24,
      height: 24,
      src: LOGO,
    },

    editLink: {
      pattern: 'https://github.com/airscripts/cacca/edit/main/docs/:path',
      text: 'Suggest changes to this page',
    },

    nav: [
      { text: 'Home', link: '/' },
      { text: 'Documentation', link: '/getting-started' }
    ],

    sidebar: [
      {
        text: 'Guide',
        items: [
          { text: 'Getting Started', link: '/getting-started' },
          { text: 'Installation', link: '/installation' },
          { text: 'Hello Toilet', link: '/hello-toilet' }
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/airscripts/cacca' }
    ]
  }
})

import { defineConfig } from 'vitepress'

export default defineConfig({
  lang: 'en-US',
  title: "Cacca",
  description: "Workflow Framework",

  head: [
    ['link', { rel: 'icon', type: 'image/png', href: 'https://raw.githubusercontent.com/airscripts/cacca/main/assets/images/logo.png' }],
  ],

  themeConfig: {
    logo: {
      width: 24,
      height: 24,
      src: 'https://raw.githubusercontent.com/airscripts/cacca/main/assets/images/logo.png',
    },

    nav: [
      { text: 'Home', link: '/' },
      { text: 'Documentation', link: '/docs' }
    ],

    sidebar: [
      {
        text: 'Introduction',
        items: [
          { text: 'Getting Started', link: '/getting-started' },
          { text: 'Installation', link: '/installation' },
          { text: 'Scripting', link: '/scripting' }
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/airscripts/cacca' }
    ]
  }
})

import type { Config } from 'tailwindcss';
import colors from 'tailwindcss/colors'

export default {
  content: ['./src/**/*.{html,js,svelte,ts}', "./node_modules/flowbite/**/*.js"],

  theme: {
    extend: {
      colors: {
        "primary": colors.orange["600"]
      }
    }
  },

  plugins: [
    require('flowbite/plugin')
  ]
} satisfies Config;

module.exports = {
  plugins: [
    require('@tailwindcss/postcss')(),  // ✅ new plugin required by Tailwind v4
    require('autoprefixer'),
  ],
};


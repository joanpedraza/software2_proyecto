module.exports = {
  plugins: {
    'postcss-import': {},
    'postcss-simple-vars': {},
    'postcss-nested': {},
    // Usar cssnano para minificar CSS en producción
    ...(process.env.NODE_ENV === 'production' ? { 'cssnano': {} } : {}),
  },
};

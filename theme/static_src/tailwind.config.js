// tailwind.config.js
module.exports = {
    important: false,
    content: [
        '../templates/**/*.html',
        '../../templates/**/*.html',
        '../../**/templates/**/*.html',
    ],
    theme: {
        screens: {
            sm: '480px',
            md: '768px',
            lg: '1020px',
            xl: '1440px',
        },
        extend: {},
    },
    plugins: [
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
    ],
    purge: {
        content: [
            './templates/**/*.html',
            './static/**/*.js',
        ],
        options: {
            safelist: [],
        },
    },
    // Aquí especifica la ruta donde se deben almacenar los archivos de salida
    output: {
        css: './static/css/dist/styles.css', // Asegúrate de que Tailwind escriba aquí
    },
};

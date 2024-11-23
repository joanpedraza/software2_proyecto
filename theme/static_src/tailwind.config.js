module.exports = {
    important: false,
    content: [
        // Templates dentro de la app theme (<tailwind_app_name>/templates), e.g. base.html
        '../templates/**/*.html',

        // Directorio de templates principales del proyecto (BASE_DIR/templates)
        '../../templates/**/*.html',

        // Templates en otras aplicaciones de Django (BASE_DIR/<app_name>/templates)
        '../../**/templates/**/*.html',

        // JS: Si usas Tailwind CSS en JavaScript
        // '../../**/*.js',

        // Python: Si usas Tailwind CSS en Python
        // '../../**/*.py'
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
    // Asegúrate de purgar las clases no utilizadas en producción
    purge: {
        content: [
            './templates/**/*.html',
            './static/**/*.js',
        ],
        options: {
            safelist: [], // Puedes agregar clases que quieras mantener sin purgar, si es necesario.
        },
    },
};

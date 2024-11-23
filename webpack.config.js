const path = require('path');

const isProduction = process.env.NODE_ENV === 'production';

module.exports = {
  mode: isProduction ? 'production' : 'development', // Modo dinámico
  entry: './frontend/src/index.js', // Asegúrate de que este archivo exista
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'static/frontend'),
    publicPath: '/static/frontend/',
  },
  module: {
    rules: [
      {
        test: /\.scss$/,
        use: ['style-loader', 'css-loader', 'sass-loader'],
      },
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env'],
          },
        },
      },
    ],
  },
  resolve: {
    extensions: ['.js', '.scss'],
  },
  devtool: isProduction ? false : 'source-map',
};

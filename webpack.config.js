const path = require('path');

module.exports = {
  entry: './frontend/src/index.js',
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
  devtool: 'source-map',
};

const path = require("path");

module.exports = {
  entry: "./front_end_assets/index.js",
  output: {
    filename: "index_bundle.js",
    path: path.resolve(__dirname, "./front_end_statics",)
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        loader: "babel-loader",
        options: { presets: ["@babel/preset-env", "@babel/preset-react"]}
      },
    ]
  }
};

const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const { VueLoaderPlugin } = require('vue-loader');
const TerserPlugin = require('terser-webpack-plugin');

module.exports = {
    entry: {
        'site-base': './assets/site-base.js',  // base styles shared between frameworks
        'site-bulma': './assets/site-bulma.js',  // required for bulma styles
        'app': './assets/javascript/vue/main.js',
    },
    output: {
        path: path.resolve(__dirname, './apps/static'),
        filename: 'js/[name]-bundle.js',
        library: ["SiteJS", "[name]"],
    },
    module: {
        rules: [
            {
                test: /\.vue$/,
                loader: 'vue-loader'
            },
            {
                test: /\.(js|jsx)$/,
                exclude: /node_modules/,
                loader: "babel-loader",
                options: { presets: ["@babel/env"] }
            },
            {
                test: /\.scss$/,
                use: [
                    MiniCssExtractPlugin.loader,
                    'css-loader',
                    'sass-loader',
                ],
            },
        ]
    },
    plugins: [
        new MiniCssExtractPlugin({
            'filename': 'css/[name].css',
        }),
        new VueLoaderPlugin(),
    ],
    optimization: {
        minimizer: [new TerserPlugin({
            extractComments: false,  // disable generation of license.txt files
        })],
    },
};

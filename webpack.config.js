'use strict';

const NODE_ENV = process.env.NODE_ENV || 'development';

const path = require('path');
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');

// const NODE_ENV = process.env.NODE_ENV || 'development';

module.exports = {
    entry: './frontend/js/app.js',
    output: {
        path: path.resolve(`./static/bundles`),
        filename: 'app.js'
    },

    watch: NODE_ENV === 'development',

    watchOptions: {
        aggregateTimeout: 100
    },

    plugins: [
        new BundleTracker({filename: './webpack-stats.json'})
    ],

    module: {
        loaders: [
            {
                test: /\.js$/,
                query: {
                    presets: [
                        'es2015',
                        'react'
                    ]
                },
                loader: 'babel-loader',
                exclude: /node_modules/
            }, {
            test: /\.less$/,
                loader: 'style-loader!css-loader!less-loader',
                exclude: /node_modules/
            }, {
            test: /\.css$/,
                loader: 'style-loader!css-loader'
            }
        ]
    }
};


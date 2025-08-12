// from flask import Flask
const express = require('express')

// app = Flask(__name__)
const app = express()

// @app.route('/')
// def index():
    // return "hello, world from flask"
app.get('/', (req, res) => {
    res.send('hello, world from node.js')
})

// app.run()
app.listen(3000, () => {
    console.log("서버가 준비되었음...");
});

// python app.py
// node app.js

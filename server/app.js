/**
 * Module dependencies
 */
const express = require('express'); // Web server
const path = require('path'); // Generating path URIs
const fs = require('fs'); // File-system library

let app = express();

/**
 * Routing
 */
app.get('/images', async function(req, res) {

    let response = {'images': []};
    fs.readdir('images/', (err, files) => {
        if(err) {
            res.sendStatus(500);
            return;
        }

        files.forEach(file => {
            response['images'].push(file);
        });

        res.send(response);
    });
});

app.get('/images/:fileName', function(req, res) {

    let filePath = path.resolve('images/' + req.params.fileName);
    if (fs.existsSync(filePath)) {
        res.sendFile(filePath);
    } else {
        res.sendStatus(404);
    }
});

module.exports = app;
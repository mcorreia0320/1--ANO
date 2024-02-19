const express = require('express');
const fs = require('fs');
const app = express();
const port = 3000;

app.use(express.json());

function writeLog(req, res, next) {
    var log = req.url + ", " + req.method + ", " + new Date().toString() + "\n";
    fs.appendFileSync("log.txt", log);
    next();
}

app.use(writeLog);

fs.appendFileSync("log.txt", "SERVER STARTED \n");

app.get('/', (req, res) => {
    const body = "Hello World";
    res.writeHead(200, {
        'content-Length': Buffer.byteLength(body),
        'content-Type': 'text/plain'
    });
    res.end(body);
});

app.get('/html', (req, res) => {
    const html = "<h1> Hello World </h1>";
    res.writeHead(200, {
        'content-Length': Buffer.byteLength(html),
        'content-Type': 'text/html'
    });
    res.end(html);
});

app.get('/html2', (req, res) => {
    var date = new Date();
    var name = 'Miguel';
    var html2 = fs.readFileSync("./index.html", "utf-8")
    html2 = html2.replace("{name}", name);
    html2 = html2.replace("{date}", date.toDateString());
    res.writeHead(200, {
        'content-Length': Buffer.byteLength(html2),
        'content-Type': 'text/html'
    });
    res.end(html2);
});

app.get('/html/:name', (req, res) => {
    var date = new Date();
    var name = req.params.name;
    var body = fs.readFileSync("./index.html", "utf-8");
    body = body.replace("{name}", name);
    body = body.replace("{date}", date.toDateString());
    res.writeHead(200, {
        'content-Length': Buffer.byteLength(body),
        'content-Type': 'text/html'
    });
    res.end(body);
});

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`);
});

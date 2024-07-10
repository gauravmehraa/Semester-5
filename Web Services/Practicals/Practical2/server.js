"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var http_1 = require("http");
var hostname = 'localhost';
var port = 3000;
var server = (0, http_1.createServer)(function (req, res) {
    res.setHeader('Content-Type', 'text/plain');
    if (req.method === 'GET') {
        collectData(req, function (body) {
            res.statusCode = 200;
            if (req.url === '/add')
                res.end("".concat(body.num1 + body.num2));
            else if (req.url === '/subtract')
                res.end("".concat(body.num1 - body.num2));
            else if (req.url === '/multiply')
                res.end("".concat(body.num1 * body.num2));
            else if (req.url === '/divide')
                res.end("".concat(body.num1 / body.num2));
            else {
                res.statusCode = 404;
                res.end('Page not found!');
            }
        });
    }
    else {
        res.statusCode = 404;
        res.end('Page not found!');
    }
});
function collectData(request, callback) {
    if (request.headers['content-type'] === 'text/plain') {
        var body_1 = '';
        request.on('data', function (chunk) {
            body_1 += chunk.toString();
        });
        request.on('end', function () {
            callback(JSON.parse(body_1));
        });
    }
    else
        callback(null);
}
server.listen(port, hostname, function () {
    console.log("Server listening on port ".concat(port));
});

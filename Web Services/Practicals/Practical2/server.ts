import { createServer, IncomingMessage, Server, ServerResponse } from "http";

const hostname: string = 'localhost';
const port: number = 3000;

const server: Server = createServer((req: IncomingMessage, res: ServerResponse) => {
    res.setHeader('Content-Type', 'text/plain');
    if(req.method === 'GET'){
        collectData(req, (body: any) => {
            res.statusCode = 200;
            if(req.url === '/add') res.end(`${body.num1 + body.num2}`);
            else if(req.url === '/subtract') res.end(`${body.num1 - body.num2}`);
            else if(req.url === '/multiply') res.end(`${body.num1 * body.num2}`);
            else if(req.url === '/divide') res.end(`${body.num1 / body.num2}`);
            else{
                res.statusCode = 404;
                res.end('Page not found!');
            }
        });
    }
    else{
        res.statusCode = 404;
        res.end('Page not found!');
    }
});

function collectData(request: IncomingMessage, callback: CallableFunction) {
    if(request.headers['content-type'] === 'text/plain') {
        let body = '';
        request.on('data', chunk => {
            body += chunk.toString();
        });
        request.on('end', () => {
            callback(JSON.parse(body));
        });
    }
    else callback(null);
}

server.listen(port, hostname, () => {
    console.log(`Server listening on port ${port}`);
});
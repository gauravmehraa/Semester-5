import fs from "fs"
import http from "http";

const readFile = () => {
  const rawdata = fs.readFileSync("users.json", "utf-8");
  const data = JSON.parse(rawdata);
  return data;
}
const writeFile = (data) => {
  fs.writeFileSync("users.json", JSON.stringify(data), "utf-8")
}

const hostname = "localhost"
const port = 3000

const server = http.createServer((req, res) => {
  res.setHeader('Content-Type', 'text/plain');
  if(req.method === 'GET'){
    getData(req , (body) => {
      res.statusCode = 200;
      if(req.url === '/') res.end(`Hello ${body.name}`);
      else{
        res.statusCode = 400;
        res.end('not found');
      }
    });
  }
});

function getData(request, callback) {
  if(request.headers['content-type'] === 'text/plain'){
    let body = '';
    request.on('data', (chunk) => body += chunk.toString());
    request.on('end', () => callback(JSON.parse(body)));
  }
  else callback(null);
}

server.listen(port, hostname, ()=> {
  console.log("server up");
})
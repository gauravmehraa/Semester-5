import express, { Express, Request, Response } from "express";

const app: Express = express();
app.use(express.json());

const users = [{ name: "Gaurav Mehra", password: "password" }];

app.get('/', (req: Request, res: Response) => {
  return res.status(200).json(users);
});

app.post('/add', (req: Request, res: Response) => {
  const { name, password } = req.body;
  users.push({ name, password })
  return res.status(201).json(`User ${name} successfully added`);
});

app.listen(3000, ()=> {
  console.log("Server Up");
})
import express, { Express } from "express"
import { connectToDB } from "./connect";
import dotenv from "dotenv"

import userRoutes from "./routes";

dotenv.config();
const port = process.env.PORT;

const app: Express = express();
app.use(express.json());

app.use("/api/users", userRoutes);

app.listen(port, () => {
  connectToDB();
  console.log(`Server listening on port ${port}`);
})
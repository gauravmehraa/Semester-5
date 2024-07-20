import express, { Express } from "express";
import authRoutes from "./routes/auth.routes";
import todoRoutes from "./routes/todo.routes";

const app: Express = express();
app.use(express.json());

app.use("/auth", authRoutes);
app.use("/todo", todoRoutes);

app.listen(3000, () => {
  console.log("Server Running...");
})
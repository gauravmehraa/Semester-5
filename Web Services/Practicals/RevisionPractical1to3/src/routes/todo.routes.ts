import express, { Router } from "express";
import { getToDos, addToDo, editToDo, deleteToDo } from "../controllers/todo.controller";

const router: Router = express.Router();

router.get("/", getToDos);
router.post("/add", addToDo);
router.patch("/edit/:id", editToDo);
router.delete("/delete/:id", deleteToDo);

export default router;
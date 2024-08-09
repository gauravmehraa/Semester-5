import { Router } from "express";
import { addUser, deleteUser, editUser, getUsers } from "./controller";

const router: Router = Router();

router.get("/", getUsers);

router.post("/add", addUser);

router.patch("/edit/:id", editUser);

router.delete("/delete/:id", deleteUser);

export default router;
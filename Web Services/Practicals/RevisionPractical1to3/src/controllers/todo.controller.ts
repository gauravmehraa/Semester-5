import { Request, Response } from "express"
import { readFile, writeFile } from "../utils/file";
import { Log, ToDo } from "../types/custom";
import { verifyHash } from "../middleware/verify";

export const getToDos = async(req: Request, res: Response) => {
  try{
    const { username } = req.body;
    const todos: Array<ToDo> = readFile('todo');
    const filteredTodos: Array<ToDo> = todos.filter((todo: ToDo) => { return todo.username === username });

    const logs: Array<Log> = readFile('logs');
    logs.push({
      action: 'TODO',
      message: `${username} retrieved ToDos`,
      timestamp: new Date()
    });
    writeFile(logs, 'logs');

    res.status(200).json(filteredTodos);
  }
  catch(error){
    console.log("Error in get ToDos: ", (error as Error).message);
    res.status(500).json({error: "Internal Server Error"});
  }
}

export const addToDo = async(req: Request, res: Response) => {
  try{
    const { username, id, content } = req.body;

    if(!verifyHash(username)){
      res.status(403).json( {error: "Hash expired. Login again" })
      return;
    }

    const todos: Array<ToDo> = readFile('todo');

    const todo: Array<ToDo> = todos.filter((todo: ToDo) => { return (todo.id === parseInt(id) && todo.username === username) }); // check for duplicate usernames

    if(todo.length !== 0){
      res.status(400).json({ error: "ID already exists"});
      return;
    }

    todos.push({
      username,
      id: parseInt(id),
      content,
      created: new Date()
    })
    writeFile(todos, 'todo');

    const logs: Array<Log> = readFile('logs');
    logs.push({
      action: 'TODO',
      message: `${username} added ToDo #${id}`,
      timestamp: new Date()
    });
    writeFile(logs, 'logs');

    res.status(200).json({ message: "ToDo Successfully added" });
  }
  catch(error){
    console.log("Error in add ToDo: ", (error as Error).message);
    res.status(500).json({error: "Internal Server Error"});
  }
}

export const editToDo = async(req: Request, res: Response) => {
  try{
    const { id } = req.params;
    const { username, content } = req.body;

    if(!verifyHash(username)){
      res.status(403).json( {error: "Hash expired. Login again" })
      return;
    }

    const todos: Array<ToDo> = readFile('todo');

    const updatedTodos = todos.map((todo: ToDo) => {
      return (todo.id === parseInt(id) && todo.username === username ) ?
      {
          ...todo,
          content
      }
      :
      todo
    });
    writeFile(updatedTodos, 'todo');

    const logs: Array<Log> = readFile('logs');
    logs.push({
      action: 'TODO',
      message: `${username} edited ToDo #${id}`,
      timestamp: new Date()
    });
    writeFile(logs, 'logs');

    res.status(200).json({ message: "ToDo Successfully edited" });
  }
  catch(error){
    console.log("Error in edit ToDo: ", (error as Error).message);
    res.status(500).json({error: "Internal Server Error"});
  }
}

export const deleteToDo = async(req: Request, res: Response) => {
  try{
    const { id } = req.params;
    const { username } = req.body;

    if(!verifyHash(username)){
      res.status(403).json( {error: "Hash expired. Login again" })
      return;
    }

    const todos = readFile('todo');
    const updatedTodos = todos.filter((todo: ToDo) => { return (todo.id !== parseInt(id) && todo.username !== username) });
    writeFile(updatedTodos, 'todo');
    res.status(200).json({ message: "ToDo Successfully deleted" });
  }
  catch(error){
    console.log("Error in delete ToDo: ", (error as Error).message);
    res.status(500).json({error: "Internal Server Error"});
  }
}
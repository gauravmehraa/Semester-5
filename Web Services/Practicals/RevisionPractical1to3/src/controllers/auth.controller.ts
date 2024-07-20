import { Request, Response } from "express"
import { readFile, writeFile } from "../utils/file";
import { Log, User } from "../types/custom";
import { generateHash } from "../utils/hash";

export const signup = async(req: Request, res: Response) => {
  try{
    const { username, name, password } = req.body;
    const users: Array<User> = readFile('users'); // get all users
    const user: Array<User> = users.filter((user: User) => { return (user.username === username) }); // check for duplicate usernames

    if(user.length !== 0){
      res.status(400).json({ error: "Username already exists"});
      return;
    }

    users.push({ username, password, name });
    writeFile(users, 'users');

    const logs: Array<Log> = readFile('logs');
    logs.push({
      action: 'SIGNUP',
      message: `${username} registered successfully`,
      timestamp: new Date()
    });
    writeFile(logs, 'logs');

    res.status(201).json({ message: "User successfully registered"})
  }
  catch(error){
    console.log("Error in signup user: ", (error as Error).message);
    res.status(500).json({error: "Internal Server Error"});
  }
}

export const login = async(req: Request, res: Response) => {
  try{
    const { username, password } = req.body;

    const users: Array<User> = readFile('users'); // get all users
    const user: Array<User> = users.filter((user: User) => { return (user.username === username && user.password === password) }); // check for duplicate usernames

    const logs: Array<Log> = readFile('logs');

    if(user.length === 0){
      res.status(400).json({ error: "Wrong username and password" });
      logs.push({
        action: 'LOGIN',
        message: `${username} tried to login`,
        timestamp: new Date()
      });
    }
    else{
      logs.push({
        action: 'LOGIN',
        message: `${username} logged in successfully`,
        timestamp: new Date()
      });
      generateHash(username);
      logs.push({
        action: 'HASH',
        message: `${username} generated new hash`,
        timestamp: new Date()
      });
      res.status(201).json({ message: "User successfully logged in"})
    }
    writeFile(logs, 'logs');
  }
  catch(error){
    console.log("Error in login user: ", (error as Error).message);
    res.status(500).json({error: "Internal Server Error"});
  }
}

export const logout = async(req: Request, res: Response) => {
  try{

  }
  catch(error){
    console.log("Error in logout user: ", (error as Error).message);
    res.status(500).json({error: "Internal Server Error"});
  }
}
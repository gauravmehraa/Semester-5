import { Request, Response } from "express";
import User from "./model";

export const getUsers = async(req: Request, res: Response) => {
  try{
    const users = await User.find().select("-password");
    res.status(200).json(users);
  }
  catch (error) {
    console.log(`[ERROR] - Get Users Controller: ${(error as Error).message}`);
    res.status(500).json({ error: "Internal Server Error" });
  }
}

export const addUser = async(req: Request, res: Response) => {
  try{
    const { username, name, password } = req.body;

    const existingUser = await User.findOne({ username: { $eq: username }});
    if(existingUser){
      res.status(400).json({error: "Username is already taken"});
      return;
    }

    const newUser = new User({username, name, password});
    if(newUser){
      await newUser.save();
      res.status(201).json({
        _id: newUser._id,
        username: newUser.username,
        name: newUser.name
      });
    }
    else{
      res.status(400).json({ error: "Invalid data" });
    }
  }
  catch (error) {
    console.log(`[ERROR] - Add User Controller: ${(error as Error).message}`);
    res.status(500).json({ error: "Internal Server Error" });
  }
}

export const editUser = async(req: Request, res: Response) => {
  try{
    const { id } = req.params;
    const { username, name, password } = req.body;

    const user = await User.findById(id);
    if(!user){
      res.status(400).json({error: "User does not exist"});
      return;
    }

    const existingUser = await User.findOne({ username: { $eq: username }});
    if(existingUser){
      res.status(400).json({error: "Username is already taken"});
      return;
    }

    const newUser = await User.findByIdAndUpdate(
      id,
      {username, name, password},
      { new: true}
    );

    if(newUser){
      await newUser.save();
      res.status(201).json({
        _id: newUser._id,
        username: newUser.username,
        name: newUser.name
      });
    }
    else{
      res.status(400).json({ error: "Invalid data" });
    }
  }
  catch (error) {
    console.log(`[ERROR] - Edit User Controller: ${(error as Error).message}`);
    res.status(500).json({ error: "Internal Server Error" });
  }
}

export const deleteUser = async(req: Request, res: Response) => {
  try{
    const { id } = req.params;
    const user = await User.findById(id);
    if(!user){
      res.status(400).json({error: "User does not exist"});
      return;
    }
    await user.deleteOne();
    res.status(200).json({ message: "User successfully deleted" });
  }
  catch (error) {
    console.log(`[ERROR] - Delete User Controller: ${(error as Error).message}`);
    res.status(500).json({ error: "Internal Server Error" });
  }
}
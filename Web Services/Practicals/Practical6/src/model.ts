import { model, Schema, Types } from "mongoose";

interface IUser {
  _id: Types.ObjectId;
  username: string;
  name: string;
  password: string;
}

const userSchema = new Schema({
  username: {
    type: String,
    minlength: 4,
    unique: true,
    required: true
  },
  name: {
    type: String,
    required: true
  },
  password: {
    type: String,
    minlength: 6,
    required: true
  },
});

const User = model("User", userSchema);

export { IUser, User };
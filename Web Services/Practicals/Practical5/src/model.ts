import { model, Schema } from "mongoose";

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

export default User;
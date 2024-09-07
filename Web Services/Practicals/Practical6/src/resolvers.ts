import { User } from "./model";

const resolvers = {
  Query: {
    users: async() => await User.find(),
    user: async(_: any, params: { username: string }) => await User.findOne({ username: params.username }),
  },
  Mutation: {
    register: async(_: any, params: { name: string, username: string, password: string }) => {
      const user = new User({ name: params.name, username: params.username, password: params.password });
      if(user) await user.save();
      return user;
    },
    update: async(_: any, params: { username:string, password: string }) =>
        await User.findOneAndUpdate(
        { username: params.username },
        { password: params.password },
        { new: true }
      )
  }
};

export default resolvers;
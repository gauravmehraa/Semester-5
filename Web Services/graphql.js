import fs from "fs"
import { ApolloServer, gql } from "apollo-server-express";
import express from "express"

const readFile = () => {
  const rawdata = fs.readFileSync("users.json", "utf-8");
  const data = JSON.parse(rawdata);
  return data;
}
const writeFile = (data) => {
  fs.writeFileSync("users.json", JSON.stringify(data), "utf-8")
}

const schema = gql`
  type User { 
    name: String
    age: Int
  }

  type Query {
    getUsers: [User]
  }

  type Mutation { 
    register(name: String!, age: Int!): User
  }
`;

const resolvers = {
  Query: {
    getUsers: () => {
      const data = readFile();
      return data;
    }
  },
  Mutation: {
    register: (_, params) => {
      const data = readFile();
      data.push(params);
      writeFile(data);
      return params;
    }
  }
}

async function start(){
  const server = new ApolloServer({ typeDefs: schema, resolvers });
  await server.start();
  const app = express();
  server.applyMiddleware( {app} );
  app.listen(3000, () => {
    console.log("Server up")
  })
}

start()
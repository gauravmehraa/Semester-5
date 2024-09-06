import express from 'express';
import { ApolloServer } from 'apollo-server-express';
import dotenv from "dotenv";

import schema from "./schema";
import resolvers from "./resolvers";
import { connectToDB } from './connect';

dotenv.config();
const port = process.env.PORT || 3500;

async function start(){
  const server = new ApolloServer({ typeDefs: schema, resolvers });
  await server.start();
  const app: any = express();
  server.applyMiddleware({ app });
  app.listen({ port }, () => {
    connectToDB();
    console.log(`Server ready at http://localhost:${port}${server.graphqlPath}`);
  })
}

start();
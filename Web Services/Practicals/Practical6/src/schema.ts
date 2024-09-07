import { gql } from "apollo-server-express";

const schema = gql`
  type User {
    _id: String
    username: String
    name: String
    password: String
  }
  
  input UserInput {
    username: String
    name: String
    password: String
  }

  type Query {
    users: [User]
    user(username: String!): User
  }

  type Mutation {
    register(name: String!, username: String!, password: String!): User,
    update(username: String!, password: String!): User
  }
`;

export default schema;
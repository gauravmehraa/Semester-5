export interface User {
  username: string;
  name: string;
  password: string;
}

export interface Log {
  action: string;
  message: string;
  timestamp: Date;
}

export interface ToDo {
  username: string;
  id: number;
  content: string;
  created: Date;
}
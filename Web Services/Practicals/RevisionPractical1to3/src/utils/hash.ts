import { readFile, writeFile } from "./file"

export const generateHash = (username: string) => {
  const hashes = readFile('userhash');
  const now = new Date();
  hashes[username] = {
    hash: "hello world",
    expiry: new Date(now.getTime() + 5*60000)
  }
  writeFile(hashes, 'userhash');
}
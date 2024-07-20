import { readFile, writeFile } from "../utils/file"

export const verifyHash = (username: string) => {
  
  const hashes = readFile('userhash');
  const logs = readFile('logs');

  const user = hashes[username];

  let isVerified = false;
  let message = '';

  if(!user){
    message = "failed hash verification";
  }
  else if(new Date(user.expiry).getTime() <= new Date().getTime()){
    message = "hash expired";
  }
  else{
    message = "hash verified";
    isVerified = true;
  }

  logs.push({
    action: 'HASH',
    message: `${username} ${message}`,
    timestamp: new Date()
  });
  writeFile(logs, 'logs');

  return isVerified;
}
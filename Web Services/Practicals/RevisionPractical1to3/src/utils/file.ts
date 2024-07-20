import path from "path";
import fs from "fs";

export const readFile = (fileName: string) => {
  const filePath: string = path.join(process.cwd(), `src/data/${fileName}.json`);
  const jsonData: string = fs.readFileSync(filePath, 'utf-8');
  const data = JSON.parse(jsonData);
  return data;
}

export const writeFile = (data: any, fileName: string) => {
  const filePath: string = path.join(process.cwd(), `src/data/${fileName}.json`);
  fs.writeFileSync(filePath, JSON.stringify(data), "utf-8");
}
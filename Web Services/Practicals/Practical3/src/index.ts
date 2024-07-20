import express, { Express, Request, Response } from "express";
import fs from "fs";
import path from "path";

const app: Express = express();
app.use(express.json());

interface User {
    id: number;
    name: string;
    age: number;
    course: string;
    address: string;
}

app.get('/', (req: Request, res: Response) => {
    try{
        const data: Array<User> = readFile();
        res.status(200).json(data);
    }
    catch(error){
        console.log("Error in get users: ", (error as Error).message);
        res.status(500).json({error: "Internal Server Error"});
    }
});

app.post('/add', (req: Request, res: Response) => {
    try{
        const { id, name, age, course, address }: User = req.body;
        if(!id || !name || !age || !course || !address){
            throw new Error("Invalid data");
        }
        const data = readFile();
        data.push({ id, name, age, course, address });
        writeFile(data);
        res.status(201).json({message: "User created"});
    }
    catch(error){
        console.log("Error in add user: ", (error as Error).message);
        res.status(500).json({error: "Internal Server Error"});
    }
});

app.patch('/update/:id', (req: Request, res: Response) => {
    try{
        const { id } = req.params;
        const { name, age, course, address }: User = req.body;
        const data = readFile();
        const updatedData = data.map((user: User) => {
            return (user.id === parseInt(id)) ?
            {
                ...user,
                name: name? name: user.name,
                age: age? age: user.age,
                course: course? course: user.course,
                address: address? address: user.address
            }
            :
            user
        });
        writeFile(updatedData);
        res.status(200).json({message: "User updated"});
    }
    catch(error){
        console.log("Error in update user: ", (error as Error).message);
        res.status(500).json({error: "Internal Server Error"});
    }
});

app.delete('/delete/:id', (req: Request, res: Response) => {
    try{
        const { id } = req.params;
        const data = readFile();
        const updatedData = data.filter((user: User) => { return (user.id !== parseInt(id)) });
        writeFile(updatedData);
        res.status(200).json({message: "User deleted"});
    }
    catch(error){
        console.log("Error in delete user: ", (error as Error).message);
        res.status(500).json({error: "Internal Server Error"});
    }
});

const readFile = (): Array<User> => {
    const filePath: string = path.join(process.cwd(), 'src/users.json');
    const jsonData: string = fs.readFileSync(filePath, 'utf8');
    const data: Array<User> = JSON.parse(jsonData);
    return data;
}

const writeFile = (data: Array<User>): void => {
    const filePath: string = path.join(process.cwd(), 'src/users.json');
    fs.writeFileSync(filePath, JSON.stringify(data), "utf-8");
}

app.listen(3000, () => {
    console.log('Server Up');
});
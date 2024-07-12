"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const express_1 = __importDefault(require("express"));
const fs_1 = __importDefault(require("fs"));
const path_1 = __importDefault(require("path"));
const app = (0, express_1.default)();
app.use(express_1.default.json());
app.get('/', (req, res) => {
    try {
        const data = readFile();
        res.status(200).json(data);
    }
    catch (error) {
        console.log("Error in get users: ", error.message);
        res.status(500).json({ error: "Internal Server Error" });
    }
});
app.post('/add', (req, res) => {
    try {
        const { id, name, age, course, address } = req.body;
        if (!id || !name || !age || !course || !address) {
            throw new Error("Invalid data");
        }
        const data = readFile();
        data.push({ id, name, age, course, address });
        writeFile(data);
        res.status(201).json({ message: "User created" });
    }
    catch (error) {
        console.log("Error in add user: ", error.message);
        res.status(500).json({ error: "Internal Server Error" });
    }
});
app.patch('/update/:id', (req, res) => {
    try {
        const { id } = req.params;
        const { name, age, course, address } = req.body;
        const data = readFile();
        const updatedData = data.map((user) => {
            return (user.id === parseInt(id)) ? Object.assign(Object.assign({}, user), { name: name ? name : user.name, age: age ? age : user.age, course: course ? course : user.course, address: address ? address : user.address }) :
                user;
        });
        writeFile(updatedData);
        res.status(200).json({ message: "User updated" });
    }
    catch (error) {
        console.log("Error in update user: ", error.message);
        res.status(500).json({ error: "Internal Server Error" });
    }
});
app.delete('/delete/:id', (req, res) => {
    try {
        const { id } = req.params;
        const data = readFile();
        const updatedData = data.filter((user) => { return (user.id !== parseInt(id)); });
        writeFile(updatedData);
        res.status(200).json({ message: "User deleted" });
    }
    catch (error) {
        console.log("Error in delete user: ", error.message);
        res.status(500).json({ error: "Internal Server Error" });
    }
});
const readFile = () => {
    const filePath = path_1.default.join(process.cwd(), 'src/users.json');
    const jsonData = fs_1.default.readFileSync(filePath, 'utf8');
    const data = JSON.parse(jsonData);
    return data;
};
const writeFile = (data) => {
    const filePath = path_1.default.join(process.cwd(), 'src/users.json');
    fs_1.default.writeFileSync(filePath, JSON.stringify(data), "utf-8");
};
app.listen(3000, () => {
    console.log('Server Up');
});

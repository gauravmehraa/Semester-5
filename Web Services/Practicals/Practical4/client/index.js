const getUsers = async() => {
  const response = await fetch('http://localhost:3000/')
  const data = await response.json();
  data.forEach(element => {
    console.log();
    for (const key in element){
      console.log(`${capitalize(key)}: ${element[key]}`);
    }
  });
}

const addUser = async() => {
  const name = "New User";
  const password = "password123";
  const newUser = { name, password };
  const response = await fetch('http://localhost:3000/add', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(newUser)
  });
  console.log(await response.json());
}

const main = () => {
  const choice = '1';
  if(choice === '1') getUsers();
  else if(choice === '2') addUser();
}

function capitalize(str) {
  return str.charAt(0).toUpperCase() + str.slice(1);
}

main();
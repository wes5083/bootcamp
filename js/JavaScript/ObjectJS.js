info={
    "name":"Wes",
    "age":18
}

info={
    name:"Wes",
    age:18
}

console.log(info);


info.age = 20;
info.name = "Jime"
console.log(info);



info["age"] = 30
info["name"] = "Mandy"
console.log(info);

for(var key in info){
    console.log(key + ":" + info[key])
}
var array1 = [11,22,33,44];
var array2= Array([11,22,33,44]);
console.log(array1)     //[ 11, 22, 33, 44 ]

array1.push("55");
console.log(array1)     //[ 11, 22, 33, 44, '55' ]

array1.unshift("55")    //[ '55', 11, 22, 33, 44, '55' ]
console.log(array1)

array1.splice(1,0,"999")    //[ '55', '999', 11, 22,   33,    44, '55' ]
console.log(array1)

array1.pop()    //[ '55', '999', 11, 22, 33, 44 ]
console.log(array1)

array1.shift()  //[ '999', 11, 22, 33, 44 ]
console.log(array1)

array1.splice(2,1)  //[ '999', 11, 33, 44 ]
console.log(array1)

for(var index in array1){
    console.log(array1[index])
}
for(var i=0; i<array1.length; i++){
    console.log(array1[i])
}










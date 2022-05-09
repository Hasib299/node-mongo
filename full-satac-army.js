const arr =[
  {id:1,value:'hasib'},
  {id:2,value:'shakil'},
  {id:3,value:'mamun'},
  {id:4,value:'wadud'},
  {id:5,value:'soroar'}
]

// let index = arr.findIndex(item => item.id===4)
// let arr2 = arr.splice(index,1)
// console.log(index);
// console.log(arr);
 
let filteredArr =   arr.filter(item => item.id !== 4)

console.log(filteredArr);
console.log(arr);
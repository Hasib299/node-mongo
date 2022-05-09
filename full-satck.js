const arr =  ['hasib',4,'6',5,85,null,65,85,false,true,undefined,]

let count = 0;
 for(let i = 0;i < arr.length;i++){
   if(typeof arr[i]!='number'){
       console.log(arr[i],'is not a number!');
   }else{
       arr[i] = arr[i-1]
       console.log(arr[i]);
   }
 }
 
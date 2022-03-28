const express = require("express");
const os = require('os')

const app = express()

app.get('/', (req,res,next) =>{
    res.send(os.platform())
})

app.listen(3000, () =>{
    console.log('server is running on port 3000!!');
})



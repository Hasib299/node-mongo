const express = require("express");
const os = require('os')

const app = express()

let nam

app.get('/:name', (req,res,next) =>{
    res.send(os.userInfo().username + ''+ req.params.name)
})

app.listen(3000, () =>{
    console.log('server is running on port 3000!!');
})



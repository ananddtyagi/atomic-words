const express = require("express");
const { spawn } = require("child_process");
require("node-pandas");
const app = express();
const port = 3000;
const cors = require("cors");

app.use(cors({}));

app.get("/:word", (req, res) => {
  var dataToSend;
  // spawn new child process to call the python script
  const python = spawn("python3", ["script.py", req.params.word]);
  // collect data from script

  python.stdout.on("data", function (data) {
    console.log("Pipe data from python script ...");
    dataToSend = JSON.parse(data.toString());
    console.log(data.toString());
  });

  python.stderr.on("data", (data) => {
    console.error(data.toString());
  });
  // in close event we are sure that stream from child process is closed
  python.on("close", (code) => {
    console.log(`child process close all stdio with code ${code}`);
    // send data to browser
    res.send(dataToSend);
  });
});
app.listen(port, () =>
  console.log(`Example app listening on port 
 ${port}!`)
);

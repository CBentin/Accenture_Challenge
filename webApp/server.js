let AWS = require('aws-sdk');
let express = require("express");
let morgan = require("morgan");
let bodyParser = require("body-parser");
require('dotenv').config();
let s3 = new AWS.S3();



app = express();
let jsonParser = bodyParser.json();
app.use(morgan("dev"));
app.use(express.static('public'));
app.use(bodyParser.urlencoded({
    extended: true
  }));
app.use(function(req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Methods", "GET, PUT, POST, DELETE");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
});

app.get("/getFrame", jsonParser,(req, res) =>{
    let count = req.query.count
    let keyName = "Frame_" + count.toString();
    let image;
    let plate;
    params = {Bucket: 'christian.accenture.challenge', Key: keyName};
    s3.getObject(params, function(err, data){
        image = data.Body.toString('base64');
        console.log(image);
        plate = data.Metadata.plate;
        return res.status(200).json({image:image,plate:plate});
    });
});

app.listen("8080", () => {
    console.log("App is running on port 8080");
});
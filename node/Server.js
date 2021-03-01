var fs = require("fs");
var http = require("http");
var os = require("os");
var ip = require("ip");
function secondsToDhms(seconds) {
    seconds = Number(seconds);
    var d = Math.floor(seconds / (3600*24));
    var h = Math.floor(seconds % (3600*24) / 3600);
    var m = Math.floor(seconds % 3600 / 60);
    var s = Math.floor(seconds % 60);
    var newTime = [d,h,m,s];
    return newTime;
    };

var server = http.createServer(function(req, res) {
    if (req.url === "/") {
        fs.readFile("./public/index.html", "UTF-8", function(err, body){
            res.writeHead(200, {"Content-Type": "text/html"});
            res.end(body);
        })
    }

    else if(req.url.match("/sysinfo")) {
        var newTime = secondsToDhms(os.uptime());
        var strNewTime = `Days: ${newTime[0]}, Hours: ${newTime[1]}, Minutes: ${newTime[2]}, Seconds: ${newTime[3]}`;
        myHostName=os.hostname();
        totalMemory=os.totalmem();
        freeMemory=os.freemem();
        myCpus=os.cpus();
        html=`
        <!DOCTYPE html>
        <head>
            <title>Node JS Response</title>
        </head>
        <body>
            <p>Hostname: ${myHostName}</p>
            <p>IP: ${ip.address()}</p>
            <p>Server Uptime: ${strNewTime}</p>
            <p>Total Memory: ${totalMemory/1000000} MB</p>
            <p>Free Memory: ${freeMemory/1000000} MB</p>
            <p>Number of CPU's: ${myCpus.length} </p>
        </body>
        </html>
        `
        res.writeHead(200, {"Contenty-Type" : "text/html"});
        res.end(html);
    }

    else{
        res.writeHead(404, {"Content-Type": "text/plain"});
        res.end(`404 File not found at ${req.url}`);
    }

});

server.listen(3000);
console.log("Server listening on port 3000");
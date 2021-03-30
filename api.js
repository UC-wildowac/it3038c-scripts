var http = require("http");
var data = require("./public/widgets.json")

var server = http.createServer(function(req, res) {
    if (req.url === "/") {
        res.writeHead(200, {"Content-Type": "text/json"});
           res.end(body);
    }

    else{
        res.writeHead(404, {"Content-Type": "text/plain"});
        res.end(`Data not found`);
    }

});

server.listen(3000);
console.log("Server listening on port 3000");
var request = require('request');

class Requester{
    constructor(address){
        this.options = address;
    }

    doRequest(cb){
        request(this.options, function(error, response, body){
            if(error){
                console.log(error);
                cb("Sorry, cannot answer that.");
            }
            var resp = JSON.parse(body);
            console.log(resp);
            cb(resp.response);
        })
    }
}

module.exports = Requester;
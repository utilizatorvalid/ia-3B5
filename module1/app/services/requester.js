var request = require('request');

class Requester{
    constructor(address, portulet, pathulet){
        this.options = {
            hostname: address,
            port: portulet,
            path: pathulet,
            method: "GET",
            json: true
        };
    }

    doRequest(cb){
        request(options, function(error, response, body){
            if(error)
                console.log(error);
            cb(body);
        })
    }
}

module.exports = Requester;
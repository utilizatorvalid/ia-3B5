var Requester = require("./requester.js");
const AnswerBot = require("./data.js");
const answerBot = new AnswerBot()
const baseAddress = 'https://3668928a.ngrok.io';
class BotCore{

  handle_message(input_message, cb){
    var requester = new Requester(baseAddress + '?question=' + input_message);
    requester.doRequest(cb);
    //cb("DA");
  }
  
}

module.exports = BotCore
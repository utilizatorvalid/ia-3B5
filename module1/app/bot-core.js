var Requester = require("./requester.js");
const AnswerBot = require("./data.js");
const answerBot = new AnswerBot()
const baseM2Address = 'https://3668928a.ngrok.io';
class BotCore{

  handle_message(input_message, cb){
    var m2requester = new Requester(baseM2Address + '?question=' + input_message);
    m2requester.doRequest(true, function(text){
      cb(text);
    });
    //cb("DA");
  }
  
}

module.exports = BotCore
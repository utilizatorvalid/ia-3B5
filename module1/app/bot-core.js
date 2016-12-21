var Requester = require("./services/requester")
const AnswerBot = require("./data.js");
const answerBot = new AnswerBot()

class BotCore{

  handle_message(input_message, cb){
    var requester = new Requester('http://localhost', '8099', input_message);
    requester.doRequest(cb);
  }
  
}

module.exports = BotCore;
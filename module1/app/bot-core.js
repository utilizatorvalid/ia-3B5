const AnswerBot = require("./data.js");
const answerBot = new AnswerBot()
class BotCore{

  handle_message(input_message){

    return answerBot.handleMessage(input_message);
  }
  
}

module.exports = BotCore
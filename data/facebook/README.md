# Facebook Data
Both the raw (`raw/`) and preprocessed message data (`clean/`) used to finetune the language model reside in this folder. 

**Note:** The message data is not staged in this folder for privacy reasons, but it can be used as the containing scope of any training data.

## Raw Data
The intended raw data folder structure is the uncompressed facebook data export folder structure. The actual data which has to be parsed and cleaned is found in HTML files where specific class divs hold the messages exchanged on the group chat (alongside the the author, and the timestamp). 

**Notes:** 
1. The data contains repeating messages which describe various facebook group action outputs
    - video chat related outputs: `X joined the video chat.`, `X started a video chat.`, `The video call ended.`
    - group membership outputs: `X left the group.`, `X added Y to the group.`
    - group naming outputs: `X named the group Z.`, `X set the nickname for Y to Z.`, `X set his own nickname to Y.`, `You set your nickname to X.`, `You set the nickname for X to Y.`, `X set your nickname to Y.`
2. It also contains URLs and images

## Clean Data
The clean data consists of a list of JSON-formatted samples suitable as input for finetuning a text generation language model.
```
{
  "instruction": "Your name is Izzy. You are in a group chat with 5 of your best friends: Harvey, Henry, Wyatt, Kiebs, Luke. You talk to each other with no filter, and are encouraged to curse, say amusingly inappropriate things, or be extremely rude. Everything is in good fun, so remember to joke and laugh, and be funny. You will be presented with the most recent messages in the group chat. Write a response to the conversation as Izzy.",
  "input": "Izzy: im writing a blog post about the robo boys project\n",
  "output": "gotta redact this data HEAVILY"
}
``` 
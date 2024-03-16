const chatForm = get('form');
const chatInput = get('input');
const chatBox = get('main');

let lastUserQuery;
let messageLimit = 5;
const previousMessages = [];

appendMessage('bot', 'Hello');
appendMessage('bot', 'How can we aid you?');


chatForm.addEventListener('submit', event => {
  event.preventDefault();
  const text = chatInput.value;
  if (!text) return;
  
  appendMessage('user', text);
  chatInput.value = '';
});

function appendMessage(side, text) {
  const bubble = `
    <div class="msg -${side}">
        <div class="bubble">${text}</div>
    </div>`;
  chatBox.insertAdjacentHTML('beforeend', bubble);
  chatBox.scrollTop += 500;

  previousMessages.push(side + ":" + text);


  if (side == 'user') {
    lastUserQuery = text
    
    messages = createMessagesToSend();

    console.log(messages);
    sendMessageToBot(messages);
  }

}

// Utils
function get(selector, root = document) {
  return root.querySelector(selector);
}

function createMessagesToSend () {
  let buf = []
  let count = 0 
  for (var i = previousMessages.length - 1; i > previousMessages.length - messageLimit - 1; i--) {
    if (previousMessages[i] !== undefined) {
      buf[count] = previousMessages[i]
      count += 1
    }
  }


  const messages = {
    "query": lastUserQuery,
    "buf": buf
  }

  console.log(messages)

  return messages
}


function sendMessageToBot (messages) {

  // headers = {
  //   "Accept" : "application/json",
  //   "Content-Type": "application/json" ,
  // }


  // const request = new Request("model_query", {
  //   header: headers,
  //   method: "POST",
  //   body: messages,
  // });

  // fetch(request)
  // .then((response) => {
  //   if (!response.ok) {
  //     throw new Error(`HTTP error! Status: ${response.status}`);
  //   }

  //   return response.blob();
  // })
  // .then((response) => {
  //   const url = request.url;
  //   const method = request.method;
  //   const credentials = request.credentials;
  //   const bodyUsed = request.bodyUsed;
  
  //   console.log(url,method, credentials, bodyUsed)
  
  //   appendMessage()
  // });

  var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

  var raw = JSON.stringify({
    "buf": [
      "user:I have a bloody nose",
      "bot:How can we aid you?",
      "bot:Hello"
    ],
    "query": "I have a bloody nose"
  });

  var requestOptions = {
    method: 'POST',
    headers: myHeaders,
    body: raw,
    redirect: 'follow'
  };

fetch("http://127.0.0.1:5000/model_query", requestOptions)
  .then(response => response.text())
  // .then(result => console.log(response))
  .then(result => JSON.parse(result))
  .then(result => result[0])
  .then(result => result["generated_text"])
  .then(result => appendMessage("bot",result))
  .then(result => previousMessages.append(result))
  .catch(error => console.log('error', error));

  
}
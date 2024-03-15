const chatForm = get('form');
const chatInput = get('input');
const chatBox = get('main');

let lastUserQuery;
let messageLimit = 5;
const previousMessages = [];

appendMessage('bot', 'Hello');
appendMessage('bot', 'How can we aid you?');
appendMessage('bot', 'How can we aid you?');
appendMessage('bot', 'How can we aid you?');
appendMessage('bot', 'How can we aid you?');
appendMessage('bot', 'How can we aid you?');
appendMessage('user', 'I have a runny nose');
appendMessage('user', 'I have a bloody nose');


sendMessagesAndContextToModel();


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

  if (side == 'user') {
    lastUserQuery = text
  }

  previousMessages.push(text);

}



// Utils
function get(selector, root = document) {
  return root.querySelector(selector);
}

function sendMessagesAndContextToModel () {
  let buf = []
  let count = 0 
  for (var i = previousMessages.length - 1; i > previousMessages.length - messageLimit - 1; i--) {
    buf[count] = previousMessages[i]
    count += 1
  }


  const messages = {
    "query": lastUserQuery,
    "buf": buf
  }

  console.log(messages)

  return messages
}
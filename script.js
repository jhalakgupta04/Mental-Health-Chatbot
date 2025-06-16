
async function sendMessage() {
    const inputBox = document.getElementById("user-input");
    const userInput = inputBox.value.trim().toLowerCase();
    if (!userInput) return;

    appendMessage(`You: ${userInput}`, "user");

    const response = await fetch("/get_response", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ user_message: userInput })
    });

    const data = await response.json();
    const botResponse = data.response;

    appendMessage(`Chatbot: ${botResponse}`, "bot");
    inputBox.value = "";
}

function appendMessage(message, sender) {
    const chatBox = document.getElementById("chat-box");
    const msg = document.createElement("div");
    msg.className = sender;
    msg.innerText = message;
    chatBox.appendChild(msg);
    chatBox.scrollTop = chatBox.scrollHeight;
}

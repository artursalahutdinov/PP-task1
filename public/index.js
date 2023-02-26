const messages = document.querySelector("#messages");
const message = document.querySelector("#message")
const send = document.querySelector("#send_message");
const status = document.querySelector("#status");

const addMessage = (message, owner) => {
    const element = document.createElement("div");
    element.classList.add("message")

    if (owner) {
        element.classList.add("message__owner")
    }

    element.textContent = message

    messages.appendChild(element)
} 

(async() => {
    await fetch("/reset");

    send.addEventListener("click", async () => {
        const text = message.value;
        if (!text) return;

        addMessage(text, true);

        message.value = "";
        status.textContent = "Benjamin is typing...";

        const response = await fetch("/message", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json;charset=utf-8'
            },
            body: JSON.stringify({ message: text })
        });
    
        if (response.status === 200) {
            const result = await response.json();
            const { text } = result.messages[result.messages.length - 1];
            
            addMessage(text, false)
        }

        status.textContent = "";
    });
})();


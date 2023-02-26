const message = document.querySelector("#message")
const send = document.querySelector("#send");

const messages = document.querySelector("#messages");

(async() => {
    await fetch("/reset");

    send.addEventListener("click", async () => {
        const text = message.value;
        
        const element = document.createElement("div");
        element.textContent = text;
        messages.appendChild(element)
    
        const response = await fetch("/message", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json;charset=utf-8'
            },
            body: JSON.stringify({ message: text })
        });
    
        if (response.status === 200) {
            const result = await response.json();
            
            const element = document.createElement("div");
            element.textContent = result.messages[result.messages.length - 1].text;
    
            messages.appendChild(element)
        }
    });
})();


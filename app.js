// Get the form element with id "chat-form" and add an event listener for the "submit" event
document.getElementById("chat-form").addEventListener("submit", async (event) => {
    event.preventDefault();  // Prevent the form from submitting normally
    const consigne = document.getElementById("consigne").value;  // Get the value of the input field with id "consigne"
    const texte = document.getElementById("texte").value;  // Get the value of the input field with id "texte"
    const responseDiv = document.getElementById("response");  // Get the div element with id "response"

    responseDiv.innerHTML = "";  // Clear the response div

    const formData = new FormData();  // Create a new FormData object
    formData.append("consigne", consigne);  // Append the consigne value to the form data
    formData.append("texte", texte);  // Append the texte value to the form data

    // Send a POST request to the specified URL with the form data
    const response = await fetch("http://127.0.0.1:8000/stream_chat", {   
        method: "POST",
        body: formData,
    });

    const reader = response.body.getReader();  // Get a ReadableStream reader from the response's body
    const textDecoder = new TextDecoder("utf-8");  // Create a new TextDecoder for utf-8 encoded text

    while (true) {  // Loop indefinitely
        const { value, done } = await reader.read();  // Read a chunk of data from the stream
        if (done) break;  // If the reader is done reading the data, break out of the loop

        const chunk = textDecoder.decode(value);  // Decode the chunk of data as text
        responseDiv.innerHTML += chunk;  // Append the decoded text to the response div
    }
});

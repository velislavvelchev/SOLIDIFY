function typeWriterEffect(elementId, message, speed = 10, delay = 30000, callback = null) {
    const textElement = document.getElementById(elementId);
    if (!textElement) return;
    let index = 0;

    function typeWriter() {
        if (index < message.length) {
            // Handle double newline as paragraph break
            if (message.substring(index, index + 2) === '\n\n') {
                textElement.innerHTML += '<br><br>';
                index += 2;
            }
            // Handle single newline as line break
            else if (message.charAt(index) === '\n') {
                textElement.innerHTML += '<br>';
                index += 1;
            }
            // Regular character
            else {
                textElement.innerHTML += message.charAt(index);
                index += 1;
            }
            setTimeout(typeWriter, speed);
        }
    }
    typeWriter();
}




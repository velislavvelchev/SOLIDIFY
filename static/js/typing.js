const message = "Manage your habits and routines effectively!";
const textElement = document.getElementById('dynamic-text');
let index = 0;

function typeWriter() {
  if (index < message.length) {
    textElement.innerHTML += message.charAt(index);
    index++;
    setTimeout(typeWriter, 100);
  } else {
    setTimeout(() => {
      textElement.innerHTML = '';
      index = 0;
      typeWriter();
    }, 3000);
  }
}

// Start the animation
window.onload = () => {
  typeWriter();
};

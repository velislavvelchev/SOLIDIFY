const message = "In short, Solidify is an application that serves to optimize our habits and align them to our personal goals, so that we can both enjoy our lives while also achieving our goals.\n" +
    "Most people nowadays, especially in urban cities,  have extremely fast and busy lives, where they try to constantly keep up with their numerous aspirations related to things like career paths, physical fitness, personal relationships etc. This very often leads to redundant stress, especially when any of the above-mentioned domains is compromised.";
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

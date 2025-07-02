const pupilL = document.getElementById('pupilL');
const pupilR = document.getElementById('pupilR');
const eyeL = document.getElementById('eyeL');
const eyeR = document.getElementById('eyeR');

function blink() {
  eyeL.setAttribute('ry', 3.5);
  eyeR.setAttribute('ry', 3.5);
  pupilL.setAttribute('ry', 2.5);
  pupilR.setAttribute('ry', 2.5);
  setTimeout(() => {
    eyeL.setAttribute('ry', 14);
    eyeR.setAttribute('ry', 14);
    pupilL.setAttribute('ry', 5.8);
    pupilR.setAttribute('ry', 5.8);
  }, 180);
  setTimeout(blink, 2200 + Math.random()*1300);
}
setTimeout(blink, 900);

// "Talk" effect: slightly wiggle the speech bubble
const speech = document.getElementById('speech');
let wiggle = 0;
function bubbleWiggle() {
  wiggle = (wiggle + 1) % 2;
  speech.style.transform = `scale(1.01) translateY(${wiggle?'-3px':'2px'})`;
  setTimeout(bubbleWiggle, 600 + Math.random()*700);
}
setTimeout(bubbleWiggle, 2200);

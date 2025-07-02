// Blinking animation
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
  setTimeout(blink, 2100 + Math.random()*1100);
}
setTimeout(blink, 1000);

// "Talk" effect: slightly wiggle the speech bubble
const speech = document.getElementById('speech');
let wiggle = 0;
function bubbleWiggle() {
  wiggle = (wiggle + 1) % 2;
  speech.style.transform = `scale(1.01) translateY(${wiggle?'-2.5px':'1.8px'})`;
  setTimeout(bubbleWiggle, 600 + Math.random()*700);
}
setTimeout(bubbleWiggle, 2100);

// Animate brain connection nodes (pulse in sequence)
const nodeIDs = ['node1','node2','node3','node4','node5'];
let connectionStep = 0;
function pulseConnections() {
  nodeIDs.forEach((id, idx) => {
    const node = document.getElementById(id);
    if (!node) return;
    if (idx === connectionStep % nodeIDs.length) {
      node.setAttribute('r', 18);
      node.setAttribute('opacity', 1);
    } else {
      node.setAttribute('r', 11);
      node.setAttribute('opacity', 0.8);
    }
  });
  connectionStep++;
  setTimeout(pulseConnections, 430);
}
pulseConnections();

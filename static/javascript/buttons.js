const buttons = document.querySelectorAll('.button')

for (let i = 0; i < buttons.length; i++) {
    const button = buttons[i];
    button.addEventListener('mousemove', rising);
    button.addEventListener('mouseout', stopRising);
}

function rising(event) {
    const button = this
    button.style.background = '#F64C72';
    button.style.transform = 'scale(1.2)'
}

function stopRising(event) {
    const button = this
    button.style.background = 'none';
    button.style.transform = 'scale(1)'
}
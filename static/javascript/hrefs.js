const buttons = document.querySelectorAll('.url')


for (let i = 0; i < buttons.length; i++) {
    const button = buttons[i];
    button.addEventListener('mousemove', rising);
    button.addEventListener('mouseout', stopRising);
}


function rising(event) {
    const button = this
    button.style.background = '#FAFAFA'
    button.style.color = '#171717'
}

function stopRising(event) {
    const button = this
    button.style.background = 'none'
    button.style.color = '#FAFAFA'
}
const cards = document.querySelectorAll('.card')

for (let i = 0; i < cards.length; i++) {
    const card = cards[i];
    card.addEventListener('mousemove', rising);
    card.addEventListener('mouseout', stopRising);
}

function rising(event) {
    const card = this
    card.style.border = "3px solid #FAFAFA"
    card.style.transform = 'scale(1.2)'
    card.style.boxShadow = '0 0 150px #000000'
    card.style.zIndex = "2"


}

function stopRising(event) {
    const card = this
    card.style.border = "1px solid #FAFAFA"
    card.style.transform = 'scale(1)'
    card.style.boxShadow = '0 0 0'
    card.style.zIndex = "auto"
}
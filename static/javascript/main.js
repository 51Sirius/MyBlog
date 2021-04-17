const card = document.querySelectorAll('.card')
card.addEventListener('mousemove', rotate())

function rotate(event) {
    const cardItem = this.querySelector('.card-item');
    cardItem.innerText = event.offsetY;
    console.log(event.offsetY)
}
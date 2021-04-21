const card = document.querySelector('#spaceBot')

card.addEventListener('mousemove', evt => create_bg(evt, 'https://www.bestsiling.ru/images/kosmos/19.jpg'));
card.addEventListener('mouseout', );


function create_bg(event, image) {
    const bg = document.querySelector('body')
    bg.style.backgroundImage = 'url(' + image + ') !important;'
}

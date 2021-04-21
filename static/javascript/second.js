const card = document.querySelector('#spaceBot')

card.addEventListener('mousemove', evt => create_bg(evt, 'https://www.bestsiling.ru/images/kosmos/19.jpg'));
card.addEventListener('mouseout', delete_bg);


function create_bg(event, image) {
    document.body.style.backgroundImage = 'url("' + image + '")'
}

function delete_bg(event) {
    document.body.style.backgroundImage = 'linear-gradient( 109.6deg,  rgba(14,11,56,1) 11.2%, rgb(2, 81, 109) 91.1% )'
}
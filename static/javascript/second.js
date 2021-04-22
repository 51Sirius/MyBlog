const card = document.querySelector('#spaceBot')

card.addEventListener('mousemove', evt => create_bg(evt, 'https://www.bestsiling.ru/images/kosmos/19.jpg'));
card.addEventListener('mouseout', delete_bg);


function create_bg(event, image) {
    document.body.style.backgroundImage = 'url("' + image + '")'
}

function delete_bg(event) {
    document.body.style.background = 'linear-gradient(rgba(0, 0, 0, 0.5), rgb(0, 0, 0)) 0 0 / cover no-repeat fixed, url("https://source.unsplash.com/tHtZo3FLhPc/1920x1080") center center'
}
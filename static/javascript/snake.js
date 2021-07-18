let width = screen.width;
let height = screen.height;
let blockSize = [width / 40, height / 24];
let widthBlock = String(blockSize[0]) + 'px';
let heightBlock = String(blockSize[1]) + 'px';
let time = 500
let stopGame = false;
let score = 0

function getRandomInt(max) {
    return Math.floor(Math.random() * max);
}


class Apple {
    constructor() {
        let block = document.createElement('div')
        block.className = 'apple'
        document.body.appendChild(block)
        this.block = document.getElementsByClassName('apple')[0];
        this.coords = [getRandomInt(39), getRandomInt(20)]
        this.block.style.width = widthBlock;
        this.block.style.height = heightBlock;
        this.block.style.marginTop = String(this.coords[1] * blockSize[1]) + 'px'
        this.block.style.marginLeft = String(this.coords[0] * blockSize[0]) + 'px'
    }
}

class SnakeBlock {
    constructor(direction = 1, number = 0, second = false) {
        let block = document.createElement('div')
        this.number = number
        let className = 'snake'
        if (second) {
            className = 'second-snake'
        }
        block.className = className
        document.body.appendChild(block)
        if (!second) {
            this.block = document.getElementsByClassName(className)[0];
        } else {
            this.block = document.getElementsByClassName(className)[number - 1];
        }
        this.block.style.width = widthBlock;
        this.block.style.height = heightBlock;
        this.coords = [0, 0]
        this.block.style.marginTop = '0px';
        this.block.style.marginLeft = '0px';
        this.direction = direction
        this.next = []
        this.eat = false
        this.lastDirection = 0;
        this.buttonPress = false
    }

    setPosition() {
        this.block.style.marginLeft = String(this.coords[0] * blockSize[0]) + 'px'
        this.block.style.marginTop = String(this.coords[1] * blockSize[1]) + 'px'
    }

    newBlock() {
        let direction = this.direction
        if (this.next[0] != null) {
            direction = this.next[this.next.length - 1].direction
        }
        this.next.push(new SnakeBlock(direction, this.next.length + 1, true))
        let x = this.coords[0];
        let y = this.coords[1];
        if (this.next[1] != null) {
            x = this.next[this.next.length - 2].coords[0]
            y = this.next[this.next.length - 2].coords[1]
        }
        if (this.next[this.next.length - 1].direction === 1) {
            this.next[this.next.length - 1].coords = [x - 1, y]
        } else if (this.next[this.next.length - 1].direction === 2) {
            this.next[this.next.length - 1].coords = [x + 1, y]
        } else if (this.next[this.next.length - 1].direction === 3) {
            this.next[this.next.length - 1].coords = [x, y - 1]
        } else if (this.next[this.next.length - 1].direction === 4) {
            this.next[this.next.length - 1].coords = [x, y + 1]
        }
        this.next[this.next.length - 1].setPosition()
        this.eat = false
    }

    move() {
        document.addEventListener("keydown", getDirection)
        if (this.next[0] != null && this.number === 0) {
            for (let i = this.next.length - 1; i !== 0; i--) {
                this.next[i].setDirection(this.next[i - 1].direction)
                this.next[i].move()
            }
            this.next[0].setDirection(this.lastDirection)
            this.next[0].move()
        }
        this.lastDirection = this.direction
        if (this.direction === 1) {
            this.coords[0]++
            this.block.style.marginLeft = String(this.coords[0] * blockSize[0]) + 'px'
        } else if (this.direction === 2) {
            this.coords[0]--
            this.block.style.marginLeft = String(this.coords[0] * blockSize[0]) + 'px'
        } else if (this.direction === 3) {
            this.coords[1]++
            this.block.style.marginTop = String(this.coords[1] * blockSize[1]) + 'px'
        } else if (this.direction === 4) {
            this.coords[1]--
            this.block.style.marginTop = String(this.coords[1] * blockSize[1]) + 'px'
        }
        this.buttonPress = false
        if (this.number === 0) {
            return this.checkbox()
        }

    }

    checkbox() {
        if ((this.coords[0] === apple.coords[0]) && (this.coords[1] === apple.coords[1])) {
            this.eat = true
        }
        if (this.next[0] != null) {
            for (let i = this.next.length - 1; i !== -1; i--) {
                if (this.coords[0] === this.next[i].coords[0] && this.coords[1] === this.next[i].coords[1]) {
                    return true
                }
            }
        }
        if (!((this.coords[0] <= 40 && this.coords[0] >= 0) && (this.coords[1] <= 24 && this.coords[1] >= 0))) {
            return true
        }
        return false
    }

    setDirection(direction) {
        this.lastDirection = this.direction
        this.direction = direction
        this.buttonPress = true
    }
}

function getDirection(e) {
    if (!snakeJ.buttonPress) {
        let direction = snakeJ.direction;
        switch (e.key) {
            case "ArrowLeft":
                if (snakeJ.direction !== 1 && snakeJ.coords[0] !== 0) {
                    direction = 2
                }
                break
            case "ArrowUp":
                if (snakeJ.direction !== 3 && snakeJ.coords[1] !== 0) {
                    direction = 4
                }
                break
            case "ArrowRight":
                if (snakeJ.direction !== 2 && snakeJ.coords[0] !== 40) {
                    direction = 1
                }
                break
            case "ArrowDown":
                if (snakeJ.direction !== 4 && snakeJ.coords[1] !== 24) {
                    direction = 3
                }
                break
        }
        snakeJ.setDirection(direction)
    }
}

const snakeJ = new SnakeBlock(1)
let apple = new Apple()

function drawScore() {
    document.body.getElementsByClassName("score")[0].innerHTML = "Score: " + score
}


let timer = setInterval(function () {
    if (stopGame) {
        clearInterval(timer);
        gameOver()
    }
    stopGame = snakeJ.move(apple)
    if (snakeJ.eat) {
        score++
        drawScore()
        snakeJ.newBlock()
        apple.block.remove()
        apple = new Apple()
    }
}, time);


function gameOver() {
    let block = document.createElement('a')
    let font = document.createElement('p')
    block.className = "game-over"
    font.className = "game-over-font"
    document.body.appendChild(block)
    block = document.body.getElementsByClassName("game-over")[0]
    block.href = "game.html"
    block.appendChild(font)
    font = document.body.getElementsByClassName("game-over-font")[0]
    font.innerHTML = "Игра окончена"


}

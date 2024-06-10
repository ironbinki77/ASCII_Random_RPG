class Character {
    constructor() {
        this.character = document.getElementById('character');
        this.keysPressed = {};
        this.moveSpeed = 4;
        this.animationFrameId = null;
        this.mapPosition = { top: 0, left: 0 };

        document.addEventListener('keydown', (e) => this.onKeyDown(e));
        document.addEventListener('keyup', (e) => this.onKeyUp(e));

        this.updateMapAndBoundary();
        this.animationFrameId = requestAnimationFrame(() => this.updateMapPosition());
    }

    onKeyDown(e) {
        this.keysPressed[e.key] = true;
        this.updateCharacterImage(e.key);

        if (e.code === 'Space') {
            this.hideMenus();
        }
    }

    onKeyUp(e) {
        this.keysPressed[e.key] = false;
    }

    updateCharacterImage(key) {
        const directions = {
            'ArrowUp': '/static/ascii_lib/character/character_up.png',
            'ArrowDown': '/static/ascii_lib/character/character_down.png',
            'ArrowLeft': '/static/ascii_lib/character/character_left.png',
            'ArrowRight': '/static/ascii_lib/character/character_right.png'
        };

        if (directions[key]) {
            this.character.style.backgroundImage = `url(${directions[key]})`;
        }
    }

    updateMapPosition() {
        // Implement the logic to update the map position based on key presses
    }

    updateMapAndBoundary() {
        // Implement the logic to update the map and boundary positions
    }

    hideMenus() {
        // Implement the logic to hide all game menus
    }
}

const character = new Character();

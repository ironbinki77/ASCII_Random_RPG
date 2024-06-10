// map.js for handling the map and character movements
document.addEventListener('DOMContentLoaded', (event) => {
    const villageMap = document.getElementById('village-map');
    const character = document.getElementById('character');
    const dungeonMap = document.getElementById('dungeon-map');
    const dungeonPortals = document.querySelectorAll('.dungeon-portal');
    let currentMap = villageMap;
    let mapPosition = { top: 0, left: 0 };
    const keysPressed = {};
    const moveSpeed = 4;
    const screenWidth = document.querySelector('.game-screen').clientWidth;
    const screenHeight = document.querySelector('.game-screen').clientHeight;
    const boundaryWidth = screenWidth * 1.2;
    const boundaryHeight = screenHeight * 1.8;

    const villageBoundaryLimits = {
        top: -(boundaryHeight / 2),
        bottom: boundaryHeight / 2,
        left: -(boundaryWidth / 2),
        right: boundaryWidth / 2,
    };

    function updateMapAndBoundary() {
        const map = currentMap;
        if (currentMap === villageMap) {
            const boundary = currentMap.querySelector('#boundary');
            boundary.style.width = `${boundaryWidth}px`;
            boundary.style.height = `${boundaryHeight}px`;
            boundary.style.top = `${-boundaryWidth / 4}px`;
            boundary.style.left = `${-boundaryHeight}px`;
        }
        map.style.transform = `translate(${mapPosition.left}px, ${mapPosition.top}px)`;
    }

    let collisionDirection = null;

    function updateMapPosition() {
        if (isMenuActive()) {
            animationFrameId = null;
            return;
        }

        const boundaryLimits = currentMap === villageMap ? villageBoundaryLimits : null;

        let newPosition = { ...mapPosition };

        if (keysPressed['ArrowUp'] && (!boundaryLimits || mapPosition.top < boundaryLimits.bottom) && collisionDirection !== 'down') {
            newPosition.top += moveSpeed;
        }
        if (keysPressed['ArrowDown'] && (!boundaryLimits || mapPosition.top > boundaryLimits.top) && collisionDirection !== 'up') {
            newPosition.top -= moveSpeed;
        }
        if (keysPressed['ArrowLeft'] && (!boundaryLimits || mapPosition.left < boundaryLimits.right) && collisionDirection !== 'right') {
            newPosition.left += moveSpeed;
        }
        if (keysPressed['ArrowRight'] && (!boundaryLimits || mapPosition.left > boundaryLimits.left) && collisionDirection !== 'left') {
            newPosition.left -= moveSpeed;
        }

        if (!isCollision(newPosition)) {
            mapPosition = newPosition;
            collisionDirection = null;
        } else {
            handleCollision(newPosition);
        }

        updateMapAndBoundary();
        checkCollisionWithDungeonPortals();
        checkCollisionWithNPCs();
        animationFrameId = requestAnimationFrame(updateMapPosition);
    }

    function isCollision(newPosition) {
        const characterRect = character.getBoundingClientRect();
        const mapRect = currentMap.getBoundingClientRect();

        const newCharacterRect = {
            top: characterRect.top + (newPosition.top - mapPosition.top),
            bottom: characterRect.bottom + (newPosition.top - mapPosition.top),
            left: characterRect.left + (newPosition.left - mapPosition.left),
            right: characterRect.right + (newPosition.left - mapPosition.left)
        };

        const blocks = document.querySelectorAll('.block');
        for (const block of blocks) {
            const blockRect = block.getBoundingClientRect();
            if (
                newCharacterRect.left < blockRect.right &&
                newCharacterRect.right > blockRect.left &&
                newCharacterRect.top < blockRect.bottom &&
                newCharacterRect.bottom > blockRect.top
            ) {
                const overlapBottom = newCharacterRect.bottom - blockRect.top;
                const overlapTop = blockRect.bottom - newCharacterRect.top;
                const overlapLeft = blockRect.right - newCharacterRect.left;
                const overlapRight = newCharacterRect.right - blockRect.left;

                const minOverlap = Math.min(overlapBottom, overlapTop, overlapLeft, overlapRight);

                if (minOverlap === overlapBottom) {
                    collisionDirection = 'down';
                } else if (minOverlap === overlapTop) {
                    collisionDirection = 'up';
                } else if (minOverlap === overlapLeft) {
                    collisionDirection = 'left';
                } else if (minOverlap === overlapRight) {
                    collisionDirection = 'right';
                }
                return true;
            }
        }
        return false;
    }

    function handleCollision(newPosition) {
        if (collisionDirection === 'up' && keysPressed['ArrowDown']) {
            mapPosition.top = newPosition.top;
        } else if (collisionDirection === 'down' && keysPressed['ArrowUp']) {
            mapPosition.top = newPosition.top;
        } else if (collisionDirection === 'left' && keysPressed['ArrowRight']) {
            mapPosition.left = newPosition.left;
        } else if (collisionDirection === 'right' && keysPressed['ArrowLeft']) {
            mapPosition.left = newPosition.left;
        }
    }

    function checkCollisionWithDungeonPortals() {
        const characterRect = character.getBoundingClientRect();
        dungeonPortals.forEach(portal => {
            const portalRect = portal.getBoundingClientRect();
            if (
                characterRect.left < portalRect.right &&
                characterRect.right > portalRect.left &&
                characterRect.top < portalRect.bottom &&
                characterRect.bottom > portalRect.top
            ) {
                toggleMap();
            }
        });
    }

    function toggleMap() {
        if (currentMap === villageMap) {
            switchToDungeonMap();
        } else {
            switchToVillageMap();
        }
    }

    function switchToDungeonMap() {
        currentMap.style.display = 'none';
        dungeonMap.style.display = 'flex';
        currentMap = dungeonMap;
        mapPosition = { top: 0, left: 0 };
        updateMapAndBoundary();
    }

    function switchToVillageMap() {
        currentMap.style.display = 'none';
        villageMap.style.display = 'flex';
        currentMap = villageMap;
        mapPosition = { top: 0, left: 0 };
        updateMapAndBoundary();
    }

    updateMapAndBoundary();
    animationFrameId = requestAnimationFrame(updateMapPosition);

    document.addEventListener('keydown', (e) => {
        keysPressed[e.key] = true;

        switch (e.key) {
            case 'ArrowUp':
                character.style.backgroundImage = "url('/static/ascii_lib/character/character_up.png')";
                shopMenuShown = false;
                enhanceMenuShown = false;
                break;
            case 'ArrowDown':
                character.style.backgroundImage = "url('/static/ascii_lib/character/character_down.png')";
                shopMenuShown = false;
                enhanceMenuShown = false;
                break;
            case 'ArrowLeft':
                character.style.backgroundImage = "url('/static/ascii_lib/character/character_left.png')";
                shopMenuShown = false;
                enhanceMenuShown = false;
                break;
            case 'ArrowRight':
                character.style.backgroundImage = "url('/static/ascii_lib/character/character_right.png')";
                shopMenuShown = false;
                enhanceMenuShown = false;
                break;
        }

        if (collisionDirection) {
            if ((collisionDirection === 'up' && e.key === 'ArrowDown') ||
                (collisionDirection === 'down' && e.key === 'ArrowUp') ||
                (collisionDirection === 'left' && e.key === 'ArrowRight') ||
                (collisionDirection === 'right' && e.key === 'ArrowLeft')) {
                collisionDirection = null;
            }
        }
    });

    document.addEventListener('keyup', (e) => {
        keysPressed[e.key] = false;
    });
});

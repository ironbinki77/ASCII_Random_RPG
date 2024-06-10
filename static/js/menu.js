document.addEventListener('DOMContentLoaded', (event) => {
    const menuItems = document.querySelectorAll('.game-menu');
    const homeLink = document.getElementById('home');
    let menuActive = false;
    let animationFrameId = null;

    document.querySelectorAll('nav a').forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const targetId = link.getAttribute('href').substring(1);
            menuItems.forEach(item => {
                item.style.display = item.id === targetId ? 'block' : 'none';
            });
            menuActive = targetId !== '';
            if (menuActive && animationFrameId !== null) {
                cancelAnimationFrame(animationFrameId);
                animationFrameId = null;
            }
            if (!menuActive && animationFrameId === null) {
                animationFrameId = requestAnimationFrame(updateMapPosition);
            }
        });
    });

    // Other functions related to menu handling...
});
class GameMenu {
    constructor() {
        this.menuItems = document.querySelectorAll('.game-menu');
        this.homeLink = document.getElementById('home');
        this.menuActive = false;
        this.animationFrameId = null;
        this.setupEventListeners();
    }

    setupEventListeners() {
        document.querySelectorAll('nav a').forEach(link => {
            link.addEventListener('click', (e) => this.handleMenuClick(e, link));
        });

        this.homeLink.addEventListener('click', () => this.closeMenus());
    }

    handleMenuClick(event, link) {
        event.preventDefault();
        const targetId = link.getAttribute('href').substring(1);
        this.menuItems.forEach(item => {
            item.style.display = item.id === targetId ? 'block' : 'none';
        });
        this.menuActive = targetId !== '';
        if (this.menuActive && this.animationFrameId !== null) {
            cancelAnimationFrame(this.animationFrameId);
            this.animationFrameId = null;
        }
        if (!this.menuActive && this.animationFrameId === null) {
            this.animationFrameId = requestAnimationFrame(() => this.updateMapPosition());
        }
    }

    closeMenus() {
        this.menuItems.forEach(item => {
            item.style.display = 'none';
        });
        this.menuActive = false;
        if (this.animationFrameId === null) {
            this.animationFrameId = requestAnimationFrame(() => this.updateMapPosition());
        }
    }

    isMenuActive() {
        return this.menuActive;
    }

    updateMapPosition() {
        // Implementation of the map position update logic
    }
}

class Inventory {
    constructor() {
        this.inventoryList = document.getElementById('inventory-list');
        this.loadInventory();
    }

    loadInventory() {
        fetch('/inventory/')
            .then(response => response.json())
            .then(data => {
                this.inventoryList.innerHTML = '';
                for (const [itemCode, quantity] of Object.entries(data)) {
                    const listItem = document.createElement('li');
                    listItem.textContent = `Item Code: ${itemCode}, Quantity: ${quantity}`;
                    this.inventoryList.appendChild(listItem);
                }
            });
    }
}

class Shop {
    constructor() {
        this.shopList = document.getElementById('shop-list');
        this.loadShopItems();
    }

    loadShopItems() {
        fetch('/shop/items/')
            .then(response => response.json())
            .then(data => {
                this.shopList.innerHTML = '';
                for (const [itemCode, itemData] of Object.entries(data)) {
                    const listItem = document.createElement('li');
                    listItem.innerHTML = `
                        <p>${itemData.name}: ${itemData.description}</p>
                        <p>Price: ${itemData.buyPrice} gold</p>
                        <button onclick="shop.buyItem(${itemCode})">Buy</button>
                    `;
                    this.shopList.appendChild(listItem);
                }
            });
    }

    buyItem(itemCode) {
        fetch(`/buy_item/${itemCode}/`, { method: 'POST' })
            .then(response => {
                if (response.ok) {
                    alert('Item bought successfully!');
                    inventory.loadInventory();  // Refresh inventory
                } else {
                    alert('Failed to buy item. Check your gold or inventory space.');
                }
            });
    }
}

class Enhance {
    constructor() {
        this.enhanceList = document.getElementById('enhance-list');
        this.loadEnhanceableItems();
    }

    loadEnhanceableItems() {
        fetch('/inventory/')
            .then(response => response.json())
            .then(data => {
                this.enhanceList.innerHTML = '';
                for (const [itemCode, quantity] of Object.entries(data)) {
                    const listItem = document.createElement('li');
                    listItem.textContent = `Item Code: ${itemCode}, Quantity: ${quantity}`;
                    listItem.addEventListener('click', () => this.enhanceItem(itemCode));
                    this.enhanceList.appendChild(listItem);
                }
            });
    }

    enhanceItem(itemCode) {
        fetch(`/enhance/${itemCode}/`)
            .then(response => response.json())
            .then(data => {
                alert(data.message);
                inventory.loadInventory();  // Refresh the inventory after enhancing an item
            });
    }
}

// Initialize classes after DOM content is loaded
document.addEventListener('DOMContentLoaded', (event) => {
    const gameMenu = new GameMenu();
    const inventory = new Inventory();
    const shop = new Shop();
    const enhance = new Enhance();
});


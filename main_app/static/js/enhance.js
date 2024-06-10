document.addEventListener('DOMContentLoaded', (event) => {
    const items = {
        "1": {
            "name": "Racket",
            "description": "A simple sword for beginners.",
            "type": "Weapon",
            "strengthPower": 3,
            "buyPrice": 8,
            "sellPrice": 4,
            "image": "static/images/racket.png"
        },
        "3": {
            "name": "Potion",
            "description": "A potion that restores a small amount of health.",
            "type": "Consumable",
            "healthBoost": 20,
            "buyPrice": 5,
            "sellPrice": 2.5,
            "image": "static/images/potion.png"
        },
        "10": {
            "name": "Fruit",
            "description": "A sturdy helm for battle",
            "type": "Armor",
            "defensePower": 12,
            "buyPrice": 40,
            "sellPrice": 20,
            "image": "static/images/fruit.png"
        }
    };

    function loadEnhanceableItems() {
        fetch('inventory.json')
            .then(response => response.json())
            .then(data => {
                const enhanceList = document.getElementById('enhance-list');
                enhanceList.innerHTML = '';
                const inventory = data[0]; // assuming inventory.json contains an array with a single object
                for (const [itemCode, quantity] of Object.entries(inventory)) {
                    const itemData = items[itemCode];
                    if (itemData) {
                        const listItem = document.createElement('li');
                        listItem.innerHTML = `
                            <img src="${itemData.image}" alt="${itemData.name}">
                            <div>
                                <p>${itemData.name}: ${itemData.description}</p>
                                <p>Quantity: ${quantity}</p>
                                <button onclick="enhanceItem(${itemCode})">Enhance</button>
                            </div>
                        `;
                        enhanceList.appendChild(listItem);
                    }
                }
            });
    }

    function enhanceItem(itemCode) {
        alert('This is a local test. Enhance feature is disabled.');
    }

    loadEnhanceableItems();
});

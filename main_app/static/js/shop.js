document.addEventListener('DOMContentLoaded', (event) => {
    const items = {
        "1": {
            "name": "Racket",
            "description": "A simple sword for beginners.",
            "type": "Weapon",
            "strengthPower": 3,
            "buyPrice": 8,
            "sellPrice": 4,
            "image": "{% static 'ascii_lib/itemracket.png' %}"
        },
        "2": {
            "name": "Mask",
            "description": "A simple shield for basic protection.",
            "type": "Armor",
            "defensePower": 3,
            "buyPrice": 10,
            "sellPrice": 5,
            "image": "{% static 'ascii_lib/itemmask.png' %}"
        },
        "3": {
            "name": "Potion",
            "description": "A potion that restores a small amount of health.",
            "type": "Consumable",
            "healthBoost": 20,
            "buyPrice": 5,
            "sellPrice": 2.5,
            "image": "{% static 'ascii_lib/itempotion.png' %}"
        },
        "4": {
            "name": "Shield",
            "description": "A better shield",
            "type": "Armor",
            "defensePower": 10,
            "buyPrice": 35,
            "sellPrice": 17.5,
            "image": "{% static 'ascii_lib/itemshield.png' %}"
        },
        "5": {
            "name": "Sword",
            "description": "A high-quality sword",
            "type": "Weapon",
            "strengthPower": 15,
            "buyPrice": 50,
            "sellPrice": 25,
            "image": "{% static 'ascii_lib/itemsword.png' %}"
        },
        "6": {
            "name": "Bowl",
            "description": "A high-quality shield",
            "type": "Armor",
            "defensePower": 15,
            "buyPrice": 55,
            "sellPrice": 27.5,
            "image": "{% static 'ascii_lib/itembowl.png' %}"
        },
        "7": {
            "name": "Fish",
            "description": "A wand for casting spells",
            "type": "Weapon",
            "intelligencePower": 20,
            "buyPrice": 60,
            "sellPrice": 30,
            "image": "{% static 'ascii_lib/itemfish.png' %}"
        },
        "8": {
            "name": "Long Sword",
            "description": "A high-quality Sword",
            "type": "Weapon",
            "intelligencePower": 10,
            "buyPrice": 40,
            "sellPrice": 20,
            "image": "{% static 'ascii_lib/itemlongsword.png' %}"
        },
        "9": {
            "name": "Bow",
            "description": "A sharp bow preferred by kingdom",
            "type": "Weapon",
            "strengthPower": 8,
            "buyPrice": 25,
            "sellPrice": 12.5,
            "image": "{% static 'ascii_lib/itembow.png' %}"
        },
        "10": {
            "name": "Fruit",
            "description": "A sturdy helm for battle",
            "type": "Armor",
            "defensePower": 12,
            "buyPrice": 40,
            "sellPrice": 20,
            "image": "{% static 'ascii_lib/itemfruit.png' %}"
        }
    };

    function loadShop() {
        const shopList = document.getElementById('shop-list');
        shopList.innerHTML = '';
        for (const [itemCode, itemData] of Object.entries(items)) {
            const listItem = document.createElement('li');
            listItem.innerHTML = `
                <img src="${itemData.image}" alt="${itemData.name}">
                <div>
                    <p>${itemData.name}: ${itemData.description}</p>
                    <p>Price: ${itemData.buyPrice} gold</p>
                    <button onclick="buyItem(${itemCode})">Buy</button>
                </div>
            `;
            shopList.appendChild(listItem);
        }
    }

    function buyItem(itemCode) {
        alert('This is a local test. The buy feature is disabled.');
    }

    loadShop();
});

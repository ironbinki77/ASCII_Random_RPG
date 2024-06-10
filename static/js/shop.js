document.addEventListener('DOMContentLoaded', (event) => {
    loadShop();
});

function loadShop() {
    fetch('/static/data/items.json')
        .then(response => response.json())
        .then(data => {
            const shopList = document.getElementById('shop-list');
            shopList.innerHTML = '';
            for (const [itemCode, itemData] of Object.entries(data)) {
                const listItem = document.createElement('li');
                listItem.innerHTML = `
                    <p>${itemData.name}: ${itemData.description}</p>
                    <p>Price: ${itemData.buyPrice} gold</p>
                    <button onclick="buyItem(${itemCode})">Buy</button>
                `;
                shopList.appendChild(listItem);
            }
        });
}

function buyItem(itemCode) {
    alert(`Item with code ${itemCode} bought successfully!`);
    // Add logic to update inventory and gold
}

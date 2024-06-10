function loadShop() {
    fetch('/static/data/items.json')  // Adjust this path according to your setup
        .then(response => response.json())
        .then(data => {
            const shopList = document.getElementById('shop-list');
            shopList.innerHTML = '';  // Clear any existing items
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
    fetch(`/buy_item/${itemCode}`, { method: 'POST' })
        .then(response => {
            if (response.ok) {
                alert('Item bought successfully!');
                loadInventory();  // Reload inventory to reflect the new item
            } else {
                alert('Failed to buy item. Check your gold or inventory space.');
            }
        });
}

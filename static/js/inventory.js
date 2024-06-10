document.addEventListener('DOMContentLoaded', (event) => {
    loadInventory();
});

function loadInventory() {
    fetch('/static/data/inventory.json')
        .then(response => response.json())
        .then(data => {
            const inventoryList = document.getElementById('inventory-list');
            inventoryList.innerHTML = '';
            for (const [itemCode, quantity] of Object.entries(data)) {
                const listItem = document.createElement('li');
                listItem.textContent = `Item Code: ${itemCode}, Quantity: ${quantity}`;
                inventoryList.appendChild(listItem);
            }
        });
}

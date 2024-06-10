document.addEventListener('DOMContentLoaded', (event) => {
    loadInventory();
});

function loadInventory() {
    fetch('/static/data/inventory.json')  // Adjust this path according to your setup
        .then(response => response.json())
        .then(data => {
            const inventoryList = document.getElementById('inventory-list');
            inventoryList.innerHTML = '';  // Clear any existing items
            for (const [itemCode, quantity] of Object.entries(data)) {
                const listItem = document.createElement('li');
                listItem.textContent = `Item Code: ${itemCode}, Quantity: ${quantity}`;
                inventoryList.appendChild(listItem);
            }
        });
}

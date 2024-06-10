document.addEventListener('DOMContentLoaded', (event) => {
    loadEnhanceableItems();
});

function loadEnhanceableItems() {
    fetch('/static/data/inventory.json')
        .then(response => response.json())
        .then(data => {
            const enhanceList = document.getElementById('enhance-list');
            enhanceList.innerHTML = '';
            for (const [itemCode, quantity] of Object.entries(data)) {
                const listItem = document.createElement('li');
                listItem.textContent = `Item Code: ${itemCode}, Quantity: ${quantity}`;
                listItem.addEventListener('click', () => {
                    enhanceItem(itemCode);
                });
                enhanceList.appendChild(listItem);
            }
        });
}

function enhanceItem(itemCode) {
    alert(`Item with code ${itemCode} enhanced successfully!`);
    // Add logic to enhance the item
}

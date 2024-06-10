function loadEnhanceableItems() {
    fetch('/inventory/')
        .then(response => response.json())
        .then(data => {
            const enhanceList = document.getElementById('enhance-list');
            enhanceList.innerHTML = '';  // Clear any existing items
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
    fetch(`/enhance/${itemCode}/`)
        .then(response => response.json())
        .then(data => {
            alert(data.message);
            loadInventory();  // Refresh the inventory after enhancing an item
        });
}

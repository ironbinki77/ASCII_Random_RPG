document.addEventListener('DOMContentLoaded', (event) => {
    function loadEnhanceableItems() {
        fetch('inventory.json')
            .then(response => response.json())
            .then(data => {
                const enhanceList = document.getElementById('enhance-list');
                enhanceList.innerHTML = '';
                for (const [itemCode, quantity] of Object.entries(data)) {
                    const listItem = document.createElement('li');
                    listItem.textContent = `Item Code: ${itemCode}, Quantity: ${quantity}`;
                    listItem.addEventListener('click', () => {
                        alert(`This is a local test. Enhance feature for item ${itemCode} is disabled.`);
                    });
                    enhanceList.appendChild(listItem);
                }
            });
    }

    loadEnhanceableItems();
});
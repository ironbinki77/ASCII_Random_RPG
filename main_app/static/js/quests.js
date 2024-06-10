document.addEventListener('DOMContentLoaded', (event) => {
    function loadQuests() {
        fetch('./quests.json')
            .then(response => response.json())
            .then(data => {
                const questList = document.getElementById('quest-list');
                questList.innerHTML = '';
                for (const [questCode, questData] of Object.entries(data)) {
                    const listItem = document.createElement('li');
                    listItem.innerHTML = `
                        <h3>${questData.name}</h3>
                        <p>${questData.description}</p>
                        <p>Reward: ${questData.reward[0]} XP, ${questData.reward[1]} gold</p>
                        <button onclick="startQuest(${questCode})">Start Quest</button>
                    `;
                    questList.appendChild(listItem);
                }
            });
    }

    function startQuest(questCode) {
        alert('This is a Alpha test. The start quest feature is disabled.');
    }

    loadQuests();
});
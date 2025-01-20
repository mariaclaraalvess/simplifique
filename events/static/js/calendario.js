/*function createCalendar(id) {
    const today = new Date();
    const calendar = document.getElementById(id);
    calendar.style.display = 'flex';
    calendar.style.flexDirection = 'column';
    calendar.style.alignItems = 'center';
    calendar.style.justifyContent = 'center';
    calendar.style.backgroundColor = '#FEE440';
    calendar.style.padding = '20px';
    calendar.style.borderRadius = '10px';
    calendar.style.fontFamily = 'Arial, sans-serif';
    calendar.style.color = '#333';

    const monthNames = [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ];

    const monthYear = document.createElement('h3');
    monthYear.textContent = `${monthNames[today.getMonth()]} ${today.getFullYear()}`;
    calendar.appendChild(monthYear);

    const daysHeader = document.createElement('div');
    daysHeader.style.display = 'grid';
    daysHeader.style.gridTemplateColumns = 'repeat(7, 1fr)';
    daysHeader.style.gap = '5px';
    daysHeader.innerHTML = `
        <strong>Dom</strong><strong>Seg</strong><strong>Ter</strong><strong>Qua</strong>
        <strong>Qui</strong><strong>Sex</strong><strong>Sáb</strong>
    `;
    calendar.appendChild(daysHeader);

    const daysGrid = document.createElement('div');
    daysGrid.style.display = 'grid';
    daysGrid.style.gridTemplateColumns = 'repeat(7, 1fr)';
    daysGrid.style.gap = '5px';

    const firstDay = new Date(today.getFullYear(), today.getMonth(), 1).getDay();
    const lastDate = new Date(today.getFullYear(), today.getMonth() + 1, 0).getDate();

    for (let i = 0; i < firstDay; i++) {
        daysGrid.appendChild(document.createElement('div'));
    }

    for (let day = 1; day <= lastDate; day++) {
        const dayElement = document.createElement('div');
        dayElement.textContent = day;
        dayElement.style.padding = '10px';
        dayElement.style.border = '1px solid #ccc';
        dayElement.style.borderRadius = '5px';
        dayElement.style.textAlign = 'center';
        if (day === today.getDate()) {
            dayElement.style.backgroundColor = '#FFDE03';
            dayElement.style.fontWeight = 'bold';
        }
        daysGrid.appendChild(dayElement);
    }

    calendar.appendChild(daysGrid);
}

document.addEventListener('DOMContentLoaded', () => {
    createCalendar('calendar');
});
*/
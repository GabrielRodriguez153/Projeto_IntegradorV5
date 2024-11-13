async function fetchData() {
    const response = await fetch('/data');
    const chartData = await response.json();
    return chartData;
}

async function createChart() {
    const data = await fetchData();

    const ctx = document.getElementById('chart').getContext('2d');
    new Chart(ctx, {
        type: 'bar',
        data: data,
        options: {
            responsive: true,
            maintainAspectRatio: false
        }
    });
}

createChart();


// Gráfico de Pizza para Nível de Infestação
const ctxPizza = document.getElementById('graficoPizza').getContext('2d');
const graficoPizza = new Chart(ctxPizza, {
    type: 'pie',
    data: {
        labels: ['Alto', 'Médio', 'Baixo'],
        datasets: [{
            data: [40, 35, 25], // Quantidade ou percentual de cada nível
            backgroundColor: ['#FF6B6B', '#FFD93D', '#6BCB77'],
            hoverOffset: 4
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: {
                position: 'top',
            },
            title: {
                display: true,
            }
        }
    }
});

// Gráfico de Barras para Localizações
const ctxBarra = document.getElementById('graficoBarra').getContext('2d');
const graficoBarra = new Chart(ctxBarra, {
    type: 'bar',
    data: {
        labels: ['Região Norte', 'Região Sul', 'Região Leste', 'Região Oeste'],
        datasets: [{
            data: [15, 25, 10, 20], // Quantidade de detecções por região
            backgroundColor: ['#4CAF50', '#2196F3', '#FF9800', '#F44336'],
            borderColor: ['#4CAF50', '#2196F3', '#FF9800', '#F44336'],
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        scales: {
            y: {
                beginAtZero: true,
                title: {
                    display: true,
                    text: 'Número de Detecções'
                }
            },
            x: {
                title: {
                    display: true,
                    text: 'Localização'
                }
            }
        },
        plugins: {
            legend: {
                position: 'top',
            },
            title: {
                display: true,
            }
        }
    }
});

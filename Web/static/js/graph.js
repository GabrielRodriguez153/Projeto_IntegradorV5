document.addEventListener('DOMContentLoaded', () => {
  fetch('/dados-grafico')
    .then(response => response.json())
    .then(data => {
      // Atualize os labels e datasets do gráfico com os dados recebidos
      const ctx = document.getElementById('myChart').getContext('2d');
      const myChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: data.labels, // Labels dinâmicos das localizações
          datasets: [
            {
              type: 'bar',
              data: data.data, // Quantidade de plantações
              backgroundColor: '#1a5319'
            },
          ]
        },
        options: {
          responsive: true,
          plugins: {
            legend: {
              display: false,
            },
          },
          scales: {
            y: {
              beginAtZero: true
            }
          }
        }
      });
    })
    .catch(error => {
      console.error('Erro ao carregar os dados do gráfico:', error);
    });
});

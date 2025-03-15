document.addEventListener('DOMContentLoaded', () => {
  fetch('/dados-grafico')
    .then(response => response.json())
    .then(data => {
      const ctx = document.getElementById('myChart').getContext('2d');
      const myChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: data.labels, 
          datasets: [
            {
              type: 'bar',
              data: data.data, 
              backgroundColor: '#5bc781'
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




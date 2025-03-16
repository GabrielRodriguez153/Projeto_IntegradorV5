const btnFiltrar = document.getElementById('applyFilter');
    const selectRegion = document.getElementById('regionFilter');
    
    const totalMudasElem = document.getElementById('totalMudas');
    const casosAntracnoseElem = document.getElementById('casosAntracnose');
    const statusRiscoElem = document.getElementById('statusRisco');

    const ctx = document.getElementById('myChart').getContext('2d');
    const myChart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: [],
        datasets: [{
          label: 'Total de Plantações',
          data: [],
          backgroundColor: '#77d999',
        }]
      },
      options: {}
    });

    function updateChart(grafico_dados) {
      const labels = grafico_dados.map(item => item._id);
      const values = grafico_dados.map(item => item.totalPlantacoes);
      myChart.data.labels = labels;
      myChart.data.datasets[0].data = values;
      myChart.update();
    }

    btnFiltrar.addEventListener('click', () => {
      event.preventDefault();
      const region = selectRegion.value;
      fetch(`/api/data_by_region?region=${encodeURIComponent(region)}`)
        .then(response => response.json())
        .then(data => {
          if(data.error) {
            console.error("Erro na API:", data.error);
            return;
          }
    
          totalMudasElem.textContent = data.total;
          casosAntracnoseElem.textContent = data.hectares_afetados;
          statusRiscoElem.textContent = data.nivel_severidade;
      
          updateChart(data.grafico_dados);
        })
        .catch(err => {
          console.error('Erro ao buscar dados:', err);
        });
    });
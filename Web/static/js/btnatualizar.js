document.getElementById('btnAtualizar').addEventListener('click', function(e) {
  e.preventDefault();
  fetch('/api/home')
    .then(res => res.json())
    .then(data => {
      document.querySelector('#ultimaAtualizacao .valor').textContent = data.ultimaAtualizacao;
      document.querySelector('#statusGeral .valor').textContent = data.statusGeral;
      document.querySelector('#totalCasos .valor').textContent = data.totalCasos + ' Casos';
    })
    .catch(err => {
      console.error('Erro ao buscar dados:', err);
    });
});
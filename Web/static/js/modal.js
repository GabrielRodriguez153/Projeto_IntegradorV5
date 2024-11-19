// Abrir o modal
document.querySelectorAll(".btn-editar").forEach((button) => {
  button.addEventListener("click", function () {
    const modal = document.getElementById("editModal");
    const row = this.closest("tr");
    document.getElementById("edit-id").value = button.getAttribute("data-id");
    document.getElementById("edit-data-deteccao").value =
      row.cells[0].textContent.trim();
    document.getElementById("edit-localizacao").value =
      row.cells[1].textContent.trim();
    document.getElementById("edit-nivel-infestacao").value =
      row.cells[2].textContent.trim();
    document.getElementById("edit-status-pupunheira").value =
      row.cells[3].textContent.trim();
    document.getElementById("edit-observacoes").value =
      row.cells[4].textContent.trim();
    document.getElementById("edit-proprietario").value =
      row.cells[5].textContent.trim();

    modal.style.display = "flex";
  });
});

document.getElementById("closeModal").addEventListener("click", function () {
  document.getElementById("editModal").style.display = "none";
});

window.addEventListener("click", function (e) {
  const modal = document.getElementById("editModal");
  if (e.target === modal) {
    modal.style.display = "none";
  }
});

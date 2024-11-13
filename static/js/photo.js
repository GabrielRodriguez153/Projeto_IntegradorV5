function loadFile(event) {
    const profilePic = document.querySelector(".mini-photo");
    const file = event.target.files[0];

    if (file) {
        profilePic.style.backgroundImage = `url(${URL.createObjectURL(file)})`;
        profilePic.classList.add("has-image");  // Esconde o +
    }
}
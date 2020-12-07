function changeLikeColor(index) {
    const likeBtn =  document.getElementById("likeBtn-" + index );
    likeBtn.style.color = likeBtn.style.color === "black" ? "orange" : "black";
}
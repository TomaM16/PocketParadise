let heart = document.querySelectorAll('.heart');
heart.forEach(element => {
    element.addEventListener('click', () =>{
        let i = document.createElement('i');
        i.className = "fas fa-heart";
        i.style.color = "rgb(216, 16, 16)";
        element.textContent = "";
        element.appendChild(i)
    })
});



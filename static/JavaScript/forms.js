let clear = document.getElementById('clear');
let send = document.getElementById('send');

let email = document.getElementById('email');
let title = document.getElementById('title');
let message = document.getElementById('message');

let emailTo = document.getElementById('emailTo');
let emails = document.querySelectorAll('.col-4 ul li');

send.addEventListener('click', () =>{
    window.location.reload()
    alert('Sent Successful');
});

let form = document.getElementById('form');

emails.forEach(element =>{
    element.addEventListener('mouseover', () =>{
        element.className = "list-group-item bg-white text-dark border-light pointer"
    });
    element.addEventListener('mouseout', () =>{
        element.className = "list-group-item bg-transparent text-white border-light"
    });
});

emails[0].addEventListener('click', () =>{
    emailTo.value = emails[0].textContent;
    form.setAttribute('action', "https://script.google.com/macros/s/AKfycbypBvWHrzqYlHQrenEvXFNhL2yU6MwkkPz0sZvul8R1oFyMBR7z/exec");
});
emails[1].addEventListener('click', () =>{
    emailTo.value = emails[1].textContent;
    form.setAttribute('action', "https://script.google.com/macros/s/AKfycbypFiwpqQz6cxRwh-jBU6rokK4jqQC1_MTGv6Mg_2Pt-QREMew/exec");
});






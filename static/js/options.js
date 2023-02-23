let options = document.getElementById("options");
let options_form = document.getElementById("options_form")
let start_form = document.getElementById("start_form")

function openOptions(){
    options.style.visibility='visible';
}

function closeOptions(){
    options.style.visibility='hidden';
}

function startQuiz(){
    start_form.submit();
}



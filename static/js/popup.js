let input = document.getElementById("answer");
let guess_form = document.getElementById("guess");
let wrong = document.getElementById("wrong");
let right = document.getElementById("right");
let okay_btn = document.getElementById("okay");

function openRight(){
    right.style.visibility='visible';
    setTimeout(closeRight, 500);
}

function closeRight(){
    right.style.visibility = 'hidden';
    guess_form.setAttribute("onSubmit", "");
    guess_form.submit();
}

function openWrong(){
    wrong.style.visibility='visible';
}

function closeWrong(){
    wrong.style.visibility = 'hidden';
    guess_form.setAttribute("onSubmit", "");
    guess_form.submit();
}

function checkAnswer(answer,real_answer){
    var Answer = answer.trim();
    var Real_answer = real_answer;
    if (Answer == Real_answer || Answer == Real_answer.toLowerCase()){
        openRight();
    } else{
        openWrong();
        input.autofocus=false;
        okay_btn.focus();
    }
}
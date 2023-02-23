let input = document.getElementById("answer");
let guess_form = document.getElementById("guess");
let wrong = document.getElementById("wrong");
let right = document.getElementById("right");

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
    setTimeout(closeWrong, 500);
}

function closeWrong(){
    wrong.style.visibility = 'hidden';
}

function checkAnswer(answer,real_answer){
    var Answer = answer.trim();
    var Real_answer = real_answer;
    if (Answer == Real_answer || Answer == Real_answer.toLowerCase()){
        openRight();
    } else{
        openWrong();
    }
}
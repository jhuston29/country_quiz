import os, random, math
from flask import Flask, render_template, url_for, request, redirect
from main import txt_to_list, get_current_datetime, get_final_time, get_current_a, check_answer, divideList, timer, getMC_choices, removeDups

directory = os.getcwd()
input_file = "countries_capitals.txt"
file_path = os.path.join(directory, input_file)
retry = False;
game_over = False;

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def home():
    global countries_capitals, final_date, final_time, clock_display, switch, hide_name, divide, retry, game_over, clock_display, option1, option2, option3, option4, option5, title, start_time, type, full_list, index, quiz_len, correct_answers, choice1, choice2, choice3, choice4
    if not retry:
        option1 = request.form.get('region');
        option2 = request.form.get('time');
        option3 = request.form.get('slider_checkbox');
        option4 = request.form.get('hide_checkbox');
        option5 = request.form.get('type');
    if option1 != "All":
        divide = True;
    else:
        divide = False;
    if option2 == "unlimited" or option2 == None:
        clock_display = "false";
        final_time = 0;
    else:
        clock_display = "true";
        final_date = get_current_datetime();
        final_time = get_final_time(float(option2), final_date);
    if option3 == "on":
        switch = True;
        title = "Country";
    else:
        switch = False;
        title = "Capital";
    if option4 == "on":
        hide_name = "True";
    else:
        hide_name = "False";

    if "start" in request.form or retry:
        retry = False;
        game_over = False;
        index = 1;
        correct_answers = 0;
        countries_capitals = txt_to_list(file_path)
        full_list = countries_capitals
        if divide:
            countries_capitals = divideList(countries_capitals, option1)
        if option1 == "All":
            countries_capitals = removeDups(countries_capitals)
        random.shuffle(countries_capitals)
        quiz_len = len(countries_capitals)
        start_time = timer();
        return redirect(url_for("quiz"))
    return render_template('start.html')

@app.route("/Quiz")
def quiz():
    global index, choice1, choice2, choice3, choice4, quiz_len, correct_answers, percentage, elapsed_time, countries_capitals, game_over, check_time, clock_display
    check_time = timer()
    if clock_display == "true":
        if math.floor(check_time-start_time) >= math.floor(float(option2)*60):
            game_over = True
    if len(countries_capitals) == 0 or game_over:
        #print(correct_answers,'/',quiz_len)
        print(correct_answers,'/',index-1) #Correct answers out of attempted questions
        percentage = round(correct_answers/quiz_len * 100, 1);
        print(percentage)
        end_time = timer();
        elapsed_time = math.floor(end_time - start_time);
        return redirect(url_for("finished"))
    if option5 == "MC" and index == 1:
        choice1, choice2, choice3, choice4 = getMC_choices(full_list, switch)
    question = countries_capitals[0]
    current_q, current_a, region = question[0], question[1], question[2]
    if switch:
        current_q = question[1]
        current_a = question[0]
    index += 1;
    print(f"Current Question: {index-1}")
    if option5 == "MC":
        if current_a != choice1 and current_a != choice2 and current_a != choice3 and current_a != choice4:
            int = random.randint(1,4)
            if int == 1:
                choice1 = current_a
            if int == 2:
                choice2 = current_a
            if int == 3:
                choice3 = current_a
            if int == 4:
                choice4 = current_a
    if option5 == "MC":
        return render_template('index_MC.html', question=current_q, answer=current_a, date=final_time, clock_display=clock_display,
                               hide=hide_name, title=title, choice1=choice1, choice2=choice2, choice3=choice3, choice4=choice4, index=index-1, quiz_len=quiz_len)
    else:
        return render_template('index_FTB.html', question=current_q, answer=current_a, date=final_time, clock_display=clock_display,
                               hide=hide_name, title=title, index=index-1, quiz_len=quiz_len)

@app.route("/Quiz", methods=['GET', 'POST'])
def get_input():
    guess = request.form.get('answer')
    if guess != None:
        guess = guess.strip()
    return compare(guess)

def compare(guess):
    global choice1, choice2, choice3, choice4, correct_answers, countries_capitals, game_over, check_time, start_time
    current_answer = get_current_a(countries_capitals, switch)
    is_correct = check_answer(current_answer, guess)
    countries_capitals.pop(0)
    if is_correct:
        correct_answers +=1
    if option5 == "MC":
        choice1, choice2, choice3, choice4 = getMC_choices(full_list, switch)
    #print(f"Correct Answers: {correct_answers}")
    return quiz()

@app.route("/Quiz/Results", methods=['GET', 'POST'])
def finished():
    global elapsed_time, retry, check_time, correct_answers, quiz_len, percentage
    if "retry" in request.form:
        retry = True
        del check_time
        return redirect(url_for("home"))
    return render_template('finished.html', elapsed_time=elapsed_time, correct_answers=correct_answers, quiz_len=quiz_len, percentage=percentage)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
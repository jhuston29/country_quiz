function getTimeRemaining(endtime) {
  const total = Date.parse(endtime) - Date.parse(new Date());
  const total_sec = Math.floor(total/1000);
  const seconds = Math.floor((total / 1000) % 60);
  const minutes = Math.floor((total / 1000 / 60) % 60);
  return {
    total,
    minutes,
    seconds,
    total_sec
  };
}

function initializeClock(id, endtime) {
  const clock = document.getElementById(id);
  const minutesSpan = clock.querySelector('.minutes');
  const secondsSpan = clock.querySelector('.seconds');

  function updateClock() {
    const t = getTimeRemaining(endtime);
    minutesSpan.innerHTML = ('0' + t.minutes).slice(-2);
    secondsSpan.innerHTML = ('0' + t.seconds).slice(-2);
    if (t.total_sec <= 30) {
      clock.style.color = 'red';
    }
    if (t.total_sec <= 0) {
      clearInterval(timeinterval);
      minutesSpan.innerHTML = '00'
      secondsSpan.innerHTML = '00'
      location.reload();
    }
  }

  updateClock();
  const timeinterval = setInterval(updateClock, 1000);
}

function StrToBool(clock_display_string){
    if (clock_display_string=="false"){
        return false
    }
    else{
        return true
    }
}

function checkClockDisplay(clock_display,stop_date){
    if (!clock_display) {
        const quiz_clock = document.getElementById("clockdiv")
        quiz_clock.style.visibility='hidden';
    }
    else{
    initializeClock("clockdiv", stop_date);
    }
}

from datetime import datetime

def get_final_time():
    d1 = '1970/1/1' #time start in JS function
    current_time = datetime.now()
    date1 = datetime.strptime(d1, "%Y/%m/%d")
    delta = current_time - date1
    total_sec = delta.total_seconds()
    return total_sec
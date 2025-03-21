from flask import Flask, render_template
import calendar

app = Flask(__name__, template_folder="templates")

# calendar
full_month = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]
s_months = [i[:3] for i in full_month]

week_list = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab', 'Dom']
week_day = [i[0] for i in week_list]

hours = ["{:02d}:00".format(i) for i in range(7, 22)]

# format the days and weeks
def get_calendar(mm,yy):
    cal = calendar.month(yy, mm).split("\n")[2:-1]
    dict_days = {i*3 + 1: i for i in range(7)}
    day_position = (cal[0].find('1'))
    first_day = dict_days[day_position]
    last_day = int(cal[-1].split(" ")[-1])

    day_check = 0
    list_cal = [[]]
    pair_day = []
    day = 1
    i = 0

    while day <= last_day:
        if day_check == 0 and i < first_day:
            list_cal[-1].append({'day':' '})
            i += 1
        else:
            day_check = 1
            pair_day += [{
                'wkd': week_day[len(list_cal[-1]) % 7],
                'day': str(day),
                'full_wkd': week_list[len(list_cal[-1]) % 7],
                'month': mm
            }]
            list_cal[-1].append({'day':day, 'link': '{}-{}'.format( mm, day)})
            day += 1

    if len(list_cal[-1]) >= 7:
        list_cal.append([])

    return [s_months[mm-1], list_cal, pair_day, week_day]

cal = get_calendar(1, 2021)

# Render page
def render_page():
    template = render_template('base_planner.html')
    return template

# Route Decorator 
@app.route('/')
def home():
    with open('planner_template.html', 'w') as f:
        template_out = render_page()
        f.write(render_page())
    
    return template_out

if __name__ == '__main__':
    app.run()
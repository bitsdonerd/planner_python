from flask import Flask, render_template
import calendar

app = Flask(__name__)

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
def get_calendar(mm, yy):
    cal = calendar.month(yy, mm).split("\n")[2:-1]

    pos_primeiro_dia = (cal[0].find('1'))
    dict_position_to_days = {i*3 + 1: i for i in range(7)}
    first_day = dict_position_to_days[pos_primeiro_dia]
    last_day = int(cal[-1].split(" ")[-1])

    day_check = 0
    list_cal = [[]]
    pair_day = []
    day = 1
    i =0
    while day < last_day + 1:
        if day_check == 0 and i < first_day:
            list_cal[-1].append({'day': ' '})
            i += 1
        else:
            day_check = 1
            pair_day += [{
                'wkd': week_day[len(list_cal[-1])], 
                "day": str(day),
                'full_wkd': week_list[len(list_cal[-1])], 
                'month': mm
                }]
            list_cal[-1].append({'day': day, 'link': '{}-{}'.format(day, mm)})
            day += 1

        if len(list_cal[-1]) >= 7:
            list_cal.append([])
    
    return [s_months[mm - 1], list_cal, pair_day, week_day]


# Render page
def render_page():
    template = ''
    template += render_template('yearly.html', cal=[get_calendar(i, 2025) for i in range(1, 13)])
    template += render_template('daily.html', anchor="1-1")
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
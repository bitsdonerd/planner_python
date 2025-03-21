import pdfkit
import os 

options = {
    'page-size': 'A5',
    'margin-top': '0px',
    'margin-right': '0px',
    'margin-bottom': '0px',
    'margin-left': '0px',
    'orientation': 'Landscape',
    'encoding': "UTF-8",
    'dpi':80,
    'no-outline': True,
}

css = {
    'static/css/planner.css'
}

pdfkit.from_file('planner_template.html', 'planner.pdf', options=options, css=css)
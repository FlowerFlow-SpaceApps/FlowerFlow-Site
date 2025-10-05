from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/images')
def images():
    import os
    import regex as re
    images = []
    for filename in os.listdir('static/images'):
        # filename %Y-%m_{type}.png
        match = re.match(r'(\d{4}-\d{2})_(.+)\.png', filename)
        if not match:
            continue
        date, image_type = match.groups()
        if len(images) == 0 or images[-1]['date'] != date:
            images.append({'date': date, 'types': {}})
        images[-1]['types'][image_type] = filename

    images = sorted(images, key=lambda x: x['date'])
    return render_template('images.html', images=images)

@app.route('/about')
def about():
    return render_template('about.html')

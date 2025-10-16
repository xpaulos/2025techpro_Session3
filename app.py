from flask import Flask, render_template_string
import random
import colorsys

app = Flask(__name__)

def random_hue_color():
    # Generate a random hue (0-360 degrees)
    hue = random.random()  # 0.0 to 1.0
    saturation = 0.8  # High saturation for vibrant colors
    value = 0.9  # High value for bright colors
    
    # Convert HSV to RGB
    rgb = colorsys.hsv_to_rgb(hue, saturation, value)
    
    # Convert RGB (0-1) to hex
    r, g, b = [int(x * 255) for x in rgb]
    return "#{:02x}{:02x}{:02x}".format(r, g, b)

@app.route('/')
def show_squares():
    colors = [random_hue_color() for _ in range(30)]
    html = '''
    <html>
      <head>
        <style>
          .container {
            display: grid;
            grid-template-columns: repeat(6, 70px);
            gap: 10px;
            margin-top: 30px;
          }
          .square {
            width: 70px;
            height: 70px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 8px;
            border: 1px solid #aaa;
            font-size: 0.8em;
            color: #222;
          }
        </style>
      </head>
      <body>
        <h2>Random Colour Squares (Hex codes)</h2>
        <div class="container">
          {% for color in colors %}
            <div class="square" style="background-color: {{color}};">
              {{color}}
            </div>
          {% endfor %}
        </div>
      </body>
    </html>
    '''
    return render_template_string(html, colors=colors)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

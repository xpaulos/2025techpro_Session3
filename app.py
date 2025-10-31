from flask import Flask, render_template_string
import json

app = Flask(__name__)

@app.route('/')
def squares():
    # 1. Define the list of fixed hex color codes
    colors = [
        "#FF5733", "#33FF57", "#3357FF", "#F1C40F", "#8E44AD",
        "#E67E22", "#2ECC71", "#3498DB", "#E74C3C", "#95A5A6",
        "#9B59B6", "#34495E", "#16A085", "#27AE60", "#FF0000",
        "#1ABC9C", "#D35400", "#C0392B", "#7F8C8D", "#F39C12",
        "#2C3E50", "#BDC3C7", "#7E57C2", "#5C6BC0", "#42A5F5",
        "#26A69A", "#66BB6A", "#FFEE58", "#FF7043", "#8D6E63"
    ]

    # 2. Load the texts from the config.json file
    try:
        with open('config.json') as f:
            config = json.load(f)
        texts = config.get('texts', [])
    except FileNotFoundError:
        texts = ["Config file not found"] * 30

    # 3. Combine colors and texts into pairs for easier templating
    #    The zip function pairs the first color with the first text, and so on.
    squares_data = zip(colors, texts)

    # The HTML template now iterates through the combined 'squares_data'
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Colored Squares with Text</title>
        <style>
            body { font-family: sans-serif; background-color: #f4f4f9; display: flex; flex-direction: column; align-items: center; padding: 20px; }
            h1 { color: #333; }
            .container { display: flex; flex-wrap: wrap; width: 650px; justify-content: center; border: 1px solid #ccc; padding: 10px; background-color: #fff; border-radius: 8px; }
            .square { width: 100px; height: 100px; margin: 5px; border-radius: 4px; display: flex; align-items: center; justify-content: center; font-size: 14px; color: white; text-shadow: 1px 1px 2px black; text-align: center; padding: 5px; box-sizing: border-box; }
        </style>
    </head>
    <body>
        <h1>Squares with Colors and Text from Config</h1>
        <div class="container">
            {% for color, text in squares_data %}
            <div class="square" style="background-color: {{ color }};" title="{{ color }}">
                {{ text }}
            </div>
            {% endfor %}
        </div>
    </body>
    </html>
    """

    return render_template_string(html, squares_data=squares_data)

if __name__ == '__main__':
    app.run(debug=True)
import imgkit
from flask import request
from markupsafe import escape

app = Flask(__name__)

@app.post('/convert_to_image')
def convert_to_image():
    return "Hello"

def html_to_image(html_content, output_path, width=500, height=500):
    # Options for wkhtmltoimage
    options = {
        'format': 'png',
        'width': width,
        'height': height,
        'encoding': "UTF-8",
        'quality': '100'
    }
    # Convert HTML to image
    imgkit.from_string(html_content, output_path, options=options)
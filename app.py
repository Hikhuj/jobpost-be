from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Allow request from the FE
# In case does not work as expected, uncomment this line
# CORS(app, resources={r"/text_to_image": {"origins": "http://localhost:8000"}})
CORS(app)

# API initial
@app.route('/', methods=['GET'])
def home():
    greetings = 'Hello, world!'
    if not greetings:
        abort(404, description="Greetings not found")
    return jsonify({"message": greetings})

@app.route('/text_to_image', methods=['GET'])
def text_to_image(data, option=1):
    if not data:
        abort(404, description="Data not send")
    content = request.json
    print(content['data'])
    html_to_image(request.args)
    return jsonify({"message": "Access granted"})


def html_to_image():
    # Setting options to set new image required
    options = {
        'format': 'png',
        'width': width,
        'height': height,
        'encoding': 'UTF-8',
        'quality': '100',
    }

    # Convert HTML to image
    imgkit.from_string(html_content, output_path, options=options)

def generate_html(requirements, job_description, recruiter_contact):
    html_content = f"""
    <html>
        <head>
            <style media="screen,print">
                body {{
                    background-image: url('{background_image}');
                }}
                #g-Positions-box ,
                #g-Positions-box .g-artboard {{
                    margin:0 auto;
                }}
                #g-Positions-box p {{
                    margin:0;
                }}
                #g-Positions-box .g-aiAbs {{
                    position:absolute;
                }}
                #g-Positions-box .g-aiImg {{
                    position:absolute;
                    top:0;
                    display:block;
                    width:100% !important;
                }}
                #g-Positions-box .g-aiSymbol {{
                    position: absolute;
                    box-sizing: border-box;
                }}
                #g-Positions-box .g-aiPointText p {{ white-space: nowrap; }}
                #g-Positions-Mesa_de_trabajo_1 {{
                    position:relative;
                    overflow:hidden;
                }}
                #g-Positions-Mesa_de_trabajo_1 p {{
                    font-weight:regular;
                    line-height:24px;
                    height:auto;
                    opacity:1;
                    letter-spacing:0em;
                    font-size:20px;
                    text-align:left;
                    color:rgb(0,0,0);
                    text-transform:none;
                    padding-bottom:0;
                    padding-top:0;
                    mix-blend-mode:normal;
                    font-style:normal;
                    position:static;
                }}
                #g-Positions-Mesa_de_trabajo_1 .g-pstyle0 {{
                    font-weight:500;
                    line-height:75px;
                    height:75px;
                    letter-spacing:-0.05em;
                    font-size:89px;
                }}
                #g-Positions-Mesa_de_trabajo_1 .g-pstyle1 {{
                    font-weight:500;
                    line-height:75px;
                    height:75px;
                    letter-spacing:-0.05em;
                    font-size:89px;
                    color:rgb(255,255,255);
                }}
                #g-Positions-Mesa_de_trabajo_1 .g-pstyle2 {{
                    font-weight:500;
                    line-height:48px;
                    height:48px;
                    font-size:40px;
                    color:rgb(247,240,240);
                }}
                #g-Positions-Mesa_de_trabajo_1 .g-pstyle3 {{
                    font-weight:700;
                    height:24px;
                }}
                #g-Positions-Mesa_de_trabajo_1 .g-pstyle4 {{
                    font-weight:500;
                    height:24px;
                    width:800px;
                }}
                #g-Positions-Mesa_de_trabajo_1 .g-cstyle0 {{
                    color:rgb(0,0,0);
                }}
                #g-Positions-Mesa_de_trabajo_1 .g-cstyle1 {{
                    font-weight:700;
                }}
            </style>
        </head>
        <body>
            <div id="g-Positions-box" class="ai2html">
                <div id="g-Positions-Mesa_de_trabajo_1" class="g-artboard" style="max-width: 1080px;max-height: 1080px" data-aspect-ratio="1" data-min-width="0">
            <div style="padding: 0 0 100% 0;"></div>
                <img id="g-Positions-Mesa_de_trabajo_1-img" class="g-Positions-Mesa_de_trabajo_1-img g-aiImg" alt="" src="Positions-Mesa_de_trabajo_1.jpg"/>
                <div id="g-ai0-1" class="g-Propuesta_2 g-aiAbs g-aiPointText" style="top:8.7412%;margin-top:-81.4px;left:4.0679%;width:504px;">
                    <p class="g-pstyle0">WE ARE</p>
                    <p class="g-pstyle1">LOOKING<span class="g-cstyle0"> FOR</span></p>
                </div>
                <div id="g-ai0-2" class="g-Propuesta_2 g-aiAbs g-aiPointText" style="top:21.7414%;margin-top:-26.8px;left:5.0612%;width:659px;">
                    <p class="g-pstyle2">Sr. Full Stack Engineer (Angular/.Net)</p>
                </div>
                <div id="g-ai0-3" class="g-Propuesta_2 g-aiAbs g-aiPointText" style="top:48.7644%;margin-top:-181.7px;left:32.8452%;width:730px;">
                    <p class="g-pstyle3">Requirements</p>
                    <p>&nbsp;</p>
                    <p class="g-pstyle4">{requirements}</p>
                    <p>&nbsp;</p>
                    <p class="g-pstyle3">Job Description</p>
                    <p>&nbsp;</p>
                    <p class="g-pstyle4">{job_description}</p>
                    <p>&nbsp;</p>
                        <p class="g-pstyle3">Recruiter Contact</p>
                    <p>&nbsp;</p>
                    <p class="g-pstyle4">{recruiter_contact}</p>
                    <p>&nbsp;</p>
                </div>
            </div>
        <body>
    </html>
    """

    return html_content

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)



####
Varios

# and two plain text parameters and transform it into an image of 500x500 pixels and return this image to user.

Additionals

<<<<<<< HEAD
import os
import imgkit
from flask import Flask, jsonify, request, json
=======
from flask import Flask, jsonify, request
>>>>>>> 40c6c097fa65cdeee6d20c0f6f2375899c01853e
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

<<<<<<< HEAD
# allow request from the FE 
CORS(app, resources={r"/data_to_image": {"origins": "http://127.0.0.1:5000"}})

# App entry point
@app.route("/")
def home():
    return jsonify({"message": "Hello, world!"})

# Send the data from form
@app.route("/data_to_image", methods=["POST"])
def data_to_image():
    try:
        if not request.is_json:
            return jsonify({"error": "Request must be in JSON format"}), 400

        # If ok lets parse the JSON data
        data = request.get_json()
        job_title = data["job_title"]
        job_description = data["job_description"]
        requirements = data["requirements"]
        recruiter_contact = data["recruiter_contact"]

        if not job_title or not job_description or not requirements or not recruiter_contact:
            return jsonify({"error": "Not all parameters were sent"}), 400

        # Output path for the image we export
        output_path = "output.png"


        # Make call with parameters to main function
        response = converter_data_to_image(output_path, job_title, job_description, requirements, recruiter_contact)

        # Return answer
        # return send_file(output_path, mimetype="image/png")

        # We are going to return a file or image to user
        return jsonify({"message": "All data ok"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

def converter_data_to_image(output_path, job_title, job_description, requirements, recruiter_contact):
    html_content = generate_html(job_title, job_description, requirements, recruiter_contact)
    return html_to_image(html_content, output_path, 500, 500)


def generate_html(job_title, job_description, requirements, recruiter_contact):
    """
    Generate HTML sting with different variables
    """
    return f"""
    <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    text-align: center;
                }}
                .section {{
                    margin: 20px;
                }}
            </style>
        </head>
        <body>
            <div class="section">
                <h1>We are hiring!</h1>
            </div>
            <div class="section">
                <h2>Job Title</h2>
                <p>{job_title}</p>
            </div>
            <div class="section">
                <h2>Job Description</h2>
                <p>{job_description}</p> b
                ''
            </div>
            <div class="section">
                <h2>Requirements</h2>
                <p>{requirements}</p>
            </div>
            <div class="section">
                <h2>Recruiter Contact</h2>
                <p>{recriter_contact}</p>
            </div>
        </body>
    </html>
    """

def html_to_image(html_content, output_path, width=1000, height=1000):
=======
# Allow request from the FE
# In case does not work as expected, uncomment this line
# CORS(app, resources={r"/text_to_image": {"origins": "http://localhost:8000"}})
CORS(app)

# API initial
@app.route('/', methods=['GET'])
def home():
    greetings = 'Hello, world!'
    if not greetings:
        abort(404, description="Greetings not found")
    return jsonify({"message": greetings})

@app.route('/text_to_image', methods=['GET'])
def text_to_image(data, option=1):
    if not data:
        abort(404, description="Data not send")
    content = request.json
    print(content['data'])
    html_to_image(request.args)
    return jsonify({"message": "Access granted"})


def html_to_image():
>>>>>>> 40c6c097fa65cdeee6d20c0f6f2375899c01853e
    # Setting options to set new image required
    options = {
        'format': 'png',
        'width': width,
        'height': height,
<<<<<<< HEAD
        'encoding': "UTF-8",
        'quality': '100'
    }

    # Convert HTML to Image
    imgkit.from_string(html_content, output_path, options=options)

=======
        'encoding': 'UTF-8',
        'quality': '100',
    }

    # Convert HTML to image
    imgkit.from_string(html_content, output_path, options=options)

def generate_html(requirements, job_description, recruiter_contact):
    html_content = f"""
    <html>
        <head>
            <style media="screen,print">
                body {{
                    background-image: url('{background_image}');
                }}
                #g-Positions-box ,
                #g-Positions-box .g-artboard {{
                    margin:0 auto;
                }}
                #g-Positions-box p {{
                    margin:0;
                }}
                #g-Positions-box .g-aiAbs {{
                    position:absolute;
                }}
                #g-Positions-box .g-aiImg {{
                    position:absolute;
                    top:0;
                    display:block;
                    width:100% !important;
                }}
                #g-Positions-box .g-aiSymbol {{
                    position: absolute;
                    box-sizing: border-box;
                }}
                #g-Positions-box .g-aiPointText p {{ white-space: nowrap; }}
                #g-Positions-Mesa_de_trabajo_1 {{
                    position:relative;
                    overflow:hidden;
                }}
                #g-Positions-Mesa_de_trabajo_1 p {{
                    font-weight:regular;
                    line-height:24px;
                    height:auto;
                    opacity:1;
                    letter-spacing:0em;
                    font-size:20px;
                    text-align:left;
                    color:rgb(0,0,0);
                    text-transform:none;
                    padding-bottom:0;
                    padding-top:0;
                    mix-blend-mode:normal;
                    font-style:normal;
                    position:static;
                }}
                #g-Positions-Mesa_de_trabajo_1 .g-pstyle0 {{
                    font-weight:500;
                    line-height:75px;
                    height:75px;
                    letter-spacing:-0.05em;
                    font-size:89px;
                }}
                #g-Positions-Mesa_de_trabajo_1 .g-pstyle1 {{
                    font-weight:500;
                    line-height:75px;
                    height:75px;
                    letter-spacing:-0.05em;
                    font-size:89px;
                    color:rgb(255,255,255);
                }}
                #g-Positions-Mesa_de_trabajo_1 .g-pstyle2 {{
                    font-weight:500;
                    line-height:48px;
                    height:48px;
                    font-size:40px;
                    color:rgb(247,240,240);
                }}
                #g-Positions-Mesa_de_trabajo_1 .g-pstyle3 {{
                    font-weight:700;
                    height:24px;
                }}
                #g-Positions-Mesa_de_trabajo_1 .g-pstyle4 {{
                    font-weight:500;
                    height:24px;
                    width:800px;
                }}
                #g-Positions-Mesa_de_trabajo_1 .g-cstyle0 {{
                    color:rgb(0,0,0);
                }}
                #g-Positions-Mesa_de_trabajo_1 .g-cstyle1 {{
                    font-weight:700;
                }}
            </style>
        </head>
        <body>
            <div id="g-Positions-box" class="ai2html">
                <div id="g-Positions-Mesa_de_trabajo_1" class="g-artboard" style="max-width: 1080px;max-height: 1080px" data-aspect-ratio="1" data-min-width="0">
            <div style="padding: 0 0 100% 0;"></div>
                <img id="g-Positions-Mesa_de_trabajo_1-img" class="g-Positions-Mesa_de_trabajo_1-img g-aiImg" alt="" src="Positions-Mesa_de_trabajo_1.jpg"/>
                <div id="g-ai0-1" class="g-Propuesta_2 g-aiAbs g-aiPointText" style="top:8.7412%;margin-top:-81.4px;left:4.0679%;width:504px;">
                    <p class="g-pstyle0">WE ARE</p>
                    <p class="g-pstyle1">LOOKING<span class="g-cstyle0"> FOR</span></p>
                </div>
                <div id="g-ai0-2" class="g-Propuesta_2 g-aiAbs g-aiPointText" style="top:21.7414%;margin-top:-26.8px;left:5.0612%;width:659px;">
                    <p class="g-pstyle2">Sr. Full Stack Engineer (Angular/.Net)</p>
                </div>
                <div id="g-ai0-3" class="g-Propuesta_2 g-aiAbs g-aiPointText" style="top:48.7644%;margin-top:-181.7px;left:32.8452%;width:730px;">
                    <p class="g-pstyle3">Requirements</p>
                    <p>&nbsp;</p>
                    <p class="g-pstyle4">{requirements}</p>
                    <p>&nbsp;</p>
                    <p class="g-pstyle3">Job Description</p>
                    <p>&nbsp;</p>
                    <p class="g-pstyle4">{job_description}</p>
                    <p>&nbsp;</p>
                        <p class="g-pstyle3">Recruiter Contact</p>
                    <p>&nbsp;</p>
                    <p class="g-pstyle4">{recruiter_contact}</p>
                    <p>&nbsp;</p>
                </div>
            </div>
        <body>
    </html>
    """

    return html_content
>>>>>>> 40c6c097fa65cdeee6d20c0f6f2375899c01853e

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)


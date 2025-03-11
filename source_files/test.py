import os
import imgkit

def generate_html(requirements, job_description, recruiter_contact, background_image):
    """
    Generate HTML sting with different variables
    """
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

def html_to_image(html_content, output_path, width=1000, height=1000):
    # Setting options to set new image required
    options = {
        'format': 'png',
        'width': width,
        'height': height,
        'encoding': "UTF-8",
        'quality': '100'
    }
    # Convert HTML to image
    imgkit.from_string(html_content, output_path, options=options)

# Example usage
if __name__ == "__main__":

    Requirements = """Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. 
    Aenean massa."""
    Job_description = "Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus."
    Recruiter_contact = """Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas 
    nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus."""

    script_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"Localizacion del proyecto {script_dir}")
    background_image = "img/template.png"

    html_content = generate_html(Requirements, Job_description, Recruiter_contact, background_image)

    output_image_path = os.path.join(script_dir, "output_image.png")

    html_to_image(html_content, output_image_path)

    print(f"Image saved to {output_image_path}")
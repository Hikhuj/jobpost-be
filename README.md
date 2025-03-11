# jobPosting_MS_BE

- Required to use Python v.3
- Create virtual ENV with venv (https://flask.palletsprojects.com/en/3.0.x/installation/)
    [code]python3 -m venv <directory>
    [code]python3 -m venv .venv (mostly common name)

- To start the Python Venv (two methods)
    [code]. .venv/bin/activate[/code]
    [code]source myvenv/bin/activate[/code]

- To deactivate, write "deactivate" on the project because any code you execute about python, will be executed outside too.
    [code]deactivate[/code]

- Install Flask micro web framework is the only dependency that you project requires.
    [code]python3 -m pip install Flask[/code]

- * You can try running the app with... and this will start the Web Server. This creates a server on port 8000.
    [code]python3 app.py[/code]

- Install the requirements with the command
    [code]pip install -r requirements.txt[/code]

- ** To run Flask App do
    [code]flask --app app run[/code]
    
- Run the app on debugg mode
    [code]flask --app app run --debug[/code]

* This method of initialize the Flask app is not recommended for development. There are sometimes where the code executes itself twice or other side-effects that we want to avoid.
** This method will allow to make the code independent of any external environment configurations. Plus, there is a lot of additionals that you can read [link]https://flask.palletsprojects.com/en/1.1.x/cli/[/link]

Para activar los ambientes virtuales de Python

https://python.land/virtual-environments/virtualenv

Activate pythong environment.

pip3 install Flask
pip3 install pillow imgkit
pip3 install flask-cors


To run application
python3 app.py

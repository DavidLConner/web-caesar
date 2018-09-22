from flask import Flask, request
from caesar import rotate_string


app = Flask(__name__)
app.config['DEBUG'] = True

form = """

<!DOCTYPE html>

<html>
    <head>
        <style>

            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
                
            }}

        </style>
    </head>

    <body>

    <form method='POST'>
        <label> Rotate by:
            <input type="text" name="rot" value='0'>
            
        </label>    
    
    <textarea type="text" name="Text" {0}>
    </textarea>

    <button type="submit" form="nameform" value="Submit">Submit Query</button>    


          
    </form>
    
    </body>
</html>  
    """

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=["POST"])

def encrypt():
    rot = int()
    text = ""
    return 'h1>rotate_string.format(text)</h1>'


 

app.run()
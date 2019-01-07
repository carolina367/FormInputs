from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    # found in ../templates/
    return render_template("main_page.html")

@app.route('/process_inputs', methods=['POST'])
def process_inputs():
    name = request.form.get('user_name', '')
    dropdown = request.form.get('reason_dropdown', '')
    select = request.form.get('officer_select', '')
    return render_template("main_page.html", input_data=dropdown,
                           output="You're a wizard %s." % name)

from flask import Flask, render_template, redirect, send_from_directory


app = Flask(__name__)

@app.route('/issue', methods=['GET'])
def issue_get():
    return render_template('issue.html')

if __name__ == '__main__':
    app.run(debug=True, port=541)
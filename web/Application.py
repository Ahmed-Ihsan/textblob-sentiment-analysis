from flask import Flask,jsonify,request
from flask import render_template
import ast
import webbrowser

app = Flask(__name__)
labels = ['positive', 'negative', 'neutral']
values = []

myfile = open("data.txt", "r")
myline = myfile.readline()
while myline:
    values.append(int(myline))
    myline = myfile.readline()
myfile.close()   

@app.route("/")
def get_chart_page():
        return render_template('chart.html', values=values, labels=labels)
@app.route('/json_data')
def refresh_graph_data():
        global labels, values
        print("labels now: " + str(labels))
        print("data now: " + str(values))
        return jsonify(sLabel=labels, sData=values)

if __name__ == "__main__":
        webbrowser.open_new('http://127.0.0.1:5000/')
        app.run()
                                               

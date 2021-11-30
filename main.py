import pandas as pd
import dataframe_image as dfi
from flask import Flask, redirect, url_for, render_template, request
from Convert import convertor

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def input_page():
    if request.method == "POST":
        q1 = request.form["q1"]
        q1_z = request.form["q1_z"]
        q1_o = request.form["q1_o"]
        q1_output = request.form["q1_output"]

        q2 = request.form["q2"]
        q2_z = request.form["q2_z"]
        q2_o = request.form["q2_o"]
        q2_output = request.form["q2_output"]

        q3 = request.form["q3"]
        q3_z = request.form["q3_z"]
        q3_o = request.form["q3_o"]
        q3_output = request.form["q3_output"]

        convertor(q1, q1_z, q1_o, q1_output, q2, q2_z, q2_o, q2_output, q3, q3_z, q3_o, q3_output)
        return '<img src="/static/mealy_machine.png">'
        #return redirect(url_for("generate", q1=q1, q1_z=q1_z, q1_o=q1_o, q1_output=q1_output, q2=q2, q2_z=q2_z, q2_o=q2_o, q2_output=q2_output, q3=q3, q3_z=q3_z, q3_o=q3_o, q3_output=q3_output))
     #   return redirect(url_for("user", usr=q1))
    return render_template("index.html")
    @app.route("/<usr>")
    #def generate(q1, q1_z, q1_o, q1_output, q2, q2_z, q2_o, q2_output, q3, q3_z, q3_o, q3_output):
     #   convertor(q1, q1_z, q1_o, q1_output, q2, q2_z, q2_o, q2_output, q3, q3_z, q3_o, q3_output)
      #  return '<img src="mealy_machine.png" alt="Mealy Machine">'
   # def ok():
    #    return "<h1>OK</h1>"
    def user(usr):
        return f"<h1>{usr}</h1>"

    if __name__=="__main__":
        app.run(debug=True)

# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# ---- YOUR APP STARTS HERE ----
# -- Import section --
# Renee Catanach and Aniruddha Pokhrel

print("testing push")
from flask import Flask
from flask import render_template
from flask import request
from model import capital_checker 

# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/results', methods = ['GET', 'POST'])
def results():
    answers = {"New York": request.form['New York'], "California": request.form['California'], "New Mexico": request.form['New Mexico'], "Florida": request.form['Florida'], "Michigan": request.form['Michigan']}
    corrects = capital_checker(answers)
    return render_template("results.html", corrects=corrects)
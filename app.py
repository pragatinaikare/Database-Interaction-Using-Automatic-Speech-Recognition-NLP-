from flask import Flask
from flask import Flask, flash, redirect, render_template, request
import os
import speech_recognition as sr
import subprocess
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

#ln2sql is a NLP tool to query a database in natural language. 
#The tool takes in input a database model and a sentence and translate the latter in a valid SQL statement able to query the input data model.
app = Flask(__name__)

@app.route("/")
def LoadHome():
    return render_template('SpeechToText.html')

@app.route('/Speech', methods=['GET', 'POST'])
def Speech():
    Output = ""#"Text: "
    df = ""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something:")
        audio = r.listen(source)
        print(audio)
    try:
        Output = Output + r.recognize_google(audio);
    except:
        pass;
    
    # Create your connection.
    cnx = sqlite3.connect('school.db')
    #df = pd.read_sql_query("SELECT * FROM student", cnx)    
    #df = subprocess.check_output('python -m ln2sql.main -d database_store/school.sql -l lang_store/english.csv -j output.json -i "' + Output + '"',stderr=subprocess.STDOUT,shell=True)
    Output = Output.lower()
    print("Speech 2 Text::",Output)
    try:
        #df = subprocess.check_output('python -m ln2sql.main -d ln2sql/database_store/school.sql -l lang_store/english.csv -i "' + Output + '"',stderr=subprocess.STDOUT,shell=True)
        df = subprocess.check_output('python -m ln2sql.main -d database_store/school.sql -l lang_store/english.csv -i "' + Output + '"',stderr=subprocess.STDOUT,shell=True)
        print(df)
        #df = subprocess.check_call('python -m ln2sql.main -d database_store/school.sql -l lang_store/english.csv -i "' + Output + '"',stderr=subprocess.STDOUT,shell=True)
    except subprocess.CalledProcessError as exc:
        print("Status : FAIL", exc.returncode, exc.output)
    else:
        print("Output: \n{}\n".format(df))
    print("========>",df,type(df))
    df = repr(df)
    df = df.replace(r"\r\n",r" ")
    df = df.replace(r"b",r"")
    df = df.replace(r'"',r"")
    df = df[:-1]
    df = df[1:]
    print("--####>",df)
    df1 = pd.read_sql_query(df, cnx) 
    return render_template('SpeechToText.html', Output = Output, OutputQuery = df, tables=[df1.to_html(classes='TableBody')], titles=df1.columns.values)

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=False,host='0.0.0.0', port=5001)



'''Average age of STUDENTS
Highest age of STUDENTS
Give me the list of STUDENTS whose name like MAHI
Give me the list of STUDENTS whose age is greater than 21'''
# Count of students
# age < 23
# aesc | desc
# age not 23
# distinct




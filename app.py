from flask import Flask, render_template
import pandas as pd
app = Flask(__name__)

table_df = pd.read_csv('templates/table.csv')
table2_df = pd.read_csv('templates/table2.csv')
app.config['static'] = '/image'

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/table1')
def table():
    return render_template('table.html')

@app.route('/table2')
def table2():
    return render_template('table2.html')

@app.route('/table-data')
def table_data():
    table_json = table_df.to_json(orient='records')
    return table_json
@app.route('/table2-data')
def table2_data():
    table2_json = table2_df.to_json(orient='records')
    return table2_json
if __name__ == '__main__':
    app.run(debug=True)

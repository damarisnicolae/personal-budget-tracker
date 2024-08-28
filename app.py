from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

try:
    connection = mysql.connector.connect(
        host = '127.0.0.1',
        user = 'damaris',
        password = 'damarisub',
        database = 'budgetTracker'
    )
    print("Connected to database successfully!")
except mysql.connector.Error as error:
        print(f"Database connection error: {error}")
        

@app.route('/transactions', methods=['GET'])
def get_transactions():
    
    cursor = connection.cursor()
    query = """SELECT * FROM Transactions"""
    cursor.execute(query)
    transactions = cursor.fetchall()
    
    return render_template('transactions.html', data = transactions)


@app.route('/postform', methods=['GET'])
def get_postform():
    render_template('postform.html')
    
    
@app.route('/editform/{id}', methods=['GET'])
def get_editform(id):
    
    cursor = connection.cursor()
    query = f"SELECT FROM Transactions WHERE ID={id}"
    cursor.execute(query)
    transaction = cursor.fetchone()
    
    return render_template('editform.html', data = transaction)


@app.route('/transactions', methods=['POST'])
def add_transactions():

    amount = request.form['amount']
    type = request.form['type']
    date = request.form['date']
    description = request.form['description']
    
    if type == "income" and amount.startswith('-') or type == "expense" and amount.startswith('+'):
        return "Error: put the correct type of amount, please!"
    
    cursor = connection.cursor()
    query = f"INSERT INTO Transactions (Amount, Type, Date, Description) VALUES ({amount}, {type}, {date}, {description})"
    cursor.execute(query)
    connection.commit()
    connection.close()
    return render_template('transactions.html')
    

@app.route('/transactions/{id}', methods=['PUT'])
def edit_transactions(id):

    amount = request.form['amount']
    type = request.form['type']
    date = request.form['date']
    description = request.form['description']
    
    if type == "income" and amount.startswith('-') or type == "expense" and amount.startswith('+'):
        return "Error: put the correct type of amount, please!"
    
    cursor = connection.cursor()
    query = f"UPDATE Transactions SET Amount = {amount}, Type = {type}, Date = {date}, Description = {description} WHERE ID = {id}"
    cursor.execute(query)
    connection.commit()
    connection.close()
    
    return render_template('transactions.html')


@app.route('/transactions/{id}', methods=['DELETE'])
def delete_transactions(id):
    
    cursor = connection.cursor()
    query = f"DELETE FROM Transactions WHERE ID = {id}"
    cursor.execute(query)
    connection.commit()
    connection.close()
    
    return render_template('transactions.html')


if __name__=='__main__': 
    app.run(host='0.0.0.0', port=5050, debug=True)

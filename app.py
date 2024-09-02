from flask import Flask, request, render_template, jsonify
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
    
    transactions_list = []
    for transaction in transactions:
        transactions_list.append({
            'id': transaction[0],
            'amount': transaction[1],
            'type': transaction[2],
            'date': transaction[3].strftime("%Y-%m-%d"),
            'description': transaction[4]
        })
    
    cursor.close()
    connection.close()
    
    return render_template('transactions.html', data = transactions_list)


@app.route('/summary', methods=['GET'])
def summary():
    
    cursor = connection.cursor()
    query = "SELECT SUM(Amount) FROM Transactions WHERE Type='income'"
    cursor.execute(query)
    income_sum = cursor.fetchone()[0]
    print(income_sum)
    print(type(income_sum))
    
    query2 = "SELECT SUM(Amount) FROM Transactions WHERE Type='expense'"
    cursor.execute(query2)
    expense_sum = cursor.fetchone()[0]
    
    balance = income_sum + expense_sum
    
    return render_template('summary.html', income_sum = income_sum, expense_sum = expense_sum, balance = balance)


@app.route('/postform', methods=['GET'])
def get_postform():
    return render_template('postform.html')
    
    
@app.route('/editform/{id}', methods=['GET'])
def get_editform(id):
    
    cursor = connection.cursor()
    query = f"SELECT FROM Transactions WHERE ID={id}"
    cursor.execute(query)
    transaction = cursor.fetchone()
    
    return render_template('editform.html', transaction = transaction)


@app.route('/transactions', methods=['POST'])
def add_transactions():

    amount = request.form['amount']
    type = request.form['type']
    date = request.form['date']
    description = request.form['description']
    
    if type == "income" and amount.startswith('-') or type == "expense" and amount.startswith('+'):
        return "Error: put the correct type of amount, please!"
    
    cursor = connection.cursor()
    query = f"""INSERT INTO Transactions (Amount, Type, Date, Description) VALUES ({amount}, {type}, {date}, {description})"""
    cursor.execute(query)
    connection.commit()
    cursor.close()
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

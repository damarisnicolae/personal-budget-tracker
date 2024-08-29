# Personal Budget Tracker

## Overview

This project includes a Python-based API, a SQL schema for database structure, and a frontend implemented in HTML and JavaScript. It is designed to handle transactions data, allowing users to view and modify transaction records.

## Technologies Used

- **Backend**: Python with Flask
- **Database**: SQL (e.g. MySQL)
- **Frontend**: HTML, JavaScript
- **Database Management**: SQLite (or any other SQL database you use)

## Project Structure

- `app.py` - The main Python file containing the Flask API.
- `schema.sql` - The SQL schema file for setting up the database.
- `templates/` - Directory containing HTML files.

## Prerequisites

Before running the project, ensure you have the following installed:
- Python 3.x
- pip (Python package installer)
- A SQL database (SQLite, PostgreSQL, MySQL, etc.)

## Run the API Server

Start the Flask Server:
- Ensure you're in the directory containing app.py.
- Run the Flask application:
- **python3 app.py**

## Usage

- **Viewing Transactions:**
Access http://127.0.0.1:5050/transactions to view a list of transactions.

- **Updating Transactions:**
Use the frontend form to update transactions. The form sends data to the backend via a PUT request to the /transactions/{id} endpoint.

- **Adding Transactions:**
Use the frontend form to add transactions. The form sends data to the backend via a POST request to the /transactions endpoint.

- **Deleting Transactions:**
Use the frontend button to delete transactions. The form sends data to the backend via a DELETE request to the /transactions/{id} endpoint.

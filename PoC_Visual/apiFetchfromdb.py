import pyodbc
from flask import Flask, request, render_template

app = Flask(__name__)

# # Connection details
# server = "10.100.13.56"
# database = "ESBDB_PPD"
# username = "dbadmin"
# password = "Oliya.20"

# Connection details
server = "10.100.7.55"
database = "ESBDB_PROD"
username = "dbadmin"
password = "Prod-Oliya.20"

# Function to establish a connection to the database
def get_connection():
    connection = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password + ';Encrypt=yes;TrustServerCertificate=yes;')
    return connection

# API endpoint to retrieve records corresponding to a specific column value
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/records", methods=["GET"])
def get_records():
    # Get the value of the column
    payload = request.args.get("Payload")
    from_timestamp = request.args.get("from_timestamp")
    to_timestamp = request.args.get("to_timestamp")

    # Establish a connection to the database
    connection = get_connection()

    # Create a cursor to execute SQL statements
    cursor = connection.cursor()

    # Execute the SELECT statement
    cursor.execute(f"SELECT * FROM DB_LOGGING WHERE Payload LIKE '%{payload}%' AND TimeStamp BETWEEN '{from_timestamp}' AND '{to_timestamp}'")

    # Store the description
    description = cursor.description

    # Fetch the results
    results = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    connection.close()

    # Return the results as a JSON object
    return {"records": [dict(zip([column[0] for column in description], row)) for row in results]}

@app.route("/records/<string:unique_id>", methods=["GET"])
def get_record_by_unique_id(unique_id):
    # Establish a connection to the database
    connection = get_connection()

import pyodbc
from flask import Flask, request, render_template

app = Flask(__name__)

# # Connection details
# server = "10.100.13.56"
# database = "ESBDB_PPD"
# username = "dbadmin"
# password = "Oliya.20"

# Connection details
server = "10.100.7.55"
database = "ESBDB_PROD"
username = "dbadmin"
password = "Prod-Oliya.20"

# Function to establish a connection to the database
def get_connection():
    connection = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password + ';Encrypt=yes;TrustServerCertificate=yes;')
    return connection

# API endpoint to retrieve records corresponding to a specific column value
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/records", methods=["GET"])
def get_records():
    # Get the value of the column
    payload = request.args.get("Payload")
    from_timestamp = request.args.get("from_timestamp")
    to_timestamp = request.args.get("to_timestamp")

    # Establish a connection to the database
    connection = get_connection()

    # Create a cursor to execute SQL statements
    cursor = connection.cursor()

    # Execute the SELECT statement
    cursor.execute(f"SELECT * FROM DB_LOGGING WHERE Payload LIKE '%{payload}%' AND TimeStamp BETWEEN '{from_timestamp}' AND '{to_timestamp}'")

    # Store the description
    description = cursor.description

    # Fetch the results
    results = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    connection.close()

    # Return the results as a JSON object
    return {"records": [dict(zip([column[0] for column in description], row)) for row in results]}

@app.route("/records/<string:unique_id>", methods=["GET"])
def get_record_by_unique_id(unique_id):
    # Establish a connection to the database
    connection = get_connection()

    # Create a cursor to execute SQL statements
    cursor = connection.cursor()

    # Execute the SELECT statement
    cursor.execute(f"SELECT * FROM DB_LOGGING WHERE UniqueId = '{unique_id}'")

    # Store the description
    description = cursor.description

    # Fetch the result
    result = cursor.fetchone()

    # Close the cursor and connection
    cursor.close()
    connection.close()

    # Return the result as a JSON object
    if result is None:
        return {"error": "Record not found"}
    else:
        return {"record": dict(zip([column[0] for column in description], result))}

if __name__ == "__main__":
    app.run(debug=True)


if __name__ == "__main__":
    app.run(debug=True)

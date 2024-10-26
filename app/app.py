from flask import Flask, render_template, request, redirect, url_for
import boto3
from botocore.exceptions import ClientError

app = Flask(__name__)

# Configuración de la conexión a DynamoDB local
dynamodb = boto3.resource(
    'dynamodb',
    endpoint_url="http://dynamodb-local:8000",
    region_name="us-west-2",
    aws_access_key_id="DUMMYIDEXAMPLE",
    aws_secret_access_key="DUMMYEXAMPLEKEY"
)

# Nombre de la tabla
table_name = "TestTable"

# Página para ver todos los elementos
@app.route('/')
def index():
    table = dynamodb.Table(table_name)
    try:
        response = table.scan()
        items = response.get('Items', [])
        return render_template('index.html', items=items)
    except ClientError as e:
        return f"Error: {e}"

# Página para agregar un nuevo elemento
@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        id = request.form['id']
        nombre = request.form['nombre']
        valor = request.form['valor']
        table = dynamodb.Table(table_name)
        item = {'id': id, 'nombre': nombre, 'valor': valor}
        try:
            table.put_item(Item=item)
            return redirect(url_for('index'))
        except ClientError as e:
            return f"Error: {e}"
    return render_template('add_item.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

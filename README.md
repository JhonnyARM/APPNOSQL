## Introduction

![alt text](/img/Diagrama1.jpeg)

### DynamoDB

DynamoDB is a fully managed NoSQL database service provided by Amazon Web Services (AWS). It is designed to handle large amounts of data and provides fast and predictable performance with seamless scalability.

- **Managed Service:** DynamoDB is fully managed, meaning that AWS handles operational tasks such as hardware provisioning, setup, configuration, and backups.

- **NoSQL Database:** It is a NoSQL database, allowing for flexible data models and horizontal scaling, making it suitable for applications with varying data structures.

- **Performance:** DynamoDB offers single-digit millisecond response times, ideal for applications that require high-speed data access.

- **Scalability:** The service can automatically scale up and down to accommodate varying workloads, allowing applications to handle large volumes of data and traffic without manual intervention.

- **Global Tables:** DynamoDB supports global tables, enabling multi-region, fully replicated tables that provide low-latency access to data across different geographical locations.

- **Integration with AWS Services:** DynamoDB integrates seamlessly with other AWS services such as Lambda, API Gateway, and S3, allowing for the development of complex applications in the cloud.

- **Security and Compliance:** It provides built-in security features, including encryption at rest and in transit, and supports AWS Identity and Access Management (IAM) for fine-grained access control.

### Running Local DynamoDB

We have to go to this URL and download the zip
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html

After you download the archive, extract the contents and copy the extracted directory to a location of your choice.
![alt text](/img/image.png)
To start DynamoDB on your computer, open a command prompt window, navigate to the directory where you extracted DynamoDBLocal.jar, and enter the following command.

```bash
java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb
```

![alt text](/img/image-1.png)

### Code Example

Now we are going to test a simple web application, using python and boto3 libraries with flask.

#### Requirements

- Python
- Boto3, Flask
- Docker
- DynamoDBLocal files

#### Python Code

- Project structure

```
EjemploDynamoDB/
└── app/
│    ├── templates/
│    │   ├── index.html
│    │   └── add_item.html
│    ├── app.py
└── docker-compose.yml
└── Dockerfile

```

```python
from flask import Flask, render_template, request, redirect, url_for
import boto3
from botocore.exceptions import ClientError

app = Flask(__name__)


dynamodb = boto3.resource(
    'dynamodb',
    endpoint_url="http://dynamodb-local:8000",
    region_name="us-west-2",
    aws_access_key_id="DUMMYIDEXAMPLE",
    aws_secret_access_key="DUMMYEXAMPLEKEY"
)

table_name = "TestTable"


@app.route('/')
def index():
    table = dynamodb.Table(table_name)
    try:
        response = table.scan()
        items = response.get('Items', [])
        return render_template('index.html', items=items)
    except ClientError as e:
        return f"Error: {e}"


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

```

- index.html

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Lista de Elementos</title>
  </head>
  <body>
    <h1>Elementos en DynamoDB</h1>
    <a href="{{ url_for('add_item') }}">Agregar nuevo elemento</a>
    <ul>
      {% for item in items %}
      <li>{{ item['id'] }} - {{ item['nombre'] }}: {{ item['valor'] }}</li>
      {% endfor %}
    </ul>
  </body>
</html>
```

- add_item.html

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Lista de Elementos</title>
  </head>
  <body>
    <h1>Elementos en DynamoDB</h1>
    <a href="{{ url_for('add_item') }}">Agregar nuevo elemento</a>
    <ul>
      {% for item in items %}
      <li>{{ item['id'] }} - {{ item['nombre'] }}: {{ item['valor'] }}</li>
      {% endfor %}
    </ul>
  </body>
</html>
```

- dockerfile

```dockerfile

FROM python:3.9-slim


WORKDIR /app


COPY app/app.py /app/app.py
COPY app/templates /app/templates


RUN pip install boto3 flask


CMD ["python", "app.py"]


```

- dockerfile

```bash

version: '3.8'
services:
  dynamodb-local:
    image: "amazon/dynamodb-local:latest"
    container_name: dynamodb-local
    command: "-jar DynamoDBLocal.jar -sharedDb -dbPath ./data"
    ports:
      - "8000:8000"
    volumes:
      - "./docker/dynamodb:/home/dynamodblocal/data"
    working_dir: /home/dynamodblocal

  app-python:
    build:
      context: .
      dockerfile: Dockerfile  # Dockerfile en la raíz del proyecto
    container_name: app-python
    depends_on:
      - dynamodb-local
    environment:
      AWS_ACCESS_KEY_ID: 'DUMMYIDEXAMPLE'
      AWS_SECRET_ACCESS_KEY: 'DUMMYEXAMPLEKEY'
    ports:
      - "8080:8080"
    command: >
      sh -c "pip install boto3 flask && python app.py"



```

### Run Docker Compose

In the console run the following command.

```bash
docker-compose up -d --build

```

## Results

![alt text](/img/image-5.png)
![alt text](/img/image-2.png)
![alt text](/img/image-3.png)
![alt text](/img/image-4.png)

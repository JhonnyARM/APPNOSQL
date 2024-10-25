## Introduction 

### DynamoDB

DynamoDB is a fully managed NoSQL database service provided by Amazon Web Services (AWS). It is designed to handle large amounts of data and provides fast and predictable performance with seamless scalability.

- **Managed Service:** DynamoDB is fully managed, meaning that AWS handles operational tasks such as hardware provisioning, setup, configuration, and backups.

- **NoSQL Database:** It is a NoSQL database, allowing for flexible data models and horizontal scaling, making it suitable for applications with varying data structures.

- **Performance:** DynamoDB offers single-digit millisecond response times, ideal for applications that require high-speed data access.

- **Scalability:** The service can automatically scale up and down to accommodate varying workloads, allowing applications to handle large volumes of data and traffic without manual intervention.

- **Global Tables:** DynamoDB supports global tables, enabling multi-region, fully replicated tables that provide low-latency access to data across different geographical locations.

- **Integration with AWS Services:** DynamoDB integrates seamlessly with other AWS services such as Lambda, API Gateway, and S3, allowing for the development of complex applications in the cloud.

- **Security and Compliance:** It provides built-in security features, including encryption at rest and in transit, and supports AWS Identity and Access Management (IAM) for fine-grained access control.

- **Code Example:** Below is a simple Python code snippet demonstrating how to interact with DynamoDB using the `boto3` library to create a table and add an item.

![alt text](Diagrama1.png)
- Here we have the compiled code and the generated graphics.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/emfbnr5oy5lfd6sf0rnw.png)
## Creating a dashboard with BOKEH in python
### Requirements:
- Python
- Visual Studio Code
### First steps
- Open visual studio code

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/bipsbnhguwq9tnjp19nc.png)
- We create a working environment and add a .py file

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/023vjfcpnhilrj4b5m0c.png)
- Important, to make this dashboard it is necessary to install the dependencies, for this we open a console in administrator mode and we execute
```bash
pip install bokeh
```

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/f59ek97fqwzy9vwxhjly.png)
- Once installed, run the sample code to generate graphics.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/4qmkdiqt1k48h504u8y6.png)
As we can see we have the panda and bokeh packages imported.

### Last step
- Run the project.
To run the project we will open the console and paste the following code:
```bash
python -m bokeh serve --show dashboard.py
```
this will show the dashboard on a local page.


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/d20b8b0h3x3cv1oy8z20.png)

## Deploy the project in the cloud

### To deploy the project it is necessary to have a cloud service provider, in this case I used a debian VPS.
### to install python in linux

```bash
apt update
```

```bash
apt install python3
```

### install the environment

```bash
sudo apt install python3-venv
mkdir my_project
cd my_project
python3 -m venv my_env
pip install bokeh
```

### Make my_env permanent:

```bash

nano ~/.bashrc
```

copy and past at the end:

```bash

source /ruta/a/my_env/bin/activate
```

in my case it was: 

```bash
source /opt/dashboardpy/my_env/bin/activate
```

ctrl+o ENTER ctrl+x

with "source" you're activating bashrc

```bash

source ~/.bashrc
```

### Permanent configuration of the project

finally we make the created websocket permanent, that is to say, it does not close when closing putty, now we create a nohup that will always be executed:
```bash
nohup python -m bokeh serve --show dashboard.py &
```


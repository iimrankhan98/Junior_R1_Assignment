# Junior_R1_Assignment 

## Step 1: Launch AWS EC2 ##
Install docker 

yum install docker -y

systemctl start docker

systemctl enable docker

## Step 2: Create flask Program ##
Create sample flask program with an endpoint which will ping a list of urls to see if they return 200.

Save the Flask application code to a file named app.py.
Save the requirements to a file named requirements.txt.
Save the Dockerfile to a file named Dockerfile.

## Step 3: Build Docker image and Run Docker container ##

docker build -t flask-app:v1 .
docker tag flask-app:v1  iimrankhan98/flask-app:v1
docker run -dit --name flask-app  -p 9090:9090 iimrankhan98/flask-app:v1

## Step 4: Test the flask application ##
You can then test the /ping endpoint by sending a POST request with a JSON body containing the list of URLs to ping, for example:

curl -X POST http://localhost:9090/ping -H "Content-Type: application/json" -d '{"urls": ["https://www.google.com", "https://www.example.com"]}'

Successfully output comes with status code 200

## Step 5: Push the Docker image in Docker Hub ##
Login "hub.docker.com" with user id and password

docker login
docker push iimrankhan98/flask-app:v1





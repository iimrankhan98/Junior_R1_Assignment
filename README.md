## Step 1: Launch AWS EC2 with Amazon Linux ##
Install docker on EC2

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


### Setup MicroK8s on AWS EC2 Ubuntu OS ###

## Step 1: Install MicroK8s ##

sudo apt update && sudo apt upgrade -y

sudo snap install microk8s --classic --channel=1.30

## Step 2: Join the group ##

sudo usermod -a -G microk8s $USER

mkdir -p ~/.kube

chmod 0700 ~/.kube

su - $USER

## Step 3: Check the status ##

microk8s status --wait-ready

## Step 4: Access Kubernetes ##

microk8s kubectl get nodes

alias kubectl='microk8s kubectl'


## Step 5: Deploy flask-app ##

Create a YAML file for your deployment, for example, deployment.yaml.

kubectl apply -f Create deployment.yml

kubectl get pods


## Step 6: Enabling MicroK8s Add-ons ##

For example, to enable a storage add-on that can auto-provision persistent volumes “PV”, we can use the below command.

microk8s enable dns

microk8s enable hostpath-storage

## Step 7: Starting and Stopping MicroK8s ##

microk8s start

microk8s stop


## Set up Gitlab Repo locally.check in. Could be using docker image as well ##

Setting up GitLab Locally Using Docker

docker pull gitlab/gitlab-ce:latest

docker run -d --name gitlab -p 443:443 -p 80:80 gitlab/gitlab-ce:latest

docker exec -it gitlab grep 'Password:' /etc/gitlab/initial_root_password















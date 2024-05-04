# Webapp-devops

## Overview
Welcome to the Webapp-devops project! This project aims to implement DevOps methodologies gradually, integrating various tools and practices step by step. The deployment utilizes a Raspberry Pi Model 4 as the server, running an nginx web app.

## Installation

### Prerequisites
To get started, you'll need the following:
1. Raspberry Pi with SD Card
2. Raspberry Pi Imager (to install the desired OS on your SD card; for this project, we're using Ubuntu Server)

### Setup Instructions
1. Install the desired OS on your Raspberry Pi's SD card using the Raspberry Pi Imager.
   ![Raspberry Pi Imager](https://github.com/imadtoumi/webapp-devops/assets/41326066/19ba3a2a-efd4-43d3-8eca-f8debe5abe23)

```python
ssh "username"@s"erver_ip_add"
```
1. update apt
```python
sudo apt update
```
2. Install nginx
```python
sudo apt install nginx
```
3. check the the server's ip address and access it from your local machine but typing the ip address in a browser, (if you are installing nginx in your local machine you can access it by typing localhost)

## Making changes in the file and Setting up git 
- File creation in var/www/html/
  . cd into the html directory an created index.html
```python
cd /var/www/html
touch index.html
nano index.html
```

   . Edit index.html and save it
```python
<h1>Welcome to devops project</h1>
```  
- Restart the nginx service
```python
systemctl restart nginx
```
#### Now access the nginx server from the browser (type server's ip address and port or type local host if runing it locally)
  ![nginx](https://github.com/imadtoumi/webapp-devops/assets/41326066/499345ad-6d8d-4615-a294-c5a0dadcfbd2)
</br>
#### Yes this is how the page will look like after the setup above, pretty boring isn't it? It'll get there little by little :)

. Now let's use git to save the progress and save the files in github
```python
git init
git config --global user.email "<email>"
git config --global user.name "<username>"
git add .
git commit -m "Initial install"
git remote add origin https://github.com/imadtoumi/webapp-devops.git
git push --set-upstream origin main
```

Git is set up as well as github and first push was performed, repo was created first in github before it was declared as the origin remote repo

- **Configuration Tips**: Provide tips for optimizing nginx configuration for performance and security.
- **Containerization**: Containerize the web app using technologies like Docker
- **Testing Strategies**: Discuss testing strategies for the web app and how to implement automated testing.
- **Monitoring**: Explore options for monitoring the deployed web app's performance and availability.
- **CI/CD Pipelines**: Implement CI/CD pipelines for automated testing and deployment.

# Containerizing Flask App
### after testing and familirizing with the Raspberry Pi now i will containerize a flask app i have created to test with (the files used are all in the repo).
#### first we have to install Docker
```python
sudo apt install docker.io
```
#### Create our work directory and all the files
```python
mkdir flask-app
cd flask-app
mkdir templates
touch Dockerfile app.py index.html requirement.txt
mv index.html templates 
```

#### Edit the files with the content of the files in th repo
#### Let's build our docker image
```python
docker build -t flask-docker .
```
- After running "docker images" you will see the image we have built </br> 
![flask](https://github.com/imadtoumi/webapp-devops/assets/41326066/39e8b1d5-5180-4dbb-8120-c220961b3e55)
</br>
- Make sure you are in the directory where you have your files and the <b>Dockerfile</b>

#### Let's run the docker container usiong the image we built
```python
docker run -d -p 5000:5000 flask-docker
```
- After runing "docker ps" you will se the conatiners running and you will the container we did run
![container](https://github.com/imadtoumi/webapp-devops/assets/41326066/da73384e-c597-4d5b-b22e-3338179dfc22)

1- -d is for detach so you can be able to interact with the server after runing the container </br>
2- -p is for port mapping, without this accessing the app from the browser won't work and you will be faced with " Web site unrechabale "

#### Now let's access our web app from the browser
![webapp](https://github.com/imadtoumi/webapp-devops/assets/41326066/8c069f15-b18c-4196-8f2f-bd3c3af2ea54)

- Don't forget to initilize git repo in the directory you are working and follow the commands we did above (Git setup part)

# Jenkins setup
- For jenkins i am runing it as a contianer in an other vm other then our raspberry pi.
### Let's get jenkins image and run it as a docker container  
1- first we'll pull the image from the offical jenkins repo (there is different way of doing it but this the simplest and that' what i used). </br>
```python
docker pull jenkins/jenkins:latest
```
2- Now let's run the container using jenkins image </br>
```python
docker run -d -v /var/run/docker.sock:/var/run/docker.sock -p 8080:8080 jenkins/jenkins 
```
###### This command starts Jenkins in a Docker container, exposing its web interface on port 8080 of your host machine. It also mounts the Docker socket to enable Jenkins to interact with the Docker daemon, allowing tasks like building Docker images or running containers as part of CI/CD pipelines.

### Configuration done inside docker container 
- We have to login to our container and give jenkins user rights to read and write the docker.sock file
```python
docker exec -it --user root [container_id] bash
```
- Let's give the rights
```python
chmod 666 /var/run/docker.sock
```
#### Pipeline creation 
- After the steps above now we can access our jenkins from the browser by using the vm ip add or by using local host if jenkins is hosted in our machine </br>
- Configure the account and install the recommended plugins </br>
- After that we can now go to the plugins and install the pulgins we need for our use case </br>
![plugins](https://github.com/imadtoumi/webapp-devops/assets/41326066/1c4d9335-1ef3-43f7-bc78-ccc04d66887e) </br>
- Search for the plugins needed (Docker and git and any other plugin that needs to be used) and install them. </br>
![available plugins](https://github.com/imadtoumi/webapp-devops/assets/41326066/03f22752-b75f-42f3-a27c-52f100ad4531) </br>
- After you install the plugins go to tools and configure them ( https://www.youtube.com/watch?v=PKcGy9oPVXg this video can help with jenkins understanding) </br>
- Now let's create our pipeline.</br>
![pipeline](https://github.com/imadtoumi/webapp-devops/assets/41326066/b8024f29-5116-4710-80c1-deacd06bdf8b)
</br>
- Provide the github project link and build trigger which is 'Github hook trigger' for our case. </br>
- Now let's provide the pipeline syntax. </br>

```python

pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // Check out the source code from the GitHub repository
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], userRemoteConfigs: [[url: 'https://github.com/imadtoumi/webapp-devops.git']]])
            }
        }
        
        stage('Initialize'){
            steps{
                script{
                    def dockerHome = tool 'My-Docker'
                    env.PATH = "${dockerHome}/bin:${env.PATH}"
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                // Build Docker image using the Dockerfile in the repository
                script {
                    sh 'docker build -t flask-docker:latest .'
                }
            }
        }

    }
}
```
Checkout: Retrieves source code from a GitHub repository. </br>
Initialize: Sets up Docker environment. </br>
Build Docker Image: Uses the Dockerfile in the repository to build the Docker image named "flask-docker:latest". </br>

- Let's run the pipeline. </br>
![buildpipe](https://github.com/imadtoumi/webapp-devops/assets/41326066/5684e8a7-7e6e-43c9-8f07-d0ddda91a4ba) </br>
- If we go to status after runing the pipline we will see if it finished successfully or not. </br>
![success](https://github.com/imadtoumi/webapp-devops/assets/41326066/0c0a8115-e545-4caf-9f16-55c01e5d1f9a) </br>
- It was done successfully and we can see that the image is build from the github repo and added to our local machine (Node in jenkins, we will add more nodes in next section). </br>
![fl-img](https://github.com/imadtoumi/webapp-devops/assets/41326066/c1c4e0b4-983f-4255-84f0-20725a61ec7c)
#### Adding node where we deploy (Raspberry pi in our case)
- First make sure you have Java installed in the node you want to add in Jenkins, without Java connection will fail. </br> 
. Setting up a new slave is simple if you will follow what the ui say, but for more calrity you can follow this https://www.youtube.com/watch?v=99DddJiH7lM&t=869s (that's what i watched as well). </br>
  
#### Exposing Jenkins to internet to enable webhook in github
- Without exposing our Jenkins to the internet webhooks won't work, why ? Because github can not ping and connect to machine running inside your local network and it's not exposed to the internet. </br>
- For this to be done we will use a simple tool and easy to configure it's name is " Ngrok ", since we runing everything in docker we will set it up in dockr as well. </br>
- Go to https://ngrok.com/ , create an account and go to setup & installation and choose docker instead of windows which is selected by default. </br>
 ```python
docker pull ngrok/ngrok
```
- After pulling the image you will find the docker run command with your authtoken, as well as the port you want to forward to (in our case 8080 because we are configured jenkins on this port)
```python
docker run --net=host -it -e NGROK_AUTHTOKEN="your_auth_token" ngrok/ngrok:latest http 8080
```
- Now after our container is up and runing as well as our jenkins, we will find the link in the endpoints page in ngrok. </br>
![ngrok](https://github.com/imadtoumi/webapp-devops/assets/41326066/0ff2378e-7f42-4281-b2fa-5c69fbecf946) </br>
- Let's access our Jenkins using this link! </br>
![ngrok-jenk](https://github.com/imadtoumi/webapp-devops/assets/41326066/a5d39911-3aa8-494d-a72a-991465dd733f)</br>
Yes siir it works. </br>

- Now we can configure the webhook so it can trigger the build whenever a new push is commited
![webhook](https://github.com/imadtoumi/webapp-devops/assets/41326066/be0e689e-7079-4585-b276-a4dca6b338b4)

##### Configure the pipeling to run on the added node when we push on github
- This is the pipeline we will use, make sure you give the label of the new added node in (agent {label 'label'})
```python
pipeline {
    agent {label 'slave-1'}

    stages {
        stage('Checkout') {
            steps {
                // Check out the source code from the GitHub repository
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], userRemoteConfigs: [[url: 'https://github.com/imadtoumi/webapp-devops.git']]])
            }
        }
        
        stage('Initialize'){
            steps{
                script{
                    def dockerHome = tool 'My-Docker'
                    env.PATH = "${dockerHome}/bin:${env.PATH}"
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                // Build Docker image using the Dockerfile in the repository
                script {
                    sh '''
                        docker build -t flask-docker:latest .
                        image_id=$(docker images -f dangling=true -q)
                        con_id=$(docker ps -aqf "ancestor=$image_id")
                        docker stop $con_id
                        docker container rm $con_id
                        docker image rm $image_id
                        docker run -d -p 5000:5000 flask-docker
                    '''
                }
            }
        }

    }
}
```
###### Piepline explanation
- Checks out code from the specified GitHub repository. </br>
- Sets up the Docker environment. </br>
- Builds the "flask-docker:latest" image. </br>
- Removes dangling images and containers. </br>
- Runs a new container on port 5000 .</br>
###### So in the pipeline above demonstrates the initial steps towards CI by automating the build process and lays the groundwork for further CD implementation.  </br>
- Now after we perform a new push in our github we will be abvle to see the build starts by it self in the build hisotry. </br>

## Contribution
Contributions to this project are welcome! Feel free to submit issues, feature requests, or pull requests. For support or collaboration, reach out via email at \imadtoumi8@gmail.com or via discord imad5208.

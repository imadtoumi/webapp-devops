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

### Configuration done for our project 
#### Pipeline creation 

#### Adding node where we deploy (Raspberry pi in our case)


## Contribution
Contributions to this project are welcome! Feel free to submit issues, feature requests, or pull requests. For support or collaboration, reach out via email at \imadtoumi8@gmail.com or via discord imad5208.

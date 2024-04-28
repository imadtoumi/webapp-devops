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
####Now access the nginx server from the browser (type server's ip address and port or type local host if runing it locally)
  ![nginx](https://github.com/imadtoumi/webapp-devops/assets/41326066/499345ad-6d8d-4615-a294-c5a0dadcfbd2)
</br>
####Yes this is how the page will look like after the setup above, pretty boring isn't it? It'll get there little by little :)

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

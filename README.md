# Fetch-Receipt-Processor-Challenge

## Description
This repository contains the solution to the coding assessment by **[Fetch](https://fetch.com/)**.

I've used **Python-Flask** to write the backend APIs.

The Flask app can be run using the **dockerfile**

The app will run on localhost (http://127.0.0.1:5000)

## Installation and Execution
### To run the code in a docker container:
1. Clone the repository and navigate to the repository directory
```
git clone https://github.com/Chirag-07/Fetch-Receipt-Processor-Challenge.git
cd Fetch-Receipt-Processor-Challenge
```
2. Build the docker image
```
docker build -t <app-name> .
```

3. Run the docker container
```
docker run -d -p 5000:5000 --name <container-name> <app-name>
```

### To run the code through the python file
1. Navigate to the repository directory

2. Run the below command
```
flask run
```
*OR*
```
python app.py
```

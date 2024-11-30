# Fetch-Receipt-Processor-Challenge

## Description
This repository contains the solution to the coding assessment by **[Fetch](https://fetch.com/)**.

I've used **Python-Flask** to write the backend APIs.

The Flask app can be run using the **dockerfile**

## Installation and Execution
To run the code in a docker container:
1. Clone the repository and navigate to the directory containing the repository and the **dockerfile**

2. Build the docker image
```
docker build -t <flask-app-name> .
```

3. Run the docker container
```
docker run -p 5000:5000 <flask-app-name>
```

# Welcome to CVAT-automation!

This project presents a simple solution for fetching jobs within the CVAT rest api server and generates CSV file with each individual user with its assigned jobs. 

# Requirements
    Python 3.10
    cvat_sdk 2.12.1

# Setting up test server using Docker:
1. Install Docker from official [website](https://www.docker.com/get-started/).
2. Install required version of Python from official [website](https://www.python.org/downloads/).
3. Install all missing packages using:
   > pip install package_name==version

   or use the requirements.txt file to install all packages at once using:
   > pip install -r /path/to/requirements.txt
   
4. Pull the test Docker image by running following command from terminal:
   >docker pull muonsoft/openapi-mock
5. Run the docker container using:
   >docker run -p 8080:8080 -e "OPENAPI_MOCK_SPECIFICATION_URL=https://app.cvat.ai/api/schema/" --rm muonsoft/openapi-mock

   * Here the *-p* argument defined port on which the server will be available. In case you choose different port, remember to change it within the script.
   * In this case the server is running at *(http://localhost:8080)*.




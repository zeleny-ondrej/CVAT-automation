# Welcome to CVAT-automation!


## Description

This project presents a simple solution for fetching jobs within the CVAT rest api server and generates CSV file with each individual user with its assigned jobs. Each script run generate unique subdirectory (based on current datetime) within the "assignments" directory (created by the script) and saves jobs of individual assignees into separate .csv file based on assignees' id. All unassigned jobs are saved into "Unassigned.csv" file.




## Requirements
    Python 3.10
    cvat_sdk~=2.12.1
    attrs~=23.2.0
    pillow~=10.3.0
    python-dateutil~=2.9.0.post0
    requests~=2.31.0
    packaging~=24.0
    tqdm~=4.66.4
    urllib3~=2.2.1
    setuptools~=68.2.0
    typing_extensions~=4.11.0
    platformdirs~=4.2.1
    pandas~=2.2.2
    numpy~=1.26.4
    PyYAML~=6.0.1

   #### Optional:

    pre-commit~=3.7.0

## Setting up test server using Docker:
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


6. Run the get_jobs.py script using above defined interpreter:
   * Using terminal:
   
         python310 get_jobs.py --args
   
   * Or directly from your editor.


7. The structure of saved files is as follows:

   * assignments directory
     * *current_datetime* folder
       * *user_id_1*.csv 
       * *user_id_2*.csv 
       *  ....
       *  ....
       * *user_id_n*.csv 
       * Unassigned.csv - unassigned jobs






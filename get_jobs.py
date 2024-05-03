from cvat_sdk.api_client import Configuration, ApiClient, exceptions

# Configuration, for testing purposes the authentication is OFF
config = Configuration(
    host="http://localhost:8080/",
    # username='YOUR_USERNAME',
    # password='YOUR_PASSWORD'
)
with ApiClient(config) as api_client:

    try:
        # Query list of all jobs
        (data, response) = api_client.jobs_api.list()
    except exceptions.ApiException as e:
        # Catch exceptions
        print("Exception when trying to read list of jobs: %s\n" % e)

    jobs = data['results']

print(f"Total of {len(jobs)} jobs..")

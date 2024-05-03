from cvat_sdk.api_client import Configuration, ApiClient, exceptions
import argparse


def main(configuration):
    # Configuration, for testing purposes the authentication is OFF
    config = Configuration(
        host=configuration['host'],
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


if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser(description="Description of your program")
    parser.add_argument('--host', type=str, default='http://localhost:8080/', help='Address of the REST API')
    arguments = vars(parser.parse_args())
    main(arguments)

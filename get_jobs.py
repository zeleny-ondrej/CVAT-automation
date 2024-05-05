from cvat_sdk.api_client import Configuration, ApiClient, exceptions
import argparse
import os
from pathlib import Path
import datetime
import pandas as pd


def main(configuration):
    # Configuration, for testing purposes the authentication is OFF
    config = Configuration(
        host=configuration["host"],
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

        jobs = data["results"]

    print(f"Total of {len(jobs)} jobs found.")

    # Create a directory for "todays" jobs
    save_dir = Path("assignments")
    if not save_dir.exists():
        os.mkdir(save_dir)
    datetime_now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S.%f")
    save_dir = save_dir / Path(datetime_now)
    os.mkdir(save_dir)

    # Dictionary of assignee (keys)-jobs(values)
    # https://docs.cvat.ai/docs/api_sdk/sdk/reference/models/job-read/
    assignments = dict()
    for job in jobs:
        if job["assignee"] is None:
            assignee = "Unassigned"
        else:
            assignee = str(job["assignee"]["id"])

        if assignee in assignments.keys():
            assignments[assignee].append(job._data_store)
        else:
            assignments[assignee] = [job._data_store]

    users = len(assignments)
    users += -1 if "Unassigned" in assignments.keys() else 0
    print(f"\tAssigned to {users} users.")

    unassigned = (
        len(assignments["Unassigned"])
        if "Unassigned" in assignments.keys()
        else 0
    )
    print(f"\t{unassigned} unassigned jobs.")

    for assignee in assignments.keys():
        k = pd.DataFrame.from_records(assignments[assignee])
        k.to_csv(save_dir / Path(assignee + ".csv"), index=False)


if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser(description="Description of your program")
    parser.add_argument(
        "--host",
        type=str,
        default="http://localhost:8080/",
        help="Address of the REST API",
    )
    arguments = vars(parser.parse_args())
    main(arguments)

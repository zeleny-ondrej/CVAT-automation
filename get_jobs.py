import argparse
import os
from pathlib import Path
import datetime
import pandas as pd
import logging
from Lib.retrieve import Retrieve

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    filename="get_jobs.log",
    filemode="w",
)


def main(configuration):
    logging.info(f"Host address: {configuration['host']}.")
    retriever = Retrieve(
        hostname=configuration["host"],
        username=configuration["username"],
        password=configuration["password"],
    )
    jobs = retriever.get_jobs()

    logging.info(f"Total of {len(jobs)} jobs found.")

    # Create a directory for "todays" jobs
    save_dir = Path("assignments")
    if not save_dir.exists():
        os.mkdir(save_dir)
    datetime_now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S.%f")
    save_dir = save_dir / Path(datetime_now)
    os.mkdir(save_dir)
    logging.info(f"Saving jobs to {save_dir}")

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
    unassigned = (
        len(assignments["Unassigned"])
        if "Unassigned" in assignments.keys()
        else 0
    )
    logging.info(
        f"Found {users} with assigned jobs. {unassigned} jobs are unassigned."
    )

    for assignee in assignments.keys():
        k = pd.DataFrame.from_records(assignments[assignee])
        k.to_csv(save_dir / Path(assignee + ".csv"), index=False)


if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser(description="Description of your program")
    parser.add_argument(
        "--host",
        type=str,
        default="http://localhost:808/",
        help="Address of the REST API",
    )
    parser.add_argument(
        "--username",
        type=str,
        default=None,
        help="Username with access to the REST API",
    )
    parser.add_argument(
        "--password",
        type=str,
        default=None,
        help="Password to the REST API",
    )
    arguments = vars(parser.parse_args())
    main(arguments)

from cvat_sdk.api_client import Configuration, ApiClient, exceptions


class Retrieve:
    def __init__(
        self, hostname: str = "", username: str = "", password: str = ""
    ):
        super(Retrieve, self).__init__()
        self.config = Configuration(
            host=hostname, username=username, password=password
        )

    def config(self):
        return self.config

    def get_jobs(self):

        if (
            "http://" not in self.config.host
            and "https://" not in self.config.host
            or self.config.host == ""
        ):
            raise Exception(f"Invalid host URL: {self.config.host}")
        with ApiClient(self.config) as api_client:
            try:
                # Query list of all jobs
                (data, response) = api_client.jobs_api.list()
            except exceptions.ApiException as e:
                # Catch exceptions
                raise Exception(f"Unable to retrieve data due to: {e}")
            jobs = data["results"]
        return jobs

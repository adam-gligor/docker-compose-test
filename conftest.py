import os
import pytest


@pytest.fixture(scope="session", autouse=True)
def env_setup():
    postgres_url = os.getenv(
        "POSTGRES_URL", "postgresql://postgres:password@localhost:9016/postgres"
    )
    os.environ["POSTGRES_URL"] = postgres_url

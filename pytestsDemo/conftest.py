# universal fixture which can be used in any method
# the file name must be conftest

import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executed this first ")
    yield
    print("I will be executed last")

@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Lokesh", "Darne", "lokeshdarne@gmail.com"]

@pytest.fixture(params=["chrome", "firefox", "IE"])

def crossBrowser(request):
    return request.param

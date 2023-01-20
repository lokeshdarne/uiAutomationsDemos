#pip iinstall pytest to install
#naming convesion: test_name (any pytest file should start with test_)
#pytest method names should start with test
#any code should be wrapped in method
import pytest


def test_firstProgram():
    print("Hello")

@pytest.mark.xfail
def test_SecondProgram():
    print("Good Morning")



def test_crossBrowser(crossBrowser):
    print(crossBrowser)
# pip iinstall pytest to install
# naming convesion: test_name (any pytest file should start with test_)
# pytest method names should start with test
# any code should be wrapped in method
# method name should have sense
# -k stands for method names execution to run specific methods
# -s for logs in output
# -v stands for more infor metadata
# we can run specific file with py.test <filname>
# you can mark (tag) tests @pytest.mark.smoke and then run with -m
# you can skip a particular TC using @pytest.mark.skip above the method
# @pytest.mark.xfail is used to avoid reporting TC pass or fail
# fixtures are used as setup and tear down methods for test cases - conftest file to generalize
# fixture and make it available to all test cases
# datadriven and parameterization can be done with return statements in tuple format
# when you define fixture to class only, it will run once before the Class is initiated and at the end after all methods are executed 

import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi"

def test_SecondProgram():
    a = 4
    b = 6
    assert a+2 == 6, "Addition do not match"


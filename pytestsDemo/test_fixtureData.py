import pytest

from pytestsDemo.BaseClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestExample(BaseClass):

    def test_editProfile(self, dataLoad):
        log = self.getLogger()
        log.info(dataLoad[0])
        log.info(dataLoad[1])
        print(dataLoad[2])



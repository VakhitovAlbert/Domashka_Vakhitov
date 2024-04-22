import pytest
import time
import datetime

class TestAlbert:

    def test_01(self):
        assert 2*2 == 4

    def test_02(self, time2):
        assert 50/5 == 10

    def test_03(self, time2):
        assert -10+10 == 0

    def test_04(self):
        assert 0-2 == -2


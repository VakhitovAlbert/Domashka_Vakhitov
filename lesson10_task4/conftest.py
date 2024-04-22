import pytest
import time
from datetime import datetime


@pytest.fixture(scope="class", autouse=True)
def time1():

    st_time = datetime.now()
    print('\n Время начала:' + str(st_time))
    yield
    en_time = datetime.now()
    print('\n Время окончания:'+str(en_time))


@pytest.fixture()
def time2():
    start_time = time.time()
    yield
    end_time = time.time() - start_time
    print('\n Время выполнения:' + str(end_time))

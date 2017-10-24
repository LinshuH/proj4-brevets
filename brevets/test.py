import acp_times

import nose
import arrow


def open1():
    assert open_time(100,200,"2017-01-01T00:00") == "02:56"

def open2():
    assert open_time(200,200,"2017-01-01T00:00") == "05:53"
    
def open3():
    assert open_time(210,200,"2017-01-01T00:00") == "05:53"
    
def close1():
    assert close_time(100,200,"2017-01-01T00:00") == "06:40"
    
def close2():
    assert open_time(199,200,"2017-01-01T00:00") == "13:16"
    
def close3():
    assert open_time(100,200,"2017-01-01T00:00") == "13:30"
    

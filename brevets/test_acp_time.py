import acp_times

import nose
import arrow


def test_open():
    assert open_time(0,200,"2017-01-01T14:00") == "2017-01-01T14:00"
    assert open_time(50,200,"2017-01-01T14:00") == "2017-01-01T15:28"
    assert open_time(100,200,"2017-01-01T14:00") == "2017-01-01T16:56"
    assert open_time(199,200,"2017-01-01T14:00") == "2017-01-01T19:51"
    assert open_time(200,200,"2017-01-01T14:00") == "2017-01-01T19:53"
    assert open_time(210,200,"2017-01-01T14:00") == "2017-01-01T19:53"
    
def test_close():
    assert close_time(0,200,"2017-01-01T14:00") == "2017-01-01T15:00"
    assert close_time(50,200,"2017-01-01T14:00") == "2017-01-01T17:20"
    assert close_time(100,200,"2017-01-01T14:00") == "2017-01-01T20:40"
    assert close_time(199,200,"2017-01-01T14:00") == "2017-01-02T03:16"
    assert close_time(200,200,"2017-01-01T14:00") == "2017-01-02T03:30"
    assert close_time(201,200,"2017-01-01T14:00") == "2017-01-02T03:30"
    

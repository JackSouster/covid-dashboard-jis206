from time_handler import hhmm_to_seconds_from_now
from time_handler import seconds_from_now_to_hhmm

import time

def test_time_handler():
    assert seconds_from_now_to_hhmm(hhmm_to_seconds_from_now("12:15"))
    assert seconds_from_now_to_hhmm(hhmm_to_seconds_from_now("09:00"))
    assert seconds_from_now_to_hhmm(hhmm_to_seconds_from_now("18:37"))
    assert seconds_from_now_to_hhmm(hhmm_to_seconds_from_now("00:00"))
    assert seconds_from_now_to_hhmm(hhmm_to_seconds_from_now("23:59"))
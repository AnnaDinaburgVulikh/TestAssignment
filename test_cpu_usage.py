import pytest
import psutil

from system_info import get_cpu_usage


[pytest]
def test_cpu_under_60():
    percantage = float(get_cpu_usage().strip("%"))
    assert percantage < 60, "CPU usage is above 60%"

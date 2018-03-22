import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Code.MathLib import average
import test_common
import pytest

lowerAverage = 16.909
upperAverage = 2640560.364

def test_average_lower_bound():
  assert test_common.isclose(average(test_common.lowerBound), lowerAverage), "Lower average bound test"

def test_average_upper_bound():
  assert test_common.isclose(average(test_common.upperBound), upperAverage), "Upper average bound test"

def test_average_invalid():
  with pytest.raises(TypeError, message="Invalid average test"):
    average(test_common.invalid)

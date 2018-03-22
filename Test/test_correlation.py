import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Code.MathLib import correlation
import test_common
import pytest

lower_x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
lower_y = [5, 8, 5, 5, 3, 5, 5, 2, 3.8, 5, 9]

upper_x = [1, 2, 4, 5, 7, 8, 10, 12, 14, 17, 20]
upper_y = [30, 29, 50, 60, 66, 70, 75, 77, 85, 100, 115]

invalid_x = [1, 2, "r"]
invalid_y = [0, 0, 0]

lower_correlation = 0.006077
upper_correlation = 0.977

def test_correlation_lower_bound():
  assert test_common.isclose(correlation(lower_x, lower_y), lower_correlation), "Lower correlation bound test"

def test_correlation_upper_bound():
  assert test_common.isclose(correlation(upper_x, upper_y), upper_correlation), "Upper correlation bound test"

def test_correlation_invalid():
  with pytest.raises(TypeError, message="Invalid correlation test"):
    correlation(invalid_x, invalid_y)
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Code.MathLib import regression_b0
import test_common
import pytest

upper_x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
upper_y = [793029, 689403, 389032, 203819, 2, -182039, -403290, -584039, -859302, -1029329]

lower_x = [1, 2, 4, 5, 7, 8, 10, 12, 14, 17, 20]
lower_y = [0, 240.2, 403.2, 670.32, 883.29231, 1000, 2039.53, 2394.392, 5039.322332, 9999.9999, 1200]

invalid_x = [1, 2]
invalid_y = [0, 0, 0]

upper_b1 = -206732.6060606
lower_b1 = 306.94441413099815

upper_b0 = 1038757.9333332
lower_b0 = -620.3804428272556

def test_correlation_lower_bound():
  print(regression_b0(lower_x, lower_y, lower_b1))
  assert test_common.isclose(regression_b0(lower_x, lower_y, lower_b1), lower_b0), "Lower regression (b0) bound test"

def test_correlation_upper_bound():
  print(regression_b0(upper_x, upper_y, upper_b1))
  assert test_common.isclose(regression_b0(upper_x, upper_y, upper_b1), upper_b0), "Upper regression (b0) bound test"

def test_correlation_invalid():
  with pytest.raises(TypeError, message="Invalid regression (b0) test"):
    regression_b0(invalid_x, invalid_y, 0)
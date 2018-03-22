import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Code.MathLib import variance
import test_common
import pytest

lower_variance = 29.090
upper_variance = 13652525631910

def test_variance_lower_bound():
  assert test_common.isclose(variance(test_common.lowerBound), lower_variance), "Lower variance bound test"

def test_variance_upper_bound():
  assert test_common.isclose(variance(test_common.upperBound), upper_variance), "Upper variance bound test"

def test_variance_invalid():
  with pytest.raises(TypeError, message="Invalid variance test"):
    variance(test_common.invalid)
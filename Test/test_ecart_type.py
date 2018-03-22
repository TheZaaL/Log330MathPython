import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Code.MathLib import ecartType
import test_common
import pytest

lower_ecart_type = 5.393
upper_ecart_type = 3694932.426

def test_ecart_type_lower_bound():
  assert test_common.isclose(ecartType(test_common.lowerBound), lower_ecart_type), "Lower ecart type bound test"

def test_ecart_type_upper_bound():
  assert test_common.isclose(ecartType(test_common.upperBound), upper_ecart_type), "Upper ecart type bound test"

def test_ecart_type_invalid():
  with pytest.raises(TypeError, message="Invalid ecart type test"):
    ecartType(test_common.invalid)
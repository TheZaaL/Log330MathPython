import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Code.MathLib import correlation_text, null_correlation_text, perfect_correlation_text, error_correlation_text
import test_common
import pytest

lower_correlation = 0.0321
upper_correlation = 1
invalid_correlation = 40

def test_correlation_text_lower_bound():
  assert correlation_text(lower_correlation) == null_correlation_text, "Lower correlation text bound test"

def test_correlation_text_bound():
  assert correlation_text(upper_correlation) == perfect_correlation_text, "Upper correlation text bound test"

def test_correlation_text_invalid():
  assert correlation_text(invalid_correlation) == error_correlation_text, "Upper correlation text bound test"


lowerBound = [10, 11, 12, 13, 14, 16, 18, 21, 22, 24, 25]
upperBound = [53278, 43892, 93482, 8374829, 934049, 843928, 843902, 8439220, 738297, 382903, 8298384]
invalid = [1, 2, 3, "a"]

def isclose(a, b, rel_tol=0.001, abs_tol=0.0):
  return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)
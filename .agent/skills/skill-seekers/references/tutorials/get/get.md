# How To: Get

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate Series: test get

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series(np.array([43, 48, 60, 48, 50, 51, 50, 45, 57, 48, 56, 45, 51, 39, 55, 43, 54, 52, 51, 54]), index=Index([25.0, 36.0, 49.0, 64.0, 81.0, 100.0, 121.0, 144.0, 169.0, 196.0, 1225.0, 1296.0, 1369.0, 1444.0, 1521.0, 1600.0, 1681.0, 1764.0, 1849.0, 1936.0], dtype=np.float64))
```


## Complete Example

```python
# Workflow
s = Series(np.array([43, 48, 60, 48, 50, 51, 50, 45, 57, 48, 56, 45, 51, 39, 55, 43, 54, 52, 51, 54]), index=Index([25.0, 36.0, 49.0, 64.0, 81.0, 100.0, 121.0, 144.0, 169.0, 196.0, 1225.0, 1296.0, 1369.0, 1444.0, 1521.0, 1600.0, 1681.0, 1764.0, 1849.0, 1936.0], dtype=np.float64))
```

## Next Steps


---

*Source: test_get.py:47 | Complexity: Beginner | Last updated: 2026-06-02*
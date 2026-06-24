# How To: Preserve Dtypes

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: pytest

## Overview

Instantiate DataFrame: test preserve dtypes

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.generic`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.integer`

**Setup Required:**
```python
# Fixtures: op
```

## Step-by-Step Guide

### Step 1: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame({'A': ['a', 'b', 'b'], 'B': [1, None, 3], 'C': pd.array([1, None, 3], dtype='Int64')})
```


## Complete Example

```python
# Setup
# Fixtures: op

# Workflow
df = pd.DataFrame({'A': ['a', 'b', 'b'], 'B': [1, None, 3], 'C': pd.array([1, None, 3], dtype='Int64')})
```

## Next Steps


---

*Source: test_dtypes.py:28 | Complexity: Beginner | Last updated: 2026-06-02*
# How To: Ffill

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate DataFrame: test ffill

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: left, right
```

## Step-by-Step Guide

### Step 1: Assign expected = DataFrame(...)

```python
expected = DataFrame({'key': ['a', 'b', 'c', 'd', 'e', 'f'], 'lvalue': [1.0, 1, 2, 2, 3, 3.0], 'rvalue': [np.nan, 1, 2, 3, 3, 4]})
```


## Complete Example

```python
# Setup
# Fixtures: left, right

# Workflow
expected = DataFrame({'key': ['a', 'b', 'c', 'd', 'e', 'f'], 'lvalue': [1.0, 1, 2, 2, 3, 3.0], 'rvalue': [np.nan, 1, 2, 3, 3, 4]})
```

## Next Steps


---

*Source: test_merge_ordered.py:39 | Complexity: Beginner | Last updated: 2026-06-02*
# How To: Concat Sorts Columns

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate DataFrame: test concat sorts columns

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: sort
```

## Step-by-Step Guide

### Step 1: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [1, 2, 3, 4], 'b': [1, 2, None, None], 'c': [None, None, 5, 6]}, columns=['a', 'b', 'c'])
```


## Complete Example

```python
# Setup
# Fixtures: sort

# Workflow
expected = DataFrame({'a': [1, 2, 3, 4], 'b': [1, 2, None, None], 'c': [None, None, 5, 6]}, columns=['a', 'b', 'c'])
```

## Next Steps


---

*Source: test_sort.py:16 | Complexity: Beginner | Last updated: 2026-06-02*
# How To: Numpy Err State Is Default

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Configuration example: test numpy err state is default

## Prerequisites

**Required Modules:**
- `os`
- `pytest`
- `pandas`
- `pandas._testing`
- `numpy`


## Step-by-Step Guide

### Step 1: Assign expected = value

```python
expected = {'over': 'warn', 'divide': 'warn', 'invalid': 'warn', 'under': 'ignore'}
```


## Complete Example

```python
# Workflow
expected = {'over': 'warn', 'divide': 'warn', 'invalid': 'warn', 'under': 'ignore'}
```

## Next Steps


---

*Source: test_util.py:13 | Complexity: Beginner | Last updated: 2026-06-02*
# How To: Duplicate Columns

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate DataFrame: test duplicate columns

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.groupby`

**Setup Required:**
```python
# Fixtures: request, groupby_func, as_index
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([[1, 3, 6], [1, 4, 7], [2, 5, 8]], columns=list('abb'))
```


## Complete Example

```python
# Setup
# Fixtures: request, groupby_func, as_index

# Workflow
df = DataFrame([[1, 3, 6], [1, 4, 7], [2, 5, 8]], columns=list('abb'))
```

## Next Steps


---

*Source: test_all_methods.py:42 | Complexity: Beginner | Last updated: 2026-06-02*
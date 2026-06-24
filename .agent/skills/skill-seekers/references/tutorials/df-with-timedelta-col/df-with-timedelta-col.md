# How To: Df With Timedelta Col

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: pytest

## Overview

Instantiate DataFrame: df with timedelta col

## Prerequisites

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.tests.groupby`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 1, 1, 1, 1, 2, 2, 2, 2], 'b': [3, 3, 4, 4, 4, 4, 4, 3, 3], 'c': range(9), 'd': datetime.timedelta(days=1)})
```


## Complete Example

```python
# Workflow
df = DataFrame({'a': [1, 1, 1, 1, 1, 2, 2, 2, 2], 'b': [3, 3, 4, 4, 4, 4, 4, 3, 3], 'c': range(9), 'd': datetime.timedelta(days=1)})
```

## Next Steps


---

*Source: test_raises.py:72 | Complexity: Beginner | Last updated: 2026-06-02*
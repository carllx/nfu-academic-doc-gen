# How To: Df With Datetime Col

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: pytest

## Overview

Instantiate DataFrame: df with datetime col

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
df = DataFrame({'a': [1, 1, 1, 1, 1, 2, 2, 2, 2], 'b': [3, 3, 4, 4, 4, 4, 4, 3, 3], 'c': range(9), 'd': datetime.datetime(2005, 1, 1, 10, 30, 23, 540000)})
```


## Complete Example

```python
# Workflow
df = DataFrame({'a': [1, 1, 1, 1, 1, 2, 2, 2, 2], 'b': [3, 3, 4, 4, 4, 4, 4, 3, 3], 'c': range(9), 'd': datetime.datetime(2005, 1, 1, 10, 30, 23, 540000)})
```

## Next Steps


---

*Source: test_raises.py:59 | Complexity: Beginner | Last updated: 2026-06-02*
# How To: Values Duplicates

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate DataFrame: test values duplicates

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([[1, 2, 'a', 'b'], [1, 2, 'a', 'b']], columns=['one', 'one', 'two', 'two'])
```


## Complete Example

```python
# Workflow
df = DataFrame([[1, 2, 'a', 'b'], [1, 2, 'a', 'b']], columns=['one', 'one', 'two', 'two'])
```

## Next Steps


---

*Source: test_values.py:54 | Complexity: Beginner | Last updated: 2026-06-02*
# How To: Nlargest Duplicates On Starter Columns

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate DataFrame: test nlargest duplicates on starter columns

## Prerequisites

**Required Modules:**
- `string`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.util.version`


## Step-by-Step Guide

### Step 1: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame({'a': [2, 2, 2, 1, 1, 1], 'b': [1, 2, 3, 3, 2, 1]})
```


## Complete Example

```python
# Workflow
df = pd.DataFrame({'a': [2, 2, 2, 1, 1, 1], 'b': [1, 2, 3, 3, 2, 1]})
```

## Next Steps


---

*Source: test_nlargest.py:128 | Complexity: Beginner | Last updated: 2026-06-02*
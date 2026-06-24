# How To: Index Name Retained

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate DataFrame: test index name retained

## Prerequisites

**Required Modules:**
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df_expected = pd.DataFrame(...)

```python
df_expected = pd.DataFrame({'x': [1, 2, 6, 9], 'y': [2, 2, 8, 10], 'z': [-5, 0, 5, 10]})
```


## Complete Example

```python
# Workflow
df_expected = pd.DataFrame({'x': [1, 2, 6, 9], 'y': [2, 2, 8, 10], 'z': [-5, 0, 5, 10]})
```

## Next Steps


---

*Source: test_names.py:22 | Complexity: Beginner | Last updated: 2026-06-02*
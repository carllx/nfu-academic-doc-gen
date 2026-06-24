# How To: Data Frame Value Counts Default

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate Series: test data frame value counts default

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign expected = pd.Series(...)

```python
expected = pd.Series(data=[2, 1, 1], index=pd.MultiIndex.from_arrays([(4, 2, 6), (0, 2, 0)], names=['num_legs', 'num_wings']), name='count')
```


## Complete Example

```python
# Workflow
expected = pd.Series(data=[2, 1, 1], index=pd.MultiIndex.from_arrays([(4, 2, 6), (0, 2, 0)], names=['num_legs', 'num_wings']), name='count')
```

## Next Steps


---

*Source: test_value_counts.py:51 | Complexity: Beginner | Last updated: 2026-06-02*
# How To: Plotting With Float Index Works Apply

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate DataFrame: test plotting with float index works apply

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas.tests.plotting.common`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'def': [1, 1, 1, 2, 2, 2, 3, 3, 3], 'val': np.random.default_rng(2).standard_normal(9)}, index=[1.0, 2.0, 3.0, 1.0, 2.0, 3.0, 1.0, 2.0, 3.0])
```


## Complete Example

```python
# Workflow
df = DataFrame({'def': [1, 1, 1, 2, 2, 2, 3, 3, 3], 'val': np.random.default_rng(2).standard_normal(9)}, index=[1.0, 2.0, 3.0, 1.0, 2.0, 3.0, 1.0, 2.0, 3.0])
```

## Next Steps


---

*Source: test_groupby.py:55 | Complexity: Beginner | Last updated: 2026-06-02*
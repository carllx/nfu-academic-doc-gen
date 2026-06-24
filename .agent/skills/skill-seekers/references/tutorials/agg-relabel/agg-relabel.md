# How To: Agg Relabel

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate DataFrame: test agg relabel

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat.numpy`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame({'A': [1, 2, 1, 2], 'B': [1, 2, 3, 4], 'C': [3, 4, 5, 6]})
```


## Complete Example

```python
# Workflow
df = pd.DataFrame({'A': [1, 2, 1, 2], 'B': [1, 2, 3, 4], 'C': [3, 4, 5, 6]})
```

## Next Steps


---

*Source: test_frame_apply_relabeling.py:12 | Complexity: Beginner | Last updated: 2026-06-02*
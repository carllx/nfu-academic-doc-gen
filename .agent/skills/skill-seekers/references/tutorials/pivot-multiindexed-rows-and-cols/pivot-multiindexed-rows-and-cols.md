# How To: Pivot Multiindexed Rows And Cols

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate DataFrame: test pivot multiindexed rows and cols

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: using_array_manager
```

## Step-by-Step Guide

### Step 1: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame(data=np.arange(12).reshape(4, 3), columns=MultiIndex.from_tuples([(0, 0), (0, 1), (0, 2)], names=['col_L0', 'col_L1']), index=MultiIndex.from_tuples([(0, 0, 0), (0, 0, 1), (1, 1, 1), (1, 0, 0)], names=['idx_L0', 'idx_L1', 'idx_L2']))
```


## Complete Example

```python
# Setup
# Fixtures: using_array_manager

# Workflow
df = pd.DataFrame(data=np.arange(12).reshape(4, 3), columns=MultiIndex.from_tuples([(0, 0), (0, 1), (0, 2)], names=['col_L0', 'col_L1']), index=MultiIndex.from_tuples([(0, 0, 0), (0, 0, 1), (1, 1, 1), (1, 0, 0)], names=['idx_L0', 'idx_L1', 'idx_L2']))
```

## Next Steps


---

*Source: test_pivot_multilevel.py:203 | Complexity: Beginner | Last updated: 2026-06-02*
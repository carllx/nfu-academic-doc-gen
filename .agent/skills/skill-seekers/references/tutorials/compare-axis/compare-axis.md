# How To: Compare Axis

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: pytest

## Overview

Instantiate DataFrame: test compare axis

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat.numpy`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: align_axis
```

## Step-by-Step Guide

### Step 1: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame({'col1': ['a', 'b', 'c'], 'col2': [1.0, 2.0, np.nan], 'col3': [1.0, 2.0, 3.0]}, columns=['col1', 'col2', 'col3'])
```


## Complete Example

```python
# Setup
# Fixtures: align_axis

# Workflow
df = pd.DataFrame({'col1': ['a', 'b', 'c'], 'col2': [1.0, 2.0, np.nan], 'col3': [1.0, 2.0, 3.0]}, columns=['col1', 'col2', 'col3'])
```

## Next Steps


---

*Source: test_compare.py:13 | Complexity: Beginner | Last updated: 2026-06-02*
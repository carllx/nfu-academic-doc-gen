# How To: Sort Values Nonsortedindex

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sort values nonsortedindex

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign rng = date_range(...)

```python
rng = date_range('2011-01-01', '2012-01-01', freq='W')
```

### Step 2: Assign ts = DataFrame(...)

```python
ts = DataFrame({'A': np.random.default_rng(2).standard_normal(len(rng)), 'B': np.random.default_rng(2).standard_normal(len(rng))}, index=rng)
```

### Step 3: Assign decreasing = ts.sort_values(...)

```python
decreasing = ts.sort_values('A', ascending=False)
```

### Step 4: Assign msg = 'truncate requires a sorted index'

```python
msg = 'truncate requires a sorted index'
```

### Step 5: Call decreasing.truncate()

```python
decreasing.truncate(before='2011-11', after='2011-12')
```


## Complete Example

```python
# Workflow
rng = date_range('2011-01-01', '2012-01-01', freq='W')
ts = DataFrame({'A': np.random.default_rng(2).standard_normal(len(rng)), 'B': np.random.default_rng(2).standard_normal(len(rng))}, index=rng)
decreasing = ts.sort_values('A', ascending=False)
msg = 'truncate requires a sorted index'
with pytest.raises(ValueError, match=msg):
    decreasing.truncate(before='2011-11', after='2011-12')
```

## Next Steps


---

*Source: test_truncate.py:79 | Complexity: Intermediate | Last updated: 2026-06-02*
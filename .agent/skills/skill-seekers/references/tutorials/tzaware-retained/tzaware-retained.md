# How To: Tzaware Retained

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test tzaware retained

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.reshape.util`


## Step-by-Step Guide

### Step 1: Assign x = date_range(...)

```python
x = date_range('2000-01-01', periods=2, tz='US/Pacific')
```

### Step 2: Assign y = np.array(...)

```python
y = np.array([3, 4])
```

### Step 3: Assign unknown = cartesian_product(...)

```python
result1, result2 = cartesian_product([x, y])
```

### Step 4: Assign expected = x.repeat(...)

```python
expected = x.repeat(2)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result1, expected)
```


## Complete Example

```python
# Workflow
x = date_range('2000-01-01', periods=2, tz='US/Pacific')
y = np.array([3, 4])
result1, result2 = cartesian_product([x, y])
expected = x.repeat(2)
tm.assert_index_equal(result1, expected)
```

## Next Steps


---

*Source: test_util.py:31 | Complexity: Intermediate | Last updated: 2026-06-02*
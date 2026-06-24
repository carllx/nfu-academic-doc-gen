# How To: Pi Shift Ndarray

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test pi shift ndarray

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = PeriodIndex(...)

```python
idx = PeriodIndex(['2011-01', '2011-02', 'NaT', '2011-04'], freq='M', name='idx')
```

### Step 2: Assign result = idx.shift(...)

```python
result = idx.shift(np.array([1, 2, 3, 4]))
```

### Step 3: Assign expected = PeriodIndex(...)

```python
expected = PeriodIndex(['2011-02', '2011-04', 'NaT', '2011-08'], freq='M', name='idx')
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 5: Assign result = idx.shift(...)

```python
result = idx.shift(np.array([1, -2, 3, -4]))
```

### Step 6: Assign expected = PeriodIndex(...)

```python
expected = PeriodIndex(['2011-02', '2010-12', 'NaT', '2010-12'], freq='M', name='idx')
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
idx = PeriodIndex(['2011-01', '2011-02', 'NaT', '2011-04'], freq='M', name='idx')
result = idx.shift(np.array([1, 2, 3, 4]))
expected = PeriodIndex(['2011-02', '2011-04', 'NaT', '2011-08'], freq='M', name='idx')
tm.assert_index_equal(result, expected)
result = idx.shift(np.array([1, -2, 3, -4]))
expected = PeriodIndex(['2011-02', '2010-12', 'NaT', '2010-12'], freq='M', name='idx')
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_shift.py:15 | Complexity: Intermediate | Last updated: 2026-06-02*
# How To: Getitem Index

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test getitem index

## Prerequisites

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = period_range(...)

```python
idx = period_range('2007-01', periods=10, freq='M', name='x')
```

### Step 2: Assign result = value

```python
result = idx[[1, 3, 5]]
```

### Step 3: Assign exp = PeriodIndex(...)

```python
exp = PeriodIndex(['2007-02', '2007-04', '2007-06'], freq='M', name='x')
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, exp)
```

### Step 5: Assign result = value

```python
result = idx[[True, True, False, False, False, True, True, False, False, False]]
```

### Step 6: Assign exp = PeriodIndex(...)

```python
exp = PeriodIndex(['2007-01', '2007-02', '2007-06', '2007-07'], freq='M', name='x')
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, exp)
```


## Complete Example

```python
# Workflow
idx = period_range('2007-01', periods=10, freq='M', name='x')
result = idx[[1, 3, 5]]
exp = PeriodIndex(['2007-02', '2007-04', '2007-06'], freq='M', name='x')
tm.assert_index_equal(result, exp)
result = idx[[True, True, False, False, False, True, True, False, False, False]]
exp = PeriodIndex(['2007-01', '2007-02', '2007-06', '2007-07'], freq='M', name='x')
tm.assert_index_equal(result, exp)
```

## Next Steps


---

*Source: test_indexing.py:98 | Complexity: Intermediate | Last updated: 2026-06-02*
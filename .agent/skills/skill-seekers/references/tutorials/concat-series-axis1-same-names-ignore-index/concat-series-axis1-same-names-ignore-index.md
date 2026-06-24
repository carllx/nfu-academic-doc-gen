# How To: Concat Series Axis1 Same Names Ignore Index

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat series axis1 same names ignore index

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dates = value

```python
dates = date_range('01-Jan-2013', '01-Jan-2014', freq='MS')[0:-1]
```

### Step 2: Assign s1 = Series(...)

```python
s1 = Series(np.random.default_rng(2).standard_normal(len(dates)), index=dates, name='value')
```

### Step 3: Assign s2 = Series(...)

```python
s2 = Series(np.random.default_rng(2).standard_normal(len(dates)), index=dates, name='value')
```

### Step 4: Assign result = concat(...)

```python
result = concat([s1, s2], axis=1, ignore_index=True)
```

### Step 5: Assign expected = Index(...)

```python
expected = Index(range(2))
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result.columns, expected, exact=True)
```


## Complete Example

```python
# Workflow
dates = date_range('01-Jan-2013', '01-Jan-2014', freq='MS')[0:-1]
s1 = Series(np.random.default_rng(2).standard_normal(len(dates)), index=dates, name='value')
s2 = Series(np.random.default_rng(2).standard_normal(len(dates)), index=dates, name='value')
result = concat([s1, s2], axis=1, ignore_index=True)
expected = Index(range(2))
tm.assert_index_equal(result.columns, expected, exact=True)
```

## Next Steps


---

*Source: test_series.py:113 | Complexity: Intermediate | Last updated: 2026-06-02*
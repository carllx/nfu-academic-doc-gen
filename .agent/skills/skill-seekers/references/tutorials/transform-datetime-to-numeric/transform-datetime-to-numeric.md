# How To: Transform Datetime To Numeric

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test transform datetime to numeric

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.groupby`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': 1, 'b': date_range('2015-01-01', periods=2, freq='D')})
```

### Step 2: Assign result = df.groupby.b.transform(...)

```python
result = df.groupby('a').b.transform(lambda x: x.dt.dayofweek - x.dt.dayofweek.mean())
```

### Step 3: Assign expected = Series(...)

```python
expected = Series([-0.5, 0.5], name='b')
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign df = DataFrame(...)

```python
df = DataFrame({'a': 1, 'b': date_range('2015-01-01', periods=2, freq='D')})
```

### Step 6: Assign result = df.groupby.b.transform(...)

```python
result = df.groupby('a').b.transform(lambda x: x.dt.dayofweek - x.dt.dayofweek.min())
```

### Step 7: Assign expected = Series(...)

```python
expected = Series([0, 1], dtype=np.int32, name='b')
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'a': 1, 'b': date_range('2015-01-01', periods=2, freq='D')})
result = df.groupby('a').b.transform(lambda x: x.dt.dayofweek - x.dt.dayofweek.mean())
expected = Series([-0.5, 0.5], name='b')
tm.assert_series_equal(result, expected)
df = DataFrame({'a': 1, 'b': date_range('2015-01-01', periods=2, freq='D')})
result = df.groupby('a').b.transform(lambda x: x.dt.dayofweek - x.dt.dayofweek.min())
expected = Series([0, 1], dtype=np.int32, name='b')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_transform.py:332 | Complexity: Advanced | Last updated: 2026-06-02*
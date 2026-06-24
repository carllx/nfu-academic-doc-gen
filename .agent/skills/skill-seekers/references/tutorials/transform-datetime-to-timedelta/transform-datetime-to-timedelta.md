# How To: Transform Datetime To Timedelta

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test transform datetime to timedelta

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
df = DataFrame({'A': Timestamp('20130101'), 'B': np.arange(5)})
```

### Step 2: Assign expected = Series(...)

```python
expected = Series(Timestamp('20130101') - Timestamp('20130101'), index=range(5), name='A')
```

### Step 3: Assign base_time = value

```python
base_time = df['A'][0]
```

### Step 4: Assign result = value

```python
result = df.groupby('A')['A'].transform(lambda x: x.max() - x.min() + base_time) - base_time
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign result = unknown.transform(...)

```python
result = df.groupby('A')['A'].transform(lambda x: x.max() - x.min())
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': Timestamp('20130101'), 'B': np.arange(5)})
expected = Series(Timestamp('20130101') - Timestamp('20130101'), index=range(5), name='A')
base_time = df['A'][0]
result = df.groupby('A')['A'].transform(lambda x: x.max() - x.min() + base_time) - base_time
tm.assert_series_equal(result, expected)
result = df.groupby('A')['A'].transform(lambda x: x.max() - x.min())
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_transform.py:311 | Complexity: Intermediate | Last updated: 2026-06-02*
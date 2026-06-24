# How To: Reset Index Multiindex Nat

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reset index multiindex nat

## Prerequisites

**Required Modules:**
- `datetime`
- `itertools`
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = range(...)

```python
idx = range(3)
```

### Step 2: Assign tstamp = date_range(...)

```python
tstamp = date_range('2015-07-01', freq='D', periods=3)
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame({'id': idx, 'tstamp': tstamp, 'a': list('abc')})
```

### Step 4: Assign unknown = value

```python
df.loc[2, 'tstamp'] = pd.NaT
```

### Step 5: Assign result = df.set_index.reset_index(...)

```python
result = df.set_index(['id', 'tstamp']).reset_index('id')
```

### Step 6: Assign exp_dti = pd.DatetimeIndex(...)

```python
exp_dti = pd.DatetimeIndex(['2015-07-01', '2015-07-02', 'NaT'], dtype='M8[ns]', name='tstamp')
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame({'id': range(3), 'a': list('abc')}, index=exp_dti)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
idx = range(3)
tstamp = date_range('2015-07-01', freq='D', periods=3)
df = DataFrame({'id': idx, 'tstamp': tstamp, 'a': list('abc')})
df.loc[2, 'tstamp'] = pd.NaT
result = df.set_index(['id', 'tstamp']).reset_index('id')
exp_dti = pd.DatetimeIndex(['2015-07-01', '2015-07-02', 'NaT'], dtype='M8[ns]', name='tstamp')
expected = DataFrame({'id': range(3), 'a': list('abc')}, index=exp_dti)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_reset_index.py:701 | Complexity: Advanced | Last updated: 2026-06-02*
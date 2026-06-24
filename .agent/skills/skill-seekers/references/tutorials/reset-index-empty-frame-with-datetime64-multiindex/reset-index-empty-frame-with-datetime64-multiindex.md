# How To: Reset Index Empty Frame With Datetime64 Multiindex

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reset index empty frame with datetime64 multiindex

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

### Step 1: Assign dti = pd.DatetimeIndex(...)

```python
dti = pd.DatetimeIndex(['2020-07-20 00:00:00'], dtype='M8[ns]')
```

### Step 2: Assign idx = value

```python
idx = MultiIndex.from_product([dti, [3, 4]], names=['a', 'b'])[:0]
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(index=idx, columns=['c', 'd'])
```

### Step 4: Assign result = df.reset_index(...)

```python
result = df.reset_index()
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame(columns=list('abcd'), index=RangeIndex(start=0, stop=0, step=1))
```

### Step 6: Assign unknown = unknown.astype(...)

```python
expected['a'] = expected['a'].astype('datetime64[ns]')
```

### Step 7: Assign unknown = unknown.astype(...)

```python
expected['b'] = expected['b'].astype('int64')
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
dti = pd.DatetimeIndex(['2020-07-20 00:00:00'], dtype='M8[ns]')
idx = MultiIndex.from_product([dti, [3, 4]], names=['a', 'b'])[:0]
df = DataFrame(index=idx, columns=['c', 'd'])
result = df.reset_index()
expected = DataFrame(columns=list('abcd'), index=RangeIndex(start=0, stop=0, step=1))
expected['a'] = expected['a'].astype('datetime64[ns]')
expected['b'] = expected['b'].astype('int64')
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_reset_index.py:669 | Complexity: Advanced | Last updated: 2026-06-02*
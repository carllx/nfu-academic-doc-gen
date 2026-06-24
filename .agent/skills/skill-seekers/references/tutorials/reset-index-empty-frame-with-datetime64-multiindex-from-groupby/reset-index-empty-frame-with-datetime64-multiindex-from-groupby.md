# How To: Reset Index Empty Frame With Datetime64 Multiindex From Groupby

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reset index empty frame with datetime64 multiindex from groupby

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `itertools`
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign dti = pd.DatetimeIndex(...)

```python
dti = pd.DatetimeIndex(['2020-01-01'], dtype='M8[ns]')
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'c1': [10.0], 'c2': ['a'], 'c3': dti})
```

### Step 3: Assign df = unknown.sum(...)

```python
df = df.head(0).groupby(['c2', 'c3'])[['c1']].sum()
```

### Step 4: Assign result = df.reset_index(...)

```python
result = df.reset_index()
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame(columns=['c2', 'c3', 'c1'], index=RangeIndex(start=0, stop=0, step=1))
```

### Step 6: Assign unknown = unknown.astype(...)

```python
expected['c3'] = expected['c3'].astype('datetime64[ns]')
```

### Step 7: Assign unknown = unknown.astype(...)

```python
expected['c1'] = expected['c1'].astype('float64')
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 9: Assign unknown = unknown.astype(...)

```python
expected['c2'] = expected['c2'].astype('str')
```


## Complete Example

```python
# Setup
# Fixtures: using_infer_string

# Workflow
dti = pd.DatetimeIndex(['2020-01-01'], dtype='M8[ns]')
df = DataFrame({'c1': [10.0], 'c2': ['a'], 'c3': dti})
df = df.head(0).groupby(['c2', 'c3'])[['c1']].sum()
result = df.reset_index()
expected = DataFrame(columns=['c2', 'c3', 'c1'], index=RangeIndex(start=0, stop=0, step=1))
expected['c3'] = expected['c3'].astype('datetime64[ns]')
expected['c1'] = expected['c1'].astype('float64')
if using_infer_string:
    expected['c2'] = expected['c2'].astype('str')
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_reset_index.py:683 | Complexity: Advanced | Last updated: 2026-06-02*
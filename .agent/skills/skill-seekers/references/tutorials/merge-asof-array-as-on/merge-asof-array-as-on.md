# How To: Merge Asof Array As On

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test merge asof array as on

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pytz`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.reshape.merge`

**Setup Required:**
```python
# Fixtures: unit
```

## Step-by-Step Guide

### Step 1: Assign dti = pd.DatetimeIndex(...)

```python
dti = pd.DatetimeIndex(['2021/01/01 00:37', '2021/01/01 01:40'], dtype=f'M8[{unit}]')
```

### Step 2: Assign right = pd.DataFrame(...)

```python
right = pd.DataFrame({'a': [2, 6], 'ts': dti})
```

### Step 3: Assign ts_merge = pd.date_range(...)

```python
ts_merge = pd.date_range(start=pd.Timestamp('2021/01/01 00:00'), periods=3, freq='1h', unit=unit)
```

### Step 4: Assign left = pd.DataFrame(...)

```python
left = pd.DataFrame({'b': [4, 8, 7]})
```

### Step 5: Assign result = merge_asof(...)

```python
result = merge_asof(left, right, left_on=ts_merge, right_on='ts', allow_exact_matches=False, direction='backward')
```

### Step 6: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'b': [4, 8, 7], 'a': [np.nan, 2, 6], 'ts': ts_merge})
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign result = merge_asof(...)

```python
result = merge_asof(right, left, left_on='ts', right_on=ts_merge, allow_exact_matches=False, direction='backward')
```

### Step 9: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'a': [2, 6], 'ts': dti, 'b': [4, 8]})
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: unit

# Workflow
dti = pd.DatetimeIndex(['2021/01/01 00:37', '2021/01/01 01:40'], dtype=f'M8[{unit}]')
right = pd.DataFrame({'a': [2, 6], 'ts': dti})
ts_merge = pd.date_range(start=pd.Timestamp('2021/01/01 00:00'), periods=3, freq='1h', unit=unit)
left = pd.DataFrame({'b': [4, 8, 7]})
result = merge_asof(left, right, left_on=ts_merge, right_on='ts', allow_exact_matches=False, direction='backward')
expected = pd.DataFrame({'b': [4, 8, 7], 'a': [np.nan, 2, 6], 'ts': ts_merge})
tm.assert_frame_equal(result, expected)
result = merge_asof(right, left, left_on='ts', right_on=ts_merge, allow_exact_matches=False, direction='backward')
expected = pd.DataFrame({'a': [2, 6], 'ts': dti, 'b': [4, 8]})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_merge_asof.py:3489 | Complexity: Advanced | Last updated: 2026-06-02*
# How To: Min Max

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test min max

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: left_right_dtypes, index_or_series_or_array
```

## Step-by-Step Guide

### Step 1: Assign unknown = left_right_dtypes

```python
left, right = left_right_dtypes
```

**Verification:**
```python
assert left.is_monotonic_increasing
```

### Step 2: Assign left = left.copy(...)

```python
left = left.copy(deep=True)
```

**Verification:**
```python
assert Index(arr).is_monotonic_increasing
```

### Step 3: Assign right = right.copy(...)

```python
right = right.copy(deep=True)
```

**Verification:**
```python
assert res == MIN
```

### Step 4: Assign arr = IntervalArray.from_arrays(...)

```python
arr = IntervalArray.from_arrays(left, right)
```

**Verification:**
```python
assert type(res) == type(MIN)
```

### Step 5: Assign MIN = value

```python
MIN = arr[0]
```

**Verification:**
```python
assert res == MAX
```

### Step 6: Assign MAX = value

```python
MAX = arr[-1]
```

**Verification:**
```python
assert type(res) == type(MAX)
```

### Step 7: Assign indexer = np.arange(...)

```python
indexer = np.arange(len(arr))
```

**Verification:**
```python
assert np.isnan(res)
```

### Step 8: Call np.random.default_rng.shuffle()

```python
np.random.default_rng(2).shuffle(indexer)
```

**Verification:**
```python
assert np.isnan(res)
```

### Step 9: Assign arr = arr.take(...)

```python
arr = arr.take(indexer)
```

**Verification:**
```python
assert res == MIN
```

### Step 10: Assign arr_na = arr.insert(...)

```python
arr_na = arr.insert(2, np.nan)
```

**Verification:**
```python
assert type(res) == type(MIN)
```

### Step 11: Assign arr = index_or_series_or_array(...)

```python
arr = index_or_series_or_array(arr)
```

**Verification:**
```python
assert res == MAX
```

### Step 12: Assign arr_na = index_or_series_or_array(...)

```python
arr_na = index_or_series_or_array(arr_na)
```

**Verification:**
```python
assert type(res) == type(MAX)
```

### Step 13: Assign res = arr_na.min(...)

```python
res = arr_na.min(skipna=False)
```

**Verification:**
```python
assert np.isnan(res)
```

### Step 14: Assign res = arr_na.max(...)

```python
res = arr_na.max(skipna=False)
```

**Verification:**
```python
assert np.isnan(res)
```

### Step 15: Assign res = arr_na.min(...)

```python
res = arr_na.min(skipna=True)
```

**Verification:**
```python
assert res == MIN
```

### Step 16: Assign res = arr_na.max(...)

```python
res = arr_na.max(skipna=True)
```

**Verification:**
```python
assert res == MAX
```

### Step 17: Assign res = arr.min(...)

```python
res = arr.min(skipna=skipna)
```

**Verification:**
```python
assert res == MIN
```

### Step 18: Assign res = arr.max(...)

```python
res = arr.max(skipna=skipna)
```

**Verification:**
```python
assert res == MAX
```


## Complete Example

```python
# Setup
# Fixtures: left_right_dtypes, index_or_series_or_array

# Workflow
left, right = left_right_dtypes
left = left.copy(deep=True)
right = right.copy(deep=True)
arr = IntervalArray.from_arrays(left, right)
assert left.is_monotonic_increasing
assert Index(arr).is_monotonic_increasing
MIN = arr[0]
MAX = arr[-1]
indexer = np.arange(len(arr))
np.random.default_rng(2).shuffle(indexer)
arr = arr.take(indexer)
arr_na = arr.insert(2, np.nan)
arr = index_or_series_or_array(arr)
arr_na = index_or_series_or_array(arr_na)
for skipna in [True, False]:
    res = arr.min(skipna=skipna)
    assert res == MIN
    assert type(res) == type(MIN)
    res = arr.max(skipna=skipna)
    assert res == MAX
    assert type(res) == type(MAX)
res = arr_na.min(skipna=False)
assert np.isnan(res)
res = arr_na.max(skipna=False)
assert np.isnan(res)
res = arr_na.min(skipna=True)
assert res == MIN
assert type(res) == type(MIN)
res = arr_na.max(skipna=True)
assert res == MAX
assert type(res) == type(MAX)
```

## Next Steps


---

*Source: test_interval.py:189 | Complexity: Advanced | Last updated: 2026-06-02*
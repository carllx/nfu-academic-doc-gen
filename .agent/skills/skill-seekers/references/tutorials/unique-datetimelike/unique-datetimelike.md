# How To: Unique Datetimelike

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test unique datetimelike

## Prerequisites

**Required Modules:**
- `itertools`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx1 = DatetimeIndex(...)

```python
idx1 = DatetimeIndex(['2015-01-01', '2015-01-01', '2015-01-01', '2015-01-01', 'NaT', 'NaT'])
```

### Step 2: Assign idx2 = DatetimeIndex(...)

```python
idx2 = DatetimeIndex(['2015-01-01', '2015-01-01', '2015-01-02', '2015-01-02', 'NaT', '2015-01-01'], tz='Asia/Tokyo')
```

### Step 3: Assign result = MultiIndex.from_arrays.unique(...)

```python
result = MultiIndex.from_arrays([idx1, idx2]).unique()
```

### Step 4: Assign eidx1 = DatetimeIndex(...)

```python
eidx1 = DatetimeIndex(['2015-01-01', '2015-01-01', 'NaT', 'NaT'])
```

### Step 5: Assign eidx2 = DatetimeIndex(...)

```python
eidx2 = DatetimeIndex(['2015-01-01', '2015-01-02', 'NaT', '2015-01-01'], tz='Asia/Tokyo')
```

### Step 6: Assign exp = MultiIndex.from_arrays(...)

```python
exp = MultiIndex.from_arrays([eidx1, eidx2])
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, exp)
```


## Complete Example

```python
# Workflow
idx1 = DatetimeIndex(['2015-01-01', '2015-01-01', '2015-01-01', '2015-01-01', 'NaT', 'NaT'])
idx2 = DatetimeIndex(['2015-01-01', '2015-01-01', '2015-01-02', '2015-01-02', 'NaT', '2015-01-01'], tz='Asia/Tokyo')
result = MultiIndex.from_arrays([idx1, idx2]).unique()
eidx1 = DatetimeIndex(['2015-01-01', '2015-01-01', 'NaT', 'NaT'])
eidx2 = DatetimeIndex(['2015-01-01', '2015-01-02', 'NaT', '2015-01-01'], tz='Asia/Tokyo')
exp = MultiIndex.from_arrays([eidx1, eidx2])
tm.assert_index_equal(result, exp)
```

## Next Steps


---

*Source: test_duplicates.py:63 | Complexity: Intermediate | Last updated: 2026-06-02*
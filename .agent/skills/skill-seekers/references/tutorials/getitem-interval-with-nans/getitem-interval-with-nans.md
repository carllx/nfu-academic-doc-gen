# How To: Getitem Interval With Nans

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test getitem interval with nans

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: frame_or_series, indexer_sl
```

## Step-by-Step Guide

### Step 1: Assign index = IntervalIndex(...)

```python
index = IntervalIndex([np.nan, np.nan])
```

### Step 2: Assign key = value

```python
key = index[:-1]
```

### Step 3: Assign obj = frame_or_series(...)

```python
obj = frame_or_series(range(2), index=index)
```

### Step 4: Assign result = value

```python
result = indexer_sl(obj)[key]
```

### Step 5: Assign expected = obj

```python
expected = obj
```

### Step 6: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 7: Assign obj = value

```python
obj = obj.T
```


## Complete Example

```python
# Setup
# Fixtures: frame_or_series, indexer_sl

# Workflow
index = IntervalIndex([np.nan, np.nan])
key = index[:-1]
obj = frame_or_series(range(2), index=index)
if frame_or_series is DataFrame and indexer_sl is tm.setitem:
    obj = obj.T
result = indexer_sl(obj)[key]
expected = obj
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_interval.py:125 | Complexity: Intermediate | Last updated: 2026-06-02*
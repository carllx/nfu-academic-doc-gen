# How To: Loc With Slices

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test loc with slices

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: series_with_interval_index, indexer_sl
```

## Step-by-Step Guide

### Step 1: Assign ser = series_with_interval_index.copy(...)

```python
ser = series_with_interval_index.copy()
```

### Step 2: Assign expected = value

```python
expected = ser.iloc[:3]
```

### Step 3: Assign result = value

```python
result = indexer_sl(ser)[Interval(0, 1):Interval(2, 3)]
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, result)
```

### Step 5: Assign expected = value

```python
expected = ser.iloc[3:]
```

### Step 6: Assign result = value

```python
result = indexer_sl(ser)[Interval(3, 4):]
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, result)
```

### Step 8: Assign msg = 'Interval objects are not currently supported'

```python
msg = 'Interval objects are not currently supported'
```

### Step 9: indexer_sl(ser)[Interval(3, 6):]

```python
indexer_sl(ser)[Interval(3, 6):]
```

### Step 10: indexer_sl(ser)[Interval(3, 4, closed='left'):]

```python
indexer_sl(ser)[Interval(3, 4, closed='left'):]
```


## Complete Example

```python
# Setup
# Fixtures: series_with_interval_index, indexer_sl

# Workflow
ser = series_with_interval_index.copy()
expected = ser.iloc[:3]
result = indexer_sl(ser)[Interval(0, 1):Interval(2, 3)]
tm.assert_series_equal(expected, result)
expected = ser.iloc[3:]
result = indexer_sl(ser)[Interval(3, 4):]
tm.assert_series_equal(expected, result)
msg = 'Interval objects are not currently supported'
with pytest.raises(NotImplementedError, match=msg):
    indexer_sl(ser)[Interval(3, 6):]
with pytest.raises(NotImplementedError, match=msg):
    indexer_sl(ser)[Interval(3, 4, closed='left'):]
```

## Next Steps


---

*Source: test_interval_new.py:72 | Complexity: Advanced | Last updated: 2026-06-02*
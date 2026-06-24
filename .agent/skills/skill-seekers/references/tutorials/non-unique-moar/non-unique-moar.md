# How To: Non Unique Moar

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test non unique moar

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
# Fixtures: indexer_sl
```

## Step-by-Step Guide

### Step 1: Assign idx = IntervalIndex.from_tuples(...)

```python
idx = IntervalIndex.from_tuples([(1, 3), (1, 3), (3, 7)])
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(range(len(idx)), index=idx)
```

### Step 3: Assign expected = value

```python
expected = ser.iloc[[0, 1]]
```

### Step 4: Assign result = value

```python
result = indexer_sl(ser)[Interval(1, 3)]
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, result)
```

### Step 6: Assign expected = ser

```python
expected = ser
```

### Step 7: Assign result = value

```python
result = indexer_sl(ser)[Interval(1, 3):]
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, result)
```

### Step 9: Assign expected = value

```python
expected = ser.iloc[[0, 1]]
```

### Step 10: Assign result = value

```python
result = indexer_sl(ser)[[Interval(1, 3)]]
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, result)
```


## Complete Example

```python
# Setup
# Fixtures: indexer_sl

# Workflow
idx = IntervalIndex.from_tuples([(1, 3), (1, 3), (3, 7)])
ser = Series(range(len(idx)), index=idx)
expected = ser.iloc[[0, 1]]
result = indexer_sl(ser)[Interval(1, 3)]
tm.assert_series_equal(expected, result)
expected = ser
result = indexer_sl(ser)[Interval(1, 3):]
tm.assert_series_equal(expected, result)
expected = ser.iloc[[0, 1]]
result = indexer_sl(ser)[[Interval(1, 3)]]
tm.assert_series_equal(expected, result)
```

## Next Steps


---

*Source: test_interval_new.py:186 | Complexity: Advanced | Last updated: 2026-06-02*
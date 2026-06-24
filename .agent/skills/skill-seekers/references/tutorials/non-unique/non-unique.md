# How To: Non Unique

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test non unique

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
idx = IntervalIndex.from_tuples([(1, 3), (3, 7)])
```

**Verification:**
```python
assert result == 0
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(range(len(idx)), index=idx)
```

### Step 3: Assign result = value

```python
result = indexer_sl(ser)[Interval(1, 3)]
```

**Verification:**
```python
assert result == 0
```

### Step 4: Assign result = value

```python
result = indexer_sl(ser)[[Interval(1, 3)]]
```

### Step 5: Assign expected = value

```python
expected = ser.iloc[0:1]
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, result)
```


## Complete Example

```python
# Setup
# Fixtures: indexer_sl

# Workflow
idx = IntervalIndex.from_tuples([(1, 3), (3, 7)])
ser = Series(range(len(idx)), index=idx)
result = indexer_sl(ser)[Interval(1, 3)]
assert result == 0
result = indexer_sl(ser)[[Interval(1, 3)]]
expected = ser.iloc[0:1]
tm.assert_series_equal(expected, result)
```

## Next Steps


---

*Source: test_interval_new.py:175 | Complexity: Intermediate | Last updated: 2026-06-02*
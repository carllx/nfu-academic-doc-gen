# How To: Loc With Scalar

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test loc with scalar

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

**Verification:**
```python
assert indexer_sl(ser)[1] == 0
```

### Step 2: Assign expected = value

```python
expected = ser.iloc[1:4]
```

**Verification:**
```python
assert indexer_sl(ser)[1.5] == 1
```

### Step 3: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, indexer_sl(ser)[[1.5, 2.5, 3.5]])
```

**Verification:**
```python
assert indexer_sl(ser)[2] == 1
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, indexer_sl(ser)[[2, 3, 4]])
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, indexer_sl(ser)[[1.5, 3, 4]])
```

### Step 6: Assign expected = value

```python
expected = ser.iloc[[1, 1, 2, 1]]
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, indexer_sl(ser)[[1.5, 2, 2.5, 1.5]])
```

### Step 8: Assign expected = value

```python
expected = ser.iloc[2:5]
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, indexer_sl(ser)[ser >= 2])
```


## Complete Example

```python
# Setup
# Fixtures: series_with_interval_index, indexer_sl

# Workflow
ser = series_with_interval_index.copy()
assert indexer_sl(ser)[1] == 0
assert indexer_sl(ser)[1.5] == 1
assert indexer_sl(ser)[2] == 1
expected = ser.iloc[1:4]
tm.assert_series_equal(expected, indexer_sl(ser)[[1.5, 2.5, 3.5]])
tm.assert_series_equal(expected, indexer_sl(ser)[[2, 3, 4]])
tm.assert_series_equal(expected, indexer_sl(ser)[[1.5, 3, 4]])
expected = ser.iloc[[1, 1, 2, 1]]
tm.assert_series_equal(expected, indexer_sl(ser)[[1.5, 2, 2.5, 1.5]])
expected = ser.iloc[2:5]
tm.assert_series_equal(expected, indexer_sl(ser)[ser >= 2])
```

## Next Steps


---

*Source: test_interval_new.py:50 | Complexity: Advanced | Last updated: 2026-06-02*
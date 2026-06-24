# How To: Getitem With Scalar

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test getitem with scalar

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

### Step 3: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, indexer_sl(ser)[:3])
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, indexer_sl(ser)[:2.5])
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, indexer_sl(ser)[0.1:2.5])
```

### Step 6: Assign expected = value

```python
expected = ser.iloc[1:4]
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, indexer_sl(ser)[[1.5, 2.5, 3.5]])
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, indexer_sl(ser)[[2, 3, 4]])
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, indexer_sl(ser)[[1.5, 3, 4]])
```

### Step 10: Assign expected = value

```python
expected = ser.iloc[2:5]
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, indexer_sl(ser)[ser >= 2])
```

### Step 12: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, ser.loc[-1:3])
```


## Complete Example

```python
# Setup
# Fixtures: series_with_interval_index, indexer_sl

# Workflow
ser = series_with_interval_index.copy()
expected = ser.iloc[:3]
tm.assert_series_equal(expected, indexer_sl(ser)[:3])
tm.assert_series_equal(expected, indexer_sl(ser)[:2.5])
tm.assert_series_equal(expected, indexer_sl(ser)[0.1:2.5])
if indexer_sl is tm.loc:
    tm.assert_series_equal(expected, ser.loc[-1:3])
expected = ser.iloc[1:4]
tm.assert_series_equal(expected, indexer_sl(ser)[[1.5, 2.5, 3.5]])
tm.assert_series_equal(expected, indexer_sl(ser)[[2, 3, 4]])
tm.assert_series_equal(expected, indexer_sl(ser)[[1.5, 3, 4]])
expected = ser.iloc[2:5]
tm.assert_series_equal(expected, indexer_sl(ser)[ser >= 2])
```

## Next Steps


---

*Source: test_interval.py:20 | Complexity: Advanced | Last updated: 2026-06-02*
# How To: Indexing With Datetimeindex Tz

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test indexing with datetimeindex tz

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: indexer_sl
```

## Step-by-Step Guide

### Step 1: Assign index = date_range(...)

```python
index = date_range('2015-01-01', periods=2, tz='utc')
```

**Verification:**
```python
assert indexer_sl(ser)[index[1]] == 1
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(range(2), index=index, dtype='int64')
```

**Verification:**
```python
assert indexer_sl(ser)[index[1]] == 1
```

### Step 3: Assign result = ser.copy(...)

```python
result = ser.copy()
```

### Step 4: Assign unknown = 5

```python
indexer_sl(result)[index[1]] = 5
```

### Step 5: Assign expected = Series(...)

```python
expected = Series([0, 5], index=index)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 7: Assign result = value

```python
result = indexer_sl(ser)[sel]
```

### Step 8: Assign expected = ser.copy(...)

```python
expected = ser.copy()
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 10: Assign result = ser.copy(...)

```python
result = ser.copy()
```

### Step 11: Assign unknown = 1

```python
indexer_sl(result)[sel] = 1
```

### Step 12: Assign expected = Series(...)

```python
expected = Series(1, index=index)
```

### Step 13: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 14: Assign expected.index = expected.index._with_freq(...)

```python
expected.index = expected.index._with_freq(None)
```


## Complete Example

```python
# Setup
# Fixtures: indexer_sl

# Workflow
index = date_range('2015-01-01', periods=2, tz='utc')
ser = Series(range(2), index=index, dtype='int64')
for sel in (index, list(index)):
    result = indexer_sl(ser)[sel]
    expected = ser.copy()
    if sel is not index:
        expected.index = expected.index._with_freq(None)
    tm.assert_series_equal(result, expected)
    result = ser.copy()
    indexer_sl(result)[sel] = 1
    expected = Series(1, index=index)
    tm.assert_series_equal(result, expected)
assert indexer_sl(ser)[index[1]] == 1
result = ser.copy()
indexer_sl(result)[index[1]] = 5
expected = Series([0, 5], index=index)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_datetime.py:104 | Complexity: Advanced | Last updated: 2026-06-02*
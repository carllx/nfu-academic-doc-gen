# How To: Loc With Interval

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test loc with interval

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
assert result == expected
```

### Step 2: Assign expected = 0

```python
expected = 0
```

### Step 3: Assign result = value

```python
result = indexer_sl(ser)[Interval(0, 1)]
```

**Verification:**
```python
assert result == expected
```

### Step 4: Assign expected = value

```python
expected = ser.iloc[3:5]
```

### Step 5: Assign result = value

```python
result = indexer_sl(ser)[[Interval(3, 4), Interval(4, 5)]]
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, result)
```

### Step 7: indexer_sl(ser)[Interval(3, 5, closed='left')]

```python
indexer_sl(ser)[Interval(3, 5, closed='left')]
```

### Step 8: indexer_sl(ser)[Interval(3, 5)]

```python
indexer_sl(ser)[Interval(3, 5)]
```

### Step 9: indexer_sl(ser)[Interval(-2, 0)]

```python
indexer_sl(ser)[Interval(-2, 0)]
```

### Step 10: indexer_sl(ser)[Interval(5, 6)]

```python
indexer_sl(ser)[Interval(5, 6)]
```


## Complete Example

```python
# Setup
# Fixtures: series_with_interval_index, indexer_sl

# Workflow
ser = series_with_interval_index.copy()
expected = 0
result = indexer_sl(ser)[Interval(0, 1)]
assert result == expected
expected = ser.iloc[3:5]
result = indexer_sl(ser)[[Interval(3, 4), Interval(4, 5)]]
tm.assert_series_equal(expected, result)
with pytest.raises(KeyError, match=re.escape("Interval(3, 5, closed='left')")):
    indexer_sl(ser)[Interval(3, 5, closed='left')]
with pytest.raises(KeyError, match=re.escape("Interval(3, 5, closed='right')")):
    indexer_sl(ser)[Interval(3, 5)]
with pytest.raises(KeyError, match=re.escape("Interval(-2, 0, closed='right')")):
    indexer_sl(ser)[Interval(-2, 0)]
with pytest.raises(KeyError, match=re.escape("Interval(5, 6, closed='right')")):
    indexer_sl(ser)[Interval(5, 6)]
```

## Next Steps


---

*Source: test_interval_new.py:20 | Complexity: Advanced | Last updated: 2026-06-02*
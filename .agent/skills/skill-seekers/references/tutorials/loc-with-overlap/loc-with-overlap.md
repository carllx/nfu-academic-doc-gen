# How To: Loc With Overlap

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test loc with overlap

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
idx = IntervalIndex.from_tuples([(1, 5), (3, 7)])
```

**Verification:**
```python
assert expected == result
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(range(len(idx)), index=idx)
```

### Step 3: Assign expected = ser

```python
expected = ser
```

### Step 4: Assign result = value

```python
result = indexer_sl(ser)[4]
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, result)
```

### Step 6: Assign result = value

```python
result = indexer_sl(ser)[[4]]
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, result)
```

### Step 8: Assign expected = 0

```python
expected = 0
```

### Step 9: Assign result = value

```python
result = indexer_sl(ser)[Interval(1, 5)]
```

**Verification:**
```python
assert expected == result
```

### Step 10: Assign expected = ser

```python
expected = ser
```

### Step 11: Assign result = value

```python
result = indexer_sl(ser)[[Interval(1, 5), Interval(3, 7)]]
```

### Step 12: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, result)
```

### Step 13: Assign msg = "None of \\[IntervalIndex\\(\\[\\(3, 5\\]\\], dtype='interval\\[int64, right\\]'\\)\\] are in the \\[index\\]"

```python
msg = "None of \\[IntervalIndex\\(\\[\\(3, 5\\]\\], dtype='interval\\[int64, right\\]'\\)\\] are in the \\[index\\]"
```

### Step 14: Assign expected = ser

```python
expected = ser
```

### Step 15: Assign result = value

```python
result = indexer_sl(ser)[Interval(1, 5):Interval(3, 7)]
```

### Step 16: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, result)
```

### Step 17: Assign msg = "'can only get slices from an IntervalIndex if bounds are non-overlapping and all monotonic increasing or decreasing'"

```python
msg = "'can only get slices from an IntervalIndex if bounds are non-overlapping and all monotonic increasing or decreasing'"
```

### Step 18: indexer_sl(ser)[Interval(3, 5)]

```python
indexer_sl(ser)[Interval(3, 5)]
```

### Step 19: indexer_sl(ser)[[Interval(3, 5)]]

```python
indexer_sl(ser)[[Interval(3, 5)]]
```

### Step 20: indexer_sl(ser)[Interval(1, 6):Interval(3, 8)]

```python
indexer_sl(ser)[Interval(1, 6):Interval(3, 8)]
```

### Step 21: ser.loc[1:4]

```python
ser.loc[1:4]
```


## Complete Example

```python
# Setup
# Fixtures: indexer_sl

# Workflow
idx = IntervalIndex.from_tuples([(1, 5), (3, 7)])
ser = Series(range(len(idx)), index=idx)
expected = ser
result = indexer_sl(ser)[4]
tm.assert_series_equal(expected, result)
result = indexer_sl(ser)[[4]]
tm.assert_series_equal(expected, result)
expected = 0
result = indexer_sl(ser)[Interval(1, 5)]
assert expected == result
expected = ser
result = indexer_sl(ser)[[Interval(1, 5), Interval(3, 7)]]
tm.assert_series_equal(expected, result)
with pytest.raises(KeyError, match=re.escape("Interval(3, 5, closed='right')")):
    indexer_sl(ser)[Interval(3, 5)]
msg = "None of \\[IntervalIndex\\(\\[\\(3, 5\\]\\], dtype='interval\\[int64, right\\]'\\)\\] are in the \\[index\\]"
with pytest.raises(KeyError, match=msg):
    indexer_sl(ser)[[Interval(3, 5)]]
expected = ser
result = indexer_sl(ser)[Interval(1, 5):Interval(3, 7)]
tm.assert_series_equal(expected, result)
msg = "'can only get slices from an IntervalIndex if bounds are non-overlapping and all monotonic increasing or decreasing'"
with pytest.raises(KeyError, match=msg):
    indexer_sl(ser)[Interval(1, 6):Interval(3, 8)]
if indexer_sl is tm.loc:
    with pytest.raises(KeyError, match=msg):
        ser.loc[1:4]
```

## Next Steps


---

*Source: test_interval_new.py:126 | Complexity: Advanced | Last updated: 2026-06-02*
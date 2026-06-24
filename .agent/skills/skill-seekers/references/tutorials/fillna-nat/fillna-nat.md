# How To: Fillna Nat

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fillna nat

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pytz`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign series = Series(...)

```python
series = Series([0, 1, 2, NaT._value], dtype='M8[ns]')
```

### Step 2: Assign filled = series.fillna(...)

```python
filled = series.fillna(method='pad')
```

### Step 3: Assign filled2 = series.fillna(...)

```python
filled2 = series.fillna(value=series.values[2])
```

### Step 4: Assign expected = series.copy(...)

```python
expected = series.copy()
```

### Step 5: Assign unknown = value

```python
expected.iloc[3] = expected.iloc[2]
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(filled, expected)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(filled2, expected)
```

### Step 8: Assign df = DataFrame(...)

```python
df = DataFrame({'A': series})
```

### Step 9: Assign filled = df.fillna(...)

```python
filled = df.fillna(method='pad')
```

### Step 10: Assign filled2 = df.fillna(...)

```python
filled2 = df.fillna(value=series.values[2])
```

### Step 11: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': expected})
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(filled, expected)
```

### Step 13: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(filled2, expected)
```

### Step 14: Assign series = Series(...)

```python
series = Series([NaT._value, 0, 1, 2], dtype='M8[ns]')
```

### Step 15: Assign filled = series.fillna(...)

```python
filled = series.fillna(method='bfill')
```

### Step 16: Assign filled2 = series.fillna(...)

```python
filled2 = series.fillna(value=series[1])
```

### Step 17: Assign expected = series.copy(...)

```python
expected = series.copy()
```

### Step 18: Assign unknown = value

```python
expected[0] = expected[1]
```

### Step 19: Call tm.assert_series_equal()

```python
tm.assert_series_equal(filled, expected)
```

### Step 20: Call tm.assert_series_equal()

```python
tm.assert_series_equal(filled2, expected)
```

### Step 21: Assign df = DataFrame(...)

```python
df = DataFrame({'A': series})
```

### Step 22: Assign filled = df.fillna(...)

```python
filled = df.fillna(method='bfill')
```

### Step 23: Assign filled2 = df.fillna(...)

```python
filled2 = df.fillna(value=series[1])
```

### Step 24: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': expected})
```

### Step 25: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(filled, expected)
```

### Step 26: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(filled2, expected)
```


## Complete Example

```python
# Workflow
series = Series([0, 1, 2, NaT._value], dtype='M8[ns]')
filled = series.fillna(method='pad')
filled2 = series.fillna(value=series.values[2])
expected = series.copy()
expected.iloc[3] = expected.iloc[2]
tm.assert_series_equal(filled, expected)
tm.assert_series_equal(filled2, expected)
df = DataFrame({'A': series})
filled = df.fillna(method='pad')
filled2 = df.fillna(value=series.values[2])
expected = DataFrame({'A': expected})
tm.assert_frame_equal(filled, expected)
tm.assert_frame_equal(filled2, expected)
series = Series([NaT._value, 0, 1, 2], dtype='M8[ns]')
filled = series.fillna(method='bfill')
filled2 = series.fillna(value=series[1])
expected = series.copy()
expected[0] = expected[1]
tm.assert_series_equal(filled, expected)
tm.assert_series_equal(filled2, expected)
df = DataFrame({'A': series})
filled = df.fillna(method='bfill')
filled2 = df.fillna(value=series[1])
expected = DataFrame({'A': expected})
tm.assert_frame_equal(filled, expected)
tm.assert_frame_equal(filled2, expected)
```

## Next Steps


---

*Source: test_fillna.py:32 | Complexity: Advanced | Last updated: 2026-06-02*
# How To: Setitem Interval With Slice

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test setitem interval with slice

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ii = IntervalIndex.from_breaks(...)

```python
ii = IntervalIndex.from_breaks(range(4, 15))
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(range(10), index=ii)
```

### Step 3: Assign orig = ser.copy(...)

```python
orig = ser.copy()
```

### Step 4: Assign unknown = 20

```python
ser.loc[1:3] = 20
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser, orig)
```

### Step 6: Assign unknown = 19

```python
ser.loc[6:8] = 19
```

### Step 7: Assign unknown = 19

```python
orig.iloc[1:4] = 19
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser, orig)
```

### Step 9: Assign ser2 = Series(...)

```python
ser2 = Series(range(5), index=ii[::2])
```

### Step 10: Assign orig2 = ser2.copy(...)

```python
orig2 = ser2.copy()
```

### Step 11: Assign unknown = 22

```python
ser2.loc[6:8] = 22
```

### Step 12: Assign unknown = 22

```python
orig2.iloc[1] = 22
```

### Step 13: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser2, orig2)
```

### Step 14: Assign unknown = 21

```python
ser2.loc[5:7] = 21
```

### Step 15: Assign unknown = 21

```python
orig2.iloc[:2] = 21
```

### Step 16: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser2, orig2)
```


## Complete Example

```python
# Workflow
ii = IntervalIndex.from_breaks(range(4, 15))
ser = Series(range(10), index=ii)
orig = ser.copy()
ser.loc[1:3] = 20
tm.assert_series_equal(ser, orig)
ser.loc[6:8] = 19
orig.iloc[1:4] = 19
tm.assert_series_equal(ser, orig)
ser2 = Series(range(5), index=ii[::2])
orig2 = ser2.copy()
ser2.loc[6:8] = 22
orig2.iloc[1] = 22
tm.assert_series_equal(ser2, orig2)
ser2.loc[5:7] = 21
orig2.iloc[:2] = 21
tm.assert_series_equal(ser2, orig2)
```

## Next Steps


---

*Source: test_interval.py:140 | Complexity: Advanced | Last updated: 2026-06-02*
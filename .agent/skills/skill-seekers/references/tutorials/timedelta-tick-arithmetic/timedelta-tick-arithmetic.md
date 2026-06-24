# How To: Timedelta Tick Arithmetic

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test timedelta tick arithmetic

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.tests.arithmetic.common`


## Step-by-Step Guide

### Step 1: Assign rng = pd.date_range(...)

```python
rng = pd.date_range('2013', '2014')
```

**Verification:**
```python
assert result1.freq == rng.freq
```

### Step 2: Assign s = Series(...)

```python
s = Series(rng)
```

**Verification:**
```python
assert result3.freq == rng.freq
```

### Step 3: Assign result1 = value

```python
result1 = rng - offsets.Hour(1)
```

### Step 4: Assign result2 = DatetimeIndex(...)

```python
result2 = DatetimeIndex(s - np.timedelta64(100000000))
```

### Step 5: Assign result3 = value

```python
result3 = rng - np.timedelta64(100000000)
```

### Step 6: Assign result4 = DatetimeIndex(...)

```python
result4 = DatetimeIndex(s - offsets.Hour(1))
```

**Verification:**
```python
assert result1.freq == rng.freq
```

### Step 7: Assign result1 = result1._with_freq(...)

```python
result1 = result1._with_freq(None)
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result1, result4)
```

**Verification:**
```python
assert result3.freq == rng.freq
```

### Step 9: Assign result3 = result3._with_freq(...)

```python
result3 = result3._with_freq(None)
```

### Step 10: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result2, result3)
```


## Complete Example

```python
# Workflow
rng = pd.date_range('2013', '2014')
s = Series(rng)
result1 = rng - offsets.Hour(1)
result2 = DatetimeIndex(s - np.timedelta64(100000000))
result3 = rng - np.timedelta64(100000000)
result4 = DatetimeIndex(s - offsets.Hour(1))
assert result1.freq == rng.freq
result1 = result1._with_freq(None)
tm.assert_index_equal(result1, result4)
assert result3.freq == rng.freq
result3 = result3._with_freq(None)
tm.assert_index_equal(result2, result3)
```

## Next Steps


---

*Source: test_timedelta64.py:544 | Complexity: Advanced | Last updated: 2026-06-02*
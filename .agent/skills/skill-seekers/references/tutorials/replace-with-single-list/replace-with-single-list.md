# How To: Replace With Single List

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test replace with single list

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign ser = pd.Series(...)

```python
ser = pd.Series([0, 1, 2, 3, 4])
```

**Verification:**
```python
assert return_value is None
```

### Step 2: Assign msg2 = "Series.replace without 'value' and with non-dict-like 'to_replace' is deprecated"

```python
msg2 = "Series.replace without 'value' and with non-dict-like 'to_replace' is deprecated"
```

**Verification:**
```python
assert return_value is None
```

### Step 3: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, pd.Series([0, 0, 0, 0, 4]))
```

### Step 4: Assign s = ser.copy(...)

```python
s = ser.copy()
```

**Verification:**
```python
assert return_value is None
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s, pd.Series([0, 0, 0, 0, 4]))
```

### Step 6: Assign s = ser.copy(...)

```python
s = ser.copy()
```

### Step 7: Assign msg = 'Invalid fill method\\. Expecting pad \\(ffill\\) or backfill \\(bfill\\)\\. Got crash_cymbal'

```python
msg = 'Invalid fill method\\. Expecting pad \\(ffill\\) or backfill \\(bfill\\)\\. Got crash_cymbal'
```

### Step 8: Assign msg3 = "The 'method' keyword in Series.replace is deprecated"

```python
msg3 = "The 'method' keyword in Series.replace is deprecated"
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s, ser)
```

### Step 10: Assign result = ser.replace(...)

```python
result = ser.replace([1, 2, 3])
```

### Step 11: Assign return_value = s.replace(...)

```python
return_value = s.replace([1, 2, 3], inplace=True)
```

**Verification:**
```python
assert return_value is None
```

### Step 12: Assign return_value = s.replace(...)

```python
return_value = s.replace([1, 2, 3], inplace=True, method='crash_cymbal')
```


## Complete Example

```python
# Workflow
ser = pd.Series([0, 1, 2, 3, 4])
msg2 = "Series.replace without 'value' and with non-dict-like 'to_replace' is deprecated"
with tm.assert_produces_warning(FutureWarning, match=msg2):
    result = ser.replace([1, 2, 3])
tm.assert_series_equal(result, pd.Series([0, 0, 0, 0, 4]))
s = ser.copy()
with tm.assert_produces_warning(FutureWarning, match=msg2):
    return_value = s.replace([1, 2, 3], inplace=True)
assert return_value is None
tm.assert_series_equal(s, pd.Series([0, 0, 0, 0, 4]))
s = ser.copy()
msg = 'Invalid fill method\\. Expecting pad \\(ffill\\) or backfill \\(bfill\\)\\. Got crash_cymbal'
msg3 = "The 'method' keyword in Series.replace is deprecated"
with pytest.raises(ValueError, match=msg):
    with tm.assert_produces_warning(FutureWarning, match=msg3):
        return_value = s.replace([1, 2, 3], inplace=True, method='crash_cymbal')
    assert return_value is None
tm.assert_series_equal(s, ser)
```

## Next Steps


---

*Source: test_replace.py:185 | Complexity: Advanced | Last updated: 2026-06-02*
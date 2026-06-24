# How To: Between Datetime Object Dtype

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test between datetime object dtype

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series(bdate_range('1/1/2000', periods=20), dtype=object)
```

### Step 2: Assign unknown = value

```python
ser[::2] = np.nan
```

### Step 3: Assign result = value

```python
result = ser[ser.between(ser[3], ser[17])]
```

### Step 4: Assign expected = unknown.dropna(...)

```python
expected = ser[3:18].dropna()
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign result = value

```python
result = ser[ser.between(ser[3], ser[17], inclusive='neither')]
```

### Step 7: Assign expected = unknown.dropna(...)

```python
expected = ser[5:16].dropna()
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
ser = Series(bdate_range('1/1/2000', periods=20), dtype=object)
ser[::2] = np.nan
result = ser[ser.between(ser[3], ser[17])]
expected = ser[3:18].dropna()
tm.assert_series_equal(result, expected)
result = ser[ser.between(ser[3], ser[17], inclusive='neither')]
expected = ser[5:16].dropna()
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_between.py:22 | Complexity: Advanced | Last updated: 2026-06-02*
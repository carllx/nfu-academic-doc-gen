# How To: Replace Timedelta Td64

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test replace timedelta td64

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign tdi = pd.timedelta_range(...)

```python
tdi = pd.timedelta_range(0, periods=5)
```

### Step 2: Assign ser = pd.Series(...)

```python
ser = pd.Series(tdi)
```

### Step 3: Assign result = ser.replace(...)

```python
result = ser.replace({ser[1]: ser[3]})
```

### Step 4: Assign expected = pd.Series(...)

```python
expected = pd.Series([ser[0], ser[3], ser[2], ser[3], ser[4]])
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
tdi = pd.timedelta_range(0, periods=5)
ser = pd.Series(tdi)
result = ser.replace({ser[1]: ser[3]})
expected = pd.Series([ser[0], ser[3], ser[2], ser[3], ser[4]])
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_replace.py:175 | Complexity: Intermediate | Last updated: 2026-06-02*
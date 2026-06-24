# How To: Asof Preserves Bool Dtype

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test asof preserves bool dtype

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dti = date_range(...)

```python
dti = date_range('2017-01-01', freq='MS', periods=4)
```

### Step 2: Assign ser = Series(...)

```python
ser = Series([True, False, True], index=dti[:-1])
```

### Step 3: Assign ts = value

```python
ts = dti[-1]
```

### Step 4: Assign res = ser.asof(...)

```python
res = ser.asof([ts])
```

### Step 5: Assign expected = Series(...)

```python
expected = Series([True], index=[ts])
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, expected)
```


## Complete Example

```python
# Workflow
dti = date_range('2017-01-01', freq='MS', periods=4)
ser = Series([True, False, True], index=dti[:-1])
ts = dti[-1]
res = ser.asof([ts])
expected = Series([True], index=[ts])
tm.assert_series_equal(res, expected)
```

## Next Steps


---

*Source: test_asof.py:189 | Complexity: Intermediate | Last updated: 2026-06-02*
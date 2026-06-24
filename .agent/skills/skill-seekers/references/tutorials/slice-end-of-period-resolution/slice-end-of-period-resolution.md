# How To: Slice End Of Period Resolution

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test slice end of period resolution

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: partial_dtime
```

## Step-by-Step Guide

### Step 1: Assign dti = date_range(...)

```python
dti = date_range('2019-12-31 23:59:55.999999999', periods=10, freq='s')
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(range(10), index=dti)
```

### Step 3: Assign result = value

```python
result = ser[partial_dtime]
```

### Step 4: Assign expected = value

```python
expected = ser.iloc[:5]
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: partial_dtime

# Workflow
dti = date_range('2019-12-31 23:59:55.999999999', periods=10, freq='s')
ser = Series(range(10), index=dti)
result = ser[partial_dtime]
expected = ser.iloc[:5]
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_partial_slicing.py:147 | Complexity: Intermediate | Last updated: 2026-06-02*
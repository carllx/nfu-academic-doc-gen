# How To: Where Raises

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test where raises

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: other
```

## Step-by-Step Guide

### Step 1: Assign ser = pd.Series(...)

```python
ser = pd.Series(IntervalArray.from_breaks([1, 2, 3, 4], closed='left'))
```

### Step 2: Assign mask = np.array(...)

```python
mask = np.array([True, False, True])
```

### Step 3: Assign match = "'value.closed' is 'right', expected 'left'."

```python
match = "'value.closed' is 'right', expected 'left'."
```

### Step 4: Assign res = ser.where(...)

```python
res = ser.where(mask, other=other)
```

### Step 5: Assign expected = ser.astype.where(...)

```python
expected = ser.astype(object).where(mask, other)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, expected)
```

### Step 7: Call ser.array._where()

```python
ser.array._where(mask, other)
```


## Complete Example

```python
# Setup
# Fixtures: other

# Workflow
ser = pd.Series(IntervalArray.from_breaks([1, 2, 3, 4], closed='left'))
mask = np.array([True, False, True])
match = "'value.closed' is 'right', expected 'left'."
with pytest.raises(ValueError, match=match):
    ser.array._where(mask, other)
res = ser.where(mask, other=other)
expected = ser.astype(object).where(mask, other)
tm.assert_series_equal(res, expected)
```

## Next Steps


---

*Source: test_interval.py:76 | Complexity: Intermediate | Last updated: 2026-06-02*
# How To: Compare Scalar Na

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test compare scalar na

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `operator`
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.tests.arithmetic.common`

**Setup Required:**
```python
# Fixtures: op, interval_array, nulls_fixture, box_with_array
```

## Step-by-Step Guide

### Step 1: Assign box = box_with_array

```python
box = box_with_array
```

### Step 2: Assign obj = tm.box_expected(...)

```python
obj = tm.box_expected(interval_array, box)
```

### Step 3: Assign result = op(...)

```python
result = op(obj, nulls_fixture)
```

### Step 4: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 5: Assign rev = op(...)

```python
rev = op(nulls_fixture, obj)
```

### Step 6: Call tm.assert_equal()

```python
tm.assert_equal(rev, expected)
```

### Step 7: Assign exp = np.ones(...)

```python
exp = np.ones(interval_array.shape, dtype=bool)
```

### Step 8: Assign expected = BooleanArray(...)

```python
expected = BooleanArray(exp, exp)
```

### Step 9: Assign expected = self.elementwise_comparison(...)

```python
expected = self.elementwise_comparison(op, interval_array, nulls_fixture)
```

### Step 10: Assign xbox = get_upcast_box(...)

```python
xbox = get_upcast_box(obj, nulls_fixture, True)
```

### Step 11: Assign expected = tm.box_expected(...)

```python
expected = tm.box_expected(expected, xbox)
```


## Complete Example

```python
# Setup
# Fixtures: op, interval_array, nulls_fixture, box_with_array

# Workflow
box = box_with_array
obj = tm.box_expected(interval_array, box)
result = op(obj, nulls_fixture)
if nulls_fixture is pd.NA:
    exp = np.ones(interval_array.shape, dtype=bool)
    expected = BooleanArray(exp, exp)
else:
    expected = self.elementwise_comparison(op, interval_array, nulls_fixture)
if not (box is Index and nulls_fixture is pd.NA):
    xbox = get_upcast_box(obj, nulls_fixture, True)
    expected = tm.box_expected(expected, xbox)
tm.assert_equal(result, expected)
rev = op(nulls_fixture, obj)
tm.assert_equal(rev, expected)
```

## Next Steps


---

*Source: test_interval.py:136 | Complexity: Advanced | Last updated: 2026-06-02*
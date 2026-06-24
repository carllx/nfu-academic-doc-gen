# How To: Nat Comparisons Scalar

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test nat comparisons scalar

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `itertools`
- `operator`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs.conversion`
- `pandas._libs.tslibs.offsets`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.tests.arithmetic.common`

**Setup Required:**
```python
# Fixtures: dtype, data, box_with_array
```

## Step-by-Step Guide

### Step 1: Assign box = box_with_array

```python
box = box_with_array
```

### Step 2: Assign left = Series(...)

```python
left = Series(data, dtype=dtype)
```

### Step 3: Assign left = tm.box_expected(...)

```python
left = tm.box_expected(left, box)
```

### Step 4: Assign xbox = get_upcast_box(...)

```python
xbox = get_upcast_box(left, NaT, True)
```

### Step 5: Assign expected = value

```python
expected = [False, False, False]
```

### Step 6: Assign expected = tm.box_expected(...)

```python
expected = tm.box_expected(expected, xbox)
```

### Step 7: Call tm.assert_equal()

```python
tm.assert_equal(left == NaT, expected)
```

### Step 8: Call tm.assert_equal()

```python
tm.assert_equal(NaT == left, expected)
```

### Step 9: Assign expected = value

```python
expected = [True, True, True]
```

### Step 10: Assign expected = tm.box_expected(...)

```python
expected = tm.box_expected(expected, xbox)
```

### Step 11: Call tm.assert_equal()

```python
tm.assert_equal(left != NaT, expected)
```

### Step 12: Call tm.assert_equal()

```python
tm.assert_equal(NaT != left, expected)
```

### Step 13: Assign expected = value

```python
expected = [False, False, False]
```

### Step 14: Assign expected = tm.box_expected(...)

```python
expected = tm.box_expected(expected, xbox)
```

### Step 15: Call tm.assert_equal()

```python
tm.assert_equal(left < NaT, expected)
```

### Step 16: Call tm.assert_equal()

```python
tm.assert_equal(NaT > left, expected)
```

### Step 17: Call tm.assert_equal()

```python
tm.assert_equal(left <= NaT, expected)
```

### Step 18: Call tm.assert_equal()

```python
tm.assert_equal(NaT >= left, expected)
```

### Step 19: Call tm.assert_equal()

```python
tm.assert_equal(left > NaT, expected)
```

### Step 20: Call tm.assert_equal()

```python
tm.assert_equal(NaT < left, expected)
```

### Step 21: Call tm.assert_equal()

```python
tm.assert_equal(left >= NaT, expected)
```

### Step 22: Call tm.assert_equal()

```python
tm.assert_equal(NaT <= left, expected)
```

### Step 23: Assign expected = pd.array(...)

```python
expected = pd.array(expected, dtype='bool')
```

### Step 24: Assign expected = pd.array(...)

```python
expected = pd.array(expected, dtype='bool')
```

### Step 25: Assign expected = pd.array(...)

```python
expected = pd.array(expected, dtype='bool')
```


## Complete Example

```python
# Setup
# Fixtures: dtype, data, box_with_array

# Workflow
box = box_with_array
left = Series(data, dtype=dtype)
left = tm.box_expected(left, box)
xbox = get_upcast_box(left, NaT, True)
expected = [False, False, False]
expected = tm.box_expected(expected, xbox)
if box is pd.array and dtype is object:
    expected = pd.array(expected, dtype='bool')
tm.assert_equal(left == NaT, expected)
tm.assert_equal(NaT == left, expected)
expected = [True, True, True]
expected = tm.box_expected(expected, xbox)
if box is pd.array and dtype is object:
    expected = pd.array(expected, dtype='bool')
tm.assert_equal(left != NaT, expected)
tm.assert_equal(NaT != left, expected)
expected = [False, False, False]
expected = tm.box_expected(expected, xbox)
if box is pd.array and dtype is object:
    expected = pd.array(expected, dtype='bool')
tm.assert_equal(left < NaT, expected)
tm.assert_equal(NaT > left, expected)
tm.assert_equal(left <= NaT, expected)
tm.assert_equal(NaT >= left, expected)
tm.assert_equal(left > NaT, expected)
tm.assert_equal(NaT < left, expected)
tm.assert_equal(left >= NaT, expected)
tm.assert_equal(NaT <= left, expected)
```

## Next Steps


---

*Source: test_datetime64.py:224 | Complexity: Advanced | Last updated: 2026-06-02*
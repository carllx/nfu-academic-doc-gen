# How To: Parr Cmp Period Scalar2

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test parr cmp period scalar2

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `operator`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.arrays`
- `pandas.tests.arithmetic.common`

**Setup Required:**
```python
# Fixtures: box_with_array
```

## Step-by-Step Guide

### Step 1: Assign pi = period_range(...)

```python
pi = period_range('2000-01-01', periods=10, freq='D')
```

### Step 2: Assign val = value

```python
val = pi[3]
```

### Step 3: Assign expected = value

```python
expected = [x > val for x in pi]
```

### Step 4: Assign ser = tm.box_expected(...)

```python
ser = tm.box_expected(pi, box_with_array)
```

### Step 5: Assign xbox = get_upcast_box(...)

```python
xbox = get_upcast_box(ser, val, True)
```

### Step 6: Assign expected = tm.box_expected(...)

```python
expected = tm.box_expected(expected, xbox)
```

### Step 7: Assign result = value

```python
result = ser > val
```

### Step 8: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 9: Assign val = value

```python
val = pi[5]
```

### Step 10: Assign result = value

```python
result = ser > val
```

### Step 11: Assign expected = value

```python
expected = [x > val for x in pi]
```

### Step 12: Assign expected = tm.box_expected(...)

```python
expected = tm.box_expected(expected, xbox)
```

### Step 13: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: box_with_array

# Workflow
pi = period_range('2000-01-01', periods=10, freq='D')
val = pi[3]
expected = [x > val for x in pi]
ser = tm.box_expected(pi, box_with_array)
xbox = get_upcast_box(ser, val, True)
expected = tm.box_expected(expected, xbox)
result = ser > val
tm.assert_equal(result, expected)
val = pi[5]
result = ser > val
expected = [x > val for x in pi]
expected = tm.box_expected(expected, xbox)
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_period.py:227 | Complexity: Advanced | Last updated: 2026-06-02*
# How To: Numeric Arr Mul Tdscalar

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test numeric arr mul tdscalar

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `collections`
- `datetime`
- `decimal`
- `operator`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.computation`
- `pandas.tests.arithmetic.common`

**Setup Required:**
```python
# Fixtures: scalar_td, numeric_idx, box_with_array
```

## Step-by-Step Guide

### Step 1: Assign box = box_with_array

```python
box = box_with_array
```

### Step 2: Assign index = numeric_idx

```python
index = numeric_idx
```

### Step 3: Assign expected = TimedeltaIndex(...)

```python
expected = TimedeltaIndex([Timedelta(days=n) for n in range(len(index))])
```

### Step 4: Assign index = tm.box_expected(...)

```python
index = tm.box_expected(index, box)
```

### Step 5: Assign expected = tm.box_expected(...)

```python
expected = tm.box_expected(expected, box)
```

### Step 6: Assign result = value

```python
result = index * scalar_td
```

### Step 7: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 8: Assign commute = value

```python
commute = scalar_td * index
```

### Step 9: Call tm.assert_equal()

```python
tm.assert_equal(commute, expected)
```

### Step 10: Assign dtype = value

```python
dtype = scalar_td.dtype
```

### Step 11: Assign expected = expected.astype(...)

```python
expected = expected.astype(dtype)
```

### Step 12: Assign expected = expected.astype(...)

```python
expected = expected.astype('m8[us]')
```


## Complete Example

```python
# Setup
# Fixtures: scalar_td, numeric_idx, box_with_array

# Workflow
box = box_with_array
index = numeric_idx
expected = TimedeltaIndex([Timedelta(days=n) for n in range(len(index))])
if isinstance(scalar_td, np.timedelta64):
    dtype = scalar_td.dtype
    expected = expected.astype(dtype)
elif type(scalar_td) is timedelta:
    expected = expected.astype('m8[us]')
index = tm.box_expected(index, box)
expected = tm.box_expected(expected, box)
result = index * scalar_td
tm.assert_equal(result, expected)
commute = scalar_td * index
tm.assert_equal(commute, expected)
```

## Next Steps


---

*Source: test_numeric.py:236 | Complexity: Advanced | Last updated: 2026-06-02*
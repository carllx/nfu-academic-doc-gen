# How To: Scalar Ops From Sequence Raises

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test scalar ops from sequence raises

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `decimal`
- `operator`
- `numpy`
- `pytest`
- `pandas.compat.numpy`
- `pandas`
- `pandas._testing`
- `pandas.tests.extension`
- `pandas.tests.extension.decimal.array`

**Setup Required:**
```python
# Fixtures: class_
```

## Step-by-Step Guide

### Step 1: Assign arr = class_(...)

```python
arr = class_([decimal.Decimal('1.0'), decimal.Decimal('2.0')])
```

### Step 2: Assign result = value

```python
result = arr + arr
```

### Step 3: Assign expected = np.array(...)

```python
expected = np.array([decimal.Decimal('2.0'), decimal.Decimal('4.0')], dtype='object')
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: class_

# Workflow
arr = class_([decimal.Decimal('1.0'), decimal.Decimal('2.0')])
result = arr + arr
expected = np.array([decimal.Decimal('2.0'), decimal.Decimal('4.0')], dtype='object')
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_decimal.py:418 | Complexity: Intermediate | Last updated: 2026-06-02*
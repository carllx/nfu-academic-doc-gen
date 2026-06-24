# How To: Dataframe Constructor With Dtype

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dataframe constructor with dtype

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign arr = DecimalArray(...)

```python
arr = DecimalArray([decimal.Decimal('10.0')])
```

### Step 2: Assign result = pd.DataFrame(...)

```python
result = pd.DataFrame({'A': arr}, dtype=DecimalDtype())
```

### Step 3: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'A': arr})
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign arr = DecimalArray(...)

```python
arr = DecimalArray([decimal.Decimal('10.0')])
```

### Step 6: Assign result = pd.DataFrame(...)

```python
result = pd.DataFrame({'A': arr}, dtype='int64')
```

### Step 7: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'A': [10]})
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
arr = DecimalArray([decimal.Decimal('10.0')])
result = pd.DataFrame({'A': arr}, dtype=DecimalDtype())
expected = pd.DataFrame({'A': arr})
tm.assert_frame_equal(result, expected)
arr = DecimalArray([decimal.Decimal('10.0')])
result = pd.DataFrame({'A': arr}, dtype='int64')
expected = pd.DataFrame({'A': [10]})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_decimal.py:343 | Complexity: Advanced | Last updated: 2026-06-02*
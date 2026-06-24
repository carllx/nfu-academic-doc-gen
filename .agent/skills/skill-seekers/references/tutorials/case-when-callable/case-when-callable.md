# How To: Case When Callable

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test output on a callable

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: '\n    Test output on a callable\n    '

```python
'\n    Test output on a callable\n    '
```

### Step 2: Assign x = np.linspace(...)

```python
x = np.linspace(-2.5, 2.5, 6)
```

### Step 3: Assign ser = Series(...)

```python
ser = Series(x)
```

### Step 4: Assign result = ser.case_when(...)

```python
result = ser.case_when(caselist=[(lambda df: df < 0, lambda df: -df), (lambda df: df >= 0, lambda df: df)])
```

### Step 5: Assign expected = np.piecewise(...)

```python
expected = np.piecewise(x, [x < 0, x >= 0], [lambda x: -x, lambda x: x])
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, Series(expected))
```


## Complete Example

```python
# Workflow
'\n    Test output on a callable\n    '
x = np.linspace(-2.5, 2.5, 6)
ser = Series(x)
result = ser.case_when(caselist=[(lambda df: df < 0, lambda df: -df), (lambda df: df >= 0, lambda df: df)])
expected = np.piecewise(x, [x < 0, x >= 0], [lambda x: -x, lambda x: x])
tm.assert_series_equal(result, Series(expected))
```

## Next Steps


---

*Source: test_case_when.py:134 | Complexity: Intermediate | Last updated: 2026-06-02*
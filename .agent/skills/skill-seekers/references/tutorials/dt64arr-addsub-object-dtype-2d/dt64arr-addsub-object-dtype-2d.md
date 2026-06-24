# How To: Dt64Arr Addsub Object Dtype 2D

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dt64arr addsub object dtype 2d

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign dti = date_range(...)

```python
dti = date_range('1994-02-13', freq='2W', periods=4)
```

**Verification:**
```python
assert other.shape == dta.shape
```

### Step 2: Assign dta = dti._data.reshape(...)

```python
dta = dti._data.reshape((4, 1))
```

**Verification:**
```python
assert result2.shape == (4, 1)
```

### Step 3: Assign other = np.array(...)

```python
other = np.array([[pd.offsets.Day(n)] for n in range(4)])
```

**Verification:**
```python
assert all((td._value == 0 for td in result2.ravel()))
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

**Verification:**
```python
assert result2.shape == (4, 1)
```

### Step 5: Assign result = value

```python
result = dta + other
```

### Step 6: Assign expected = unknown.reshape(...)

```python
expected = (dta[:, 0] + other[:, 0]).reshape(-1, 1)
```

### Step 7: Assign result2 = value

```python
result2 = dta - dta.astype(object)
```


## Complete Example

```python
# Workflow
dti = date_range('1994-02-13', freq='2W', periods=4)
dta = dti._data.reshape((4, 1))
other = np.array([[pd.offsets.Day(n)] for n in range(4)])
assert other.shape == dta.shape
with tm.assert_produces_warning(PerformanceWarning):
    result = dta + other
with tm.assert_produces_warning(PerformanceWarning):
    expected = (dta[:, 0] + other[:, 0]).reshape(-1, 1)
tm.assert_numpy_array_equal(result, expected)
with tm.assert_produces_warning(PerformanceWarning):
    result2 = dta - dta.astype(object)
assert result2.shape == (4, 1)
assert all((td._value == 0 for td in result2.ravel()))
```

## Next Steps


---

*Source: test_datetime64.py:2411 | Complexity: Intermediate | Last updated: 2026-06-02*
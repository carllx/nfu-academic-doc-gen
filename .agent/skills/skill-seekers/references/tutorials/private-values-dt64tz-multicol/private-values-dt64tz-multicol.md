# How To: Private Values Dt64Tz Multicol

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test private values dt64tz multicol

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: using_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign dta = date_range._data.reshape(...)

```python
dta = date_range('2000', periods=8, tz='US/Central')._data.reshape(-1, 2)
```

**Verification:**
```python
assert not np.shares_memory(df._values._ndarray, dta._ndarray)
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(dta, columns=['A', 'B'])
```

**Verification:**
```python
assert np.shares_memory(df._values._ndarray, dta._ndarray)
```

### Step 3: Call tm.assert_equal()

```python
tm.assert_equal(df._values, dta)
```

### Step 4: Assign tda = value

```python
tda = dta - dta
```

### Step 5: Assign df2 = value

```python
df2 = df - df
```

### Step 6: Call tm.assert_equal()

```python
tm.assert_equal(df2._values, tda)
```

**Verification:**
```python
assert not np.shares_memory(df._values._ndarray, dta._ndarray)
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write

# Workflow
dta = date_range('2000', periods=8, tz='US/Central')._data.reshape(-1, 2)
df = DataFrame(dta, columns=['A', 'B'])
tm.assert_equal(df._values, dta)
if using_copy_on_write:
    assert not np.shares_memory(df._values._ndarray, dta._ndarray)
else:
    assert np.shares_memory(df._values._ndarray, dta._ndarray)
tda = dta - dta
df2 = df - df
tm.assert_equal(df2._values, tda)
```

## Next Steps


---

*Source: test_values.py:253 | Complexity: Intermediate | Last updated: 2026-06-02*
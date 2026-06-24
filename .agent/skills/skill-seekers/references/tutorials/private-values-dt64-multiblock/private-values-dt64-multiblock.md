# How To: Private Values Dt64 Multiblock

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test private values dt64 multiblock

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dta = value

```python
dta = date_range('2000', periods=8)._data
```

**Verification:**
```python
assert len(df._mgr.arrays) == 2
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'A': dta[:4]}, copy=False)
```

### Step 3: Assign unknown = value

```python
df['B'] = dta[4:]
```

**Verification:**
```python
assert len(df._mgr.arrays) == 2
```

### Step 4: Assign result = value

```python
result = df._values
```

### Step 5: Assign expected = value

```python
expected = dta.reshape(2, 4).T
```

### Step 6: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```


## Complete Example

```python
# Workflow
dta = date_range('2000', periods=8)._data
df = DataFrame({'A': dta[:4]}, copy=False)
df['B'] = dta[4:]
assert len(df._mgr.arrays) == 2
result = df._values
expected = dta.reshape(2, 4).T
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_values.py:270 | Complexity: Intermediate | Last updated: 2026-06-02*
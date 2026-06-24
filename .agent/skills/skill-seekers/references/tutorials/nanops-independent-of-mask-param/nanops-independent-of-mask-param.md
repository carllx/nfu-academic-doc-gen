# How To: Nanops Independent Of Mask Param

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test nanops independent of mask param

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `functools`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`

**Setup Required:**
```python
# Fixtures: operation
```

## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series([1, 2, np.nan, 3, np.nan, 4])
```

**Verification:**
```python
assert median_expected == median_result
```

### Step 2: Assign mask = ser.isna(...)

```python
mask = ser.isna()
```

### Step 3: Assign median_expected = operation(...)

```python
median_expected = operation(ser._values)
```

### Step 4: Assign median_result = operation(...)

```python
median_result = operation(ser._values, mask=mask)
```

**Verification:**
```python
assert median_expected == median_result
```


## Complete Example

```python
# Setup
# Fixtures: operation

# Workflow
ser = Series([1, 2, np.nan, 3, np.nan, 4])
mask = ser.isna()
median_expected = operation(ser._values)
median_result = operation(ser._values, mask=mask)
assert median_expected == median_result
```

## Next Steps


---

*Source: test_nanops.py:1195 | Complexity: Intermediate | Last updated: 2026-06-02*
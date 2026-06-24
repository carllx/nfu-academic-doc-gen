# How To: Ignore Downcast Invalid Data

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test ignore downcast invalid data

## Prerequisites

**Required Modules:**
- `decimal`
- `numpy`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign data = value

```python
data = ['foo', 2, 3]
```

### Step 2: Assign expected = np.array(...)

```python
expected = np.array(data, dtype=object)
```

### Step 3: Assign msg = "errors='ignore' is deprecated"

```python
msg = "errors='ignore' is deprecated"
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res, expected)
```

### Step 5: Assign res = to_numeric(...)

```python
res = to_numeric(data, errors='ignore', downcast='unsigned')
```


## Complete Example

```python
# Workflow
data = ['foo', 2, 3]
expected = np.array(data, dtype=object)
msg = "errors='ignore' is deprecated"
with tm.assert_produces_warning(FutureWarning, match=msg):
    res = to_numeric(data, errors='ignore', downcast='unsigned')
tm.assert_numpy_array_equal(res, expected)
```

## Next Steps


---

*Source: test_to_numeric.py:507 | Complexity: Intermediate | Last updated: 2026-06-02*
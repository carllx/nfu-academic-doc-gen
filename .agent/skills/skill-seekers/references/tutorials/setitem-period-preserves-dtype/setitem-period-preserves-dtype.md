# How To: Setitem Period Preserves Dtype

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test setitem period preserves dtype

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.base`
- `pandas.core.dtypes.common`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.tseries.offsets`


## Step-by-Step Guide

### Step 1: Assign data = value

```python
data = [Period('2003-12', 'D')]
```

### Step 2: Assign result = DataFrame(...)

```python
result = DataFrame([])
```

### Step 3: Assign unknown = data

```python
result['a'] = data
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': data}, columns=['a'])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
data = [Period('2003-12', 'D')]
result = DataFrame([])
result['a'] = data
expected = DataFrame({'a': data}, columns=['a'])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_setitem.py:222 | Complexity: Intermediate | Last updated: 2026-06-02*
# How To: Series With Name Not Matching Column

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test series with name not matching column

## Prerequisites

**Required Modules:**
- `array`
- `collections`
- `collections.abc`
- `dataclasses`
- `datetime`
- `functools`
- `re`
- `numpy`
- `numpy`
- `numpy.ma`
- `pytest`
- `pytz`
- `pandas._libs`
- `pandas.compat.numpy`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.common`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.arrays`
- `numpy.dtypes`


## Step-by-Step Guide

### Step 1: Assign x = Series(...)

```python
x = Series(range(5), name=1)
```

### Step 2: Assign y = Series(...)

```python
y = Series(range(5), name=0)
```

### Step 3: Assign result = DataFrame(...)

```python
result = DataFrame(x, columns=[0])
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame([], columns=[0])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign result = DataFrame(...)

```python
result = DataFrame(y, columns=[1])
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame([], columns=[1])
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
x = Series(range(5), name=1)
y = Series(range(5), name=0)
result = DataFrame(x, columns=[0])
expected = DataFrame([], columns=[0])
tm.assert_frame_equal(result, expected)
result = DataFrame(y, columns=[1])
expected = DataFrame([], columns=[1])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_constructors.py:202 | Complexity: Advanced | Last updated: 2026-06-02*
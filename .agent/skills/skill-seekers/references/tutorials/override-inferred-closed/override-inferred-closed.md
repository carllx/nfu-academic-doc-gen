# How To: Override Inferred Closed

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test override inferred closed

## Prerequisites

**Required Modules:**
- `functools`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.common`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.core.common`


## Step-by-Step Guide

### Step 1: Assign expected = IntervalIndex.from_tuples(...)

```python
expected = IntervalIndex.from_tuples(tuples, closed=closed)
```

### Step 2: Assign result = constructor(...)

```python
result = constructor(data, closed=closed)
```

### Step 3: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 4: Assign tuples = data.to_tuples(...)

```python
tuples = data.to_tuples()
```

### Step 5: Assign tuples = value

```python
tuples = [(iv.left, iv.right) if notna(iv) else iv for iv in data]
```


## Complete Example

```python
# Workflow
if isinstance(data, IntervalIndex):
    tuples = data.to_tuples()
else:
    tuples = [(iv.left, iv.right) if notna(iv) else iv for iv in data]
expected = IntervalIndex.from_tuples(tuples, closed=closed)
result = constructor(data, closed=closed)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_constructors.py:459 | Complexity: Intermediate | Last updated: 2026-06-02*
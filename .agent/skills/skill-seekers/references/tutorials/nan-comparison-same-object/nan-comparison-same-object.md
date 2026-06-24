# How To: Nan Comparison Same Object

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test nan comparison same object

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
- `datetime`
- `functools`
- `math`
- `operator`
- `re`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.indexes.api`
- `pyarrow`
- `IPython.core.completer`

**Setup Required:**
```python
# Fixtures: op
```

## Step-by-Step Guide

### Step 1: Assign idx = Index(...)

```python
idx = Index([np.nan])
```

### Step 2: Assign expected = np.array(...)

```python
expected = np.array([False])
```

### Step 3: Assign result = op(...)

```python
result = op(idx, idx)
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 5: Assign result = op(...)

```python
result = op(idx, idx.copy())
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: op

# Workflow
idx = Index([np.nan])
expected = np.array([False])
result = op(idx, idx)
tm.assert_numpy_array_equal(result, expected)
result = op(idx, idx.copy())
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_base.py:1715 | Complexity: Intermediate | Last updated: 2026-06-02*
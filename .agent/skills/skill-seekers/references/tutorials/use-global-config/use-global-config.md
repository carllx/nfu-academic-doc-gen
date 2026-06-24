# How To: Use Global Config

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test use global config

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas.util.version`
- `numba`
- `numba`


## Step-by-Step Guide

### Step 1: Call pytest.importorskip()

```python
pytest.importorskip('numba')
```

### Step 2: Assign data = DataFrame(...)

```python
data = DataFrame({0: ['a', 'a', 'b', 'b', 'a'], 1: [1.0, 2.0, 3.0, 4.0, 5.0]}, columns=[0, 1])
```

### Step 3: Assign grouped = data.groupby(...)

```python
grouped = data.groupby(0)
```

### Step 4: Assign expected = grouped.agg(...)

```python
expected = grouped.agg(func_1, engine='numba')
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(expected, result)
```

### Step 6: Assign result = grouped.agg(...)

```python
result = grouped.agg(func_1, engine=None)
```


## Complete Example

```python
# Workflow
pytest.importorskip('numba')

def func_1(values, index):
    return np.mean(values) - 3.4
data = DataFrame({0: ['a', 'a', 'b', 'b', 'a'], 1: [1.0, 2.0, 3.0, 4.0, 5.0]}, columns=[0, 1])
grouped = data.groupby(0)
expected = grouped.agg(func_1, engine='numba')
with option_context('compute.use_numba', True):
    result = grouped.agg(func_1, engine=None)
tm.assert_frame_equal(expected, result)
```

## Next Steps


---

*Source: test_numba.py:136 | Complexity: Intermediate | Last updated: 2026-06-02*
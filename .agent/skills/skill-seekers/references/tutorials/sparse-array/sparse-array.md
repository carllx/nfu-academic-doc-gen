# How To: Sparse Array

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sparse array

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.arrays`
- `pandas.tests.extension`

**Setup Required:**
```python
# Fixtures: data_for_compare, comparison_op, request
```

## Step-by-Step Guide

### Step 1: Assign ser = pd.Series(...)

```python
ser = pd.Series(data_for_compare)
```

### Step 2: Assign arr = value

```python
arr = data_for_compare + 1
```

### Step 3: Call self._compare_other()

```python
self._compare_other(ser, data_for_compare, comparison_op, arr)
```

### Step 4: Assign arr = value

```python
arr = data_for_compare * 2
```

### Step 5: Call self._compare_other()

```python
self._compare_other(ser, data_for_compare, comparison_op, arr)
```

### Step 6: Assign mark = pytest.mark.xfail(...)

```python
mark = pytest.mark.xfail(reason='Wrong fill_value')
```

### Step 7: Call request.applymarker()

```python
request.applymarker(mark)
```


## Complete Example

```python
# Setup
# Fixtures: data_for_compare, comparison_op, request

# Workflow
if data_for_compare.dtype.fill_value == 0 and comparison_op.__name__ != 'gt':
    mark = pytest.mark.xfail(reason='Wrong fill_value')
    request.applymarker(mark)
ser = pd.Series(data_for_compare)
arr = data_for_compare + 1
self._compare_other(ser, data_for_compare, comparison_op, arr)
arr = data_for_compare * 2
self._compare_other(ser, data_for_compare, comparison_op, arr)
```

## Next Steps


---

*Source: test_sparse.py:481 | Complexity: Intermediate | Last updated: 2026-06-02*
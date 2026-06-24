# How To: From Ints With Non Nano Dt64 Dtype

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test from ints with non nano dt64 dtype

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
- `collections.abc`
- `datetime`
- `dateutil.tz`
- `numpy`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.compat`
- `pandas.compat.numpy`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.core.internals.blocks`
- `numpy.dtypes`

**Setup Required:**
```python
# Fixtures: index_or_series
```

## Step-by-Step Guide

### Step 1: Assign values = np.arange(...)

```python
values = np.arange(10)
```

### Step 2: Assign res = index_or_series(...)

```python
res = index_or_series(values, dtype='M8[s]')
```

### Step 3: Assign expected = index_or_series(...)

```python
expected = index_or_series(values.astype('M8[s]'))
```

### Step 4: Call tm.assert_equal()

```python
tm.assert_equal(res, expected)
```

### Step 5: Assign res = index_or_series(...)

```python
res = index_or_series(list(values), dtype='M8[s]')
```

### Step 6: Call tm.assert_equal()

```python
tm.assert_equal(res, expected)
```


## Complete Example

```python
# Setup
# Fixtures: index_or_series

# Workflow
values = np.arange(10)
res = index_or_series(values, dtype='M8[s]')
expected = index_or_series(values.astype('M8[s]'))
tm.assert_equal(res, expected)
res = index_or_series(list(values), dtype='M8[s]')
tm.assert_equal(res, expected)
```

## Next Steps


---

*Source: test_constructors.py:54 | Complexity: Intermediate | Last updated: 2026-06-02*
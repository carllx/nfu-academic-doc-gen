# How To: Constructor Generator

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test constructor generator

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign gen = value

```python
gen = (i for i in range(10))
```

### Step 2: Assign result = Series(...)

```python
result = Series(gen)
```

### Step 3: Assign exp = Series(...)

```python
exp = Series(range(10))
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, exp)
```

### Step 5: Assign gen = value

```python
gen = (i for i in range(10))
```

### Step 6: Assign result = Series(...)

```python
result = Series(gen, index=range(10, 20))
```

### Step 7: Assign exp.index = range(...)

```python
exp.index = range(10, 20)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, exp)
```


## Complete Example

```python
# Workflow
gen = (i for i in range(10))
result = Series(gen)
exp = Series(range(10))
tm.assert_series_equal(result, exp)
gen = (i for i in range(10))
result = Series(gen, index=range(10, 20))
exp.index = range(10, 20)
tm.assert_series_equal(result, exp)
```

## Next Steps


---

*Source: test_constructors.py:361 | Complexity: Advanced | Last updated: 2026-06-02*
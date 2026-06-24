# How To: Loc Axis 1 Slice

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test loc axis 1 slice

## Prerequisites

**Required Modules:**
- `collections`
- `contextlib`
- `datetime`
- `re`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas._libs`
- `pandas.compat.numpy`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api.types`
- `pandas.core.indexing`
- `pandas.tests.indexing.common`


## Step-by-Step Guide

### Step 1: Assign cols = value

```python
cols = [(yr, m) for yr in [2014, 2015] for m in [7, 8, 9, 10]]
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(np.ones((10, 8)), index=tuple('ABCDEFGHIJ'), columns=MultiIndex.from_tuples(cols))
```

### Step 3: Assign result = value

```python
result = df.loc(axis=1)[(2014, 9):(2015, 8)]
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame(np.ones((10, 4)), index=tuple('ABCDEFGHIJ'), columns=MultiIndex.from_tuples([(2014, 9), (2014, 10), (2015, 7), (2015, 8)]))
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
cols = [(yr, m) for yr in [2014, 2015] for m in [7, 8, 9, 10]]
df = DataFrame(np.ones((10, 8)), index=tuple('ABCDEFGHIJ'), columns=MultiIndex.from_tuples(cols))
result = df.loc(axis=1)[(2014, 9):(2015, 8)]
expected = DataFrame(np.ones((10, 4)), index=tuple('ABCDEFGHIJ'), columns=MultiIndex.from_tuples([(2014, 9), (2014, 10), (2015, 7), (2015, 8)]))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_loc.py:2892 | Complexity: Intermediate | Last updated: 2026-06-02*
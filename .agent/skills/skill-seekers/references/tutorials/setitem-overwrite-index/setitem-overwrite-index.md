# How To: Setitem Overwrite Index

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test setitem overwrite index

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

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(index=['A', 'B', 'C'])
```

### Step 2: Assign unknown = value

```python
df['X'] = df.index
```

### Step 3: Assign unknown = value

```python
df['X'] = ['x', 'y', 'z']
```

### Step 4: Assign exp = DataFrame(...)

```python
exp = DataFrame(data={'X': ['x', 'y', 'z']}, index=['A', 'B', 'C'], columns=['X'])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, exp)
```


## Complete Example

```python
# Workflow
df = DataFrame(index=['A', 'B', 'C'])
df['X'] = df.index
df['X'] = ['x', 'y', 'z']
exp = DataFrame(data={'X': ['x', 'y', 'z']}, index=['A', 'B', 'C'], columns=['X'])
tm.assert_frame_equal(df, exp)
```

## Next Steps


---

*Source: test_setitem.py:150 | Complexity: Intermediate | Last updated: 2026-06-02*
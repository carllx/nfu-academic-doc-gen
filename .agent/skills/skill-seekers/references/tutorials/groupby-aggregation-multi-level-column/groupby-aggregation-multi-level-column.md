# How To: Groupby Aggregation Multi Level Column

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test groupby aggregation multi level column

## Prerequisites

**Required Modules:**
- `datetime`
- `functools`
- `functools`
- `re`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.groupby.grouper`


## Step-by-Step Guide

### Step 1: Assign lst = value

```python
lst = [[True, True, True, False], [True, False, np.nan, False], [True, True, np.nan, False], [True, True, np.nan, False]]
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(data=lst, columns=MultiIndex.from_tuples([('A', 0), ('A', 1), ('B', 0), ('B', 1)]))
```

### Step 3: Assign msg = 'DataFrame.groupby with axis=1 is deprecated'

```python
msg = 'DataFrame.groupby with axis=1 is deprecated'
```

### Step 4: Assign result = gb.sum(...)

```python
result = gb.sum(numeric_only=False)
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame({0: [2.0, True, True, True], 1: [1, 0, 1, 1]})
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign gb = df.groupby(...)

```python
gb = df.groupby(level=1, axis=1)
```


## Complete Example

```python
# Workflow
lst = [[True, True, True, False], [True, False, np.nan, False], [True, True, np.nan, False], [True, True, np.nan, False]]
df = DataFrame(data=lst, columns=MultiIndex.from_tuples([('A', 0), ('A', 1), ('B', 0), ('B', 1)]))
msg = 'DataFrame.groupby with axis=1 is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    gb = df.groupby(level=1, axis=1)
result = gb.sum(numeric_only=False)
expected = DataFrame({0: [2.0, True, True, True], 1: [1, 0, 1, 1]})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_aggregate.py:114 | Complexity: Intermediate | Last updated: 2026-06-02*
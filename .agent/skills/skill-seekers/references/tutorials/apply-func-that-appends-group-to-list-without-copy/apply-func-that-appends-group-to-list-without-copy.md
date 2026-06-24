# How To: Apply Func That Appends Group To List Without Copy

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test apply func that appends group to list without copy

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.groupby`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame.reset_index(...)

```python
df = DataFrame(1, index=list(range(10)) * 10, columns=[0]).reset_index()
```

### Step 2: Assign groups = value

```python
groups = []
```

### Step 3: Assign msg = 'DataFrameGroupBy.apply operated on the grouping columns'

```python
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
```

### Step 4: Assign expected_value = DataFrame(...)

```python
expected_value = DataFrame({'index': [0] * 10, 0: [1] * 10}, index=pd.RangeIndex(0, 100, 10))
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(groups[0], expected_value)
```

### Step 6: Call groups.append()

```python
groups.append(group)
```

### Step 7: Call df.groupby.apply()

```python
df.groupby('index').apply(store)
```


## Complete Example

```python
# Workflow
df = DataFrame(1, index=list(range(10)) * 10, columns=[0]).reset_index()
groups = []

def store(group):
    groups.append(group)
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
with tm.assert_produces_warning(FutureWarning, match=msg):
    df.groupby('index').apply(store)
expected_value = DataFrame({'index': [0] * 10, 0: [1] * 10}, index=pd.RangeIndex(0, 100, 10))
tm.assert_frame_equal(groups[0], expected_value)
```

## Next Steps


---

*Source: test_apply.py:23 | Complexity: Intermediate | Last updated: 2026-06-02*
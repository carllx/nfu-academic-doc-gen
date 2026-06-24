# How To: Wrap Agg Out

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test wrap agg out

## Prerequisites

- [ ] Setup code must be executed first

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

**Setup Required:**
```python
# Fixtures: three_group
```

## Step-by-Step Guide

### Step 1: Assign grouped = three_group.groupby(...)

```python
grouped = three_group.groupby(['A', 'B'])
```

### Step 2: Assign result = unknown.aggregate(...)

```python
result = grouped[['D', 'E', 'F']].aggregate(func)
```

### Step 3: Assign exp_grouped = value

```python
exp_grouped = three_group.loc[:, ['A', 'B', 'D', 'E', 'F']]
```

### Step 4: Assign expected = exp_grouped.groupby.aggregate(...)

```python
expected = exp_grouped.groupby(['A', 'B']).aggregate(func)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Call grouped.aggregate()

```python
grouped.aggregate(func)
```


## Complete Example

```python
# Setup
# Fixtures: three_group

# Workflow
grouped = three_group.groupby(['A', 'B'])

def func(ser):
    if ser.dtype in (object, 'string'):
        raise TypeError('Test error message')
    return ser.sum()
with pytest.raises(TypeError, match='Test error message'):
    grouped.aggregate(func)
result = grouped[['D', 'E', 'F']].aggregate(func)
exp_grouped = three_group.loc[:, ['A', 'B', 'D', 'E', 'F']]
expected = exp_grouped.groupby(['A', 'B']).aggregate(func)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_aggregate.py:336 | Complexity: Intermediate | Last updated: 2026-06-02*
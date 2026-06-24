# How To: Suffix On List Join

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test suffix on list join

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.reshape.concat`


## Step-by-Step Guide

### Step 1: Assign first = DataFrame(...)

```python
first = DataFrame({'key': [1, 2, 3, 4, 5]})
```

### Step 2: Assign second = DataFrame(...)

```python
second = DataFrame({'key': [1, 8, 3, 2, 5], 'v1': [1, 2, 3, 4, 5]})
```

### Step 3: Assign third = DataFrame(...)

```python
third = DataFrame({'keys': [5, 2, 3, 4, 1], 'v2': [1, 2, 3, 4, 5]})
```

### Step 4: Assign msg = 'Suffixes not supported when joining multiple DataFrames'

```python
msg = 'Suffixes not supported when joining multiple DataFrames'
```

### Step 5: Assign arr_joined = first.join(...)

```python
arr_joined = first.join([third])
```

### Step 6: Assign norm_joined = first.join(...)

```python
norm_joined = first.join(third)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(arr_joined, norm_joined)
```

### Step 8: Call first.join()

```python
first.join([second], lsuffix='y')
```

### Step 9: Call first.join()

```python
first.join([second, third], rsuffix='x')
```

### Step 10: Call first.join()

```python
first.join([second, third], lsuffix='y', rsuffix='x')
```

### Step 11: Call first.join()

```python
first.join([second, third])
```


## Complete Example

```python
# Workflow
first = DataFrame({'key': [1, 2, 3, 4, 5]})
second = DataFrame({'key': [1, 8, 3, 2, 5], 'v1': [1, 2, 3, 4, 5]})
third = DataFrame({'keys': [5, 2, 3, 4, 1], 'v2': [1, 2, 3, 4, 5]})
msg = 'Suffixes not supported when joining multiple DataFrames'
with pytest.raises(ValueError, match=msg):
    first.join([second], lsuffix='y')
with pytest.raises(ValueError, match=msg):
    first.join([second, third], rsuffix='x')
with pytest.raises(ValueError, match=msg):
    first.join([second, third], lsuffix='y', rsuffix='x')
with pytest.raises(ValueError, match='Indexes have overlapping values'):
    first.join([second, third])
arr_joined = first.join([third])
norm_joined = first.join(third)
tm.assert_frame_equal(arr_joined, norm_joined)
```

## Next Steps


---

*Source: test_join.py:120 | Complexity: Advanced | Last updated: 2026-06-02*
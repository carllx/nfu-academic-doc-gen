# How To: Merge Asof Numeri Column In Index Object Dtype

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test merge asof numeri column in index object dtype

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pytz`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.reshape.merge`


## Step-by-Step Guide

### Step 1: Assign left = pd.DataFrame(...)

```python
left = pd.DataFrame({'b': [10, 11, 12]}, index=Index(['1', '2', '3'], name='a'))
```

### Step 2: Assign right = pd.DataFrame(...)

```python
right = pd.DataFrame({'c': [20, 21, 22]}, index=Index(['m', 'n', 'o'], name='a'))
```

### Step 3: Assign left = left.reset_index.set_index(...)

```python
left = left.reset_index().set_index(['a', 'b'])
```

### Step 4: Assign right = right.reset_index.set_index(...)

```python
right = right.reset_index().set_index(['a', 'c'])
```

### Step 5: Call merge_asof()

```python
merge_asof(left, right, left_on='a', right_on='a')
```

### Step 6: Call merge_asof()

```python
merge_asof(left, right, left_on='a', right_on='a')
```


## Complete Example

```python
# Workflow
left = pd.DataFrame({'b': [10, 11, 12]}, index=Index(['1', '2', '3'], name='a'))
right = pd.DataFrame({'c': [20, 21, 22]}, index=Index(['m', 'n', 'o'], name='a'))
with pytest.raises(MergeError, match='Incompatible merge dtype, .*, both sides must have numeric dtype'):
    merge_asof(left, right, left_on='a', right_on='a')
left = left.reset_index().set_index(['a', 'b'])
right = right.reset_index().set_index(['a', 'c'])
with pytest.raises(MergeError, match='Incompatible merge dtype, .*, both sides must have numeric dtype'):
    merge_asof(left, right, left_on='a', right_on='a')
```

## Next Steps


---

*Source: test_merge_asof.py:3468 | Complexity: Intermediate | Last updated: 2026-06-02*
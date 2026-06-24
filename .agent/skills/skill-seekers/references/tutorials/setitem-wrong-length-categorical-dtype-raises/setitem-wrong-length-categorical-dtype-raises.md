# How To: Setitem Wrong Length Categorical Dtype Raises

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test setitem wrong length categorical dtype raises

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

### Step 1: Assign cat = Categorical.from_codes(...)

```python
cat = Categorical.from_codes([0, 1, 1, 0, 1, 2], ['a', 'b', 'c'])
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(range(10), columns=['bar'])
```

### Step 3: Assign msg = value

```python
msg = f'Length of values \\({len(cat)}\\) does not match length of index \\({len(df)}\\)'
```

### Step 4: Assign unknown = cat

```python
df['foo'] = cat
```


## Complete Example

```python
# Workflow
cat = Categorical.from_codes([0, 1, 1, 0, 1, 2], ['a', 'b', 'c'])
df = DataFrame(range(10), columns=['bar'])
msg = f'Length of values \\({len(cat)}\\) does not match length of index \\({len(df)}\\)'
with pytest.raises(ValueError, match=msg):
    df['foo'] = cat
```

## Next Steps


---

*Source: test_setitem.py:193 | Complexity: Intermediate | Last updated: 2026-06-02*
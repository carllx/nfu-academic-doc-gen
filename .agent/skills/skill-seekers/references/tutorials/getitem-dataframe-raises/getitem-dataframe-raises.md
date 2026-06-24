# How To: Getitem Dataframe Raises

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test getitem dataframe raises

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.indexing`
- `pandas.tseries.offsets`


## Step-by-Step Guide

### Step 1: Assign rng = list(...)

```python
rng = list(range(10))
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(10, index=rng)
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(rng, index=rng)
```

### Step 4: Assign msg = 'Indexing a Series with DataFrame is not supported, use the appropriate DataFrame column'

```python
msg = 'Indexing a Series with DataFrame is not supported, use the appropriate DataFrame column'
```

### Step 5: ser[df > 5]

```python
ser[df > 5]
```


## Complete Example

```python
# Workflow
rng = list(range(10))
ser = Series(10, index=rng)
df = DataFrame(rng, index=rng)
msg = 'Indexing a Series with DataFrame is not supported, use the appropriate DataFrame column'
with pytest.raises(TypeError, match=msg):
    ser[df > 5]
```

## Next Steps


---

*Source: test_getitem.py:586 | Complexity: Intermediate | Last updated: 2026-06-02*
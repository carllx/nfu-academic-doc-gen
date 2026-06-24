# How To: Loc Slice Disallows Positional

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test loc slice disallows positional

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

### Step 1: Assign dti = date_range(...)

```python
dti = date_range('2016-01-01', periods=3)
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).random((3, 2)), index=dti)
```

### Step 3: Assign ser = value

```python
ser = df[0]
```

### Step 4: Assign msg = 'cannot do slice indexing on DatetimeIndex with these indexers \\[1\\] of type int'

```python
msg = 'cannot do slice indexing on DatetimeIndex with these indexers \\[1\\] of type int'
```

### Step 5: df.loc[1:3, 1]

```python
df.loc[1:3, 1]
```

### Step 6: Assign unknown = 2

```python
df.loc[1:3, 1] = 2
```

### Step 7: obj.loc[1:3]

```python
obj.loc[1:3]
```

### Step 8: Assign unknown = 1

```python
obj.loc[1:3] = 1
```


## Complete Example

```python
# Workflow
dti = date_range('2016-01-01', periods=3)
df = DataFrame(np.random.default_rng(2).random((3, 2)), index=dti)
ser = df[0]
msg = 'cannot do slice indexing on DatetimeIndex with these indexers \\[1\\] of type int'
for obj in [df, ser]:
    with pytest.raises(TypeError, match=msg):
        obj.loc[1:3]
    with pytest.raises(TypeError, match='Slicing a positional slice with .loc'):
        obj.loc[1:3] = 1
with pytest.raises(TypeError, match=msg):
    df.loc[1:3, 1]
with pytest.raises(TypeError, match='Slicing a positional slice with .loc'):
    df.loc[1:3, 1] = 2
```

## Next Steps


---

*Source: test_loc.py:2935 | Complexity: Advanced | Last updated: 2026-06-02*
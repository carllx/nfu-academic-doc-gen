# How To: Loc Datetimelike Mismatched Dtypes

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test loc datetimelike mismatched dtypes

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

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((5, 3)), columns=['a', 'b', 'c'], index=date_range('2012', freq='h', periods=5))
```

### Step 2: Assign df = unknown.copy(...)

```python
df = df.iloc[[0, 2, 2, 3]].copy()
```

### Step 3: Assign dti = value

```python
dti = df.index
```

### Step 4: Assign tdi = pd.TimedeltaIndex(...)

```python
tdi = pd.TimedeltaIndex(dti.asi8)
```

### Step 5: Assign msg = 'None of \\[TimedeltaIndex.* are in the \\[index\\]'

```python
msg = 'None of \\[TimedeltaIndex.* are in the \\[index\\]'
```

### Step 6: df.loc[tdi]

```python
df.loc[tdi]
```

### Step 7: df['a'].loc[tdi]

```python
df['a'].loc[tdi]
```


## Complete Example

```python
# Workflow
df = DataFrame(np.random.default_rng(2).standard_normal((5, 3)), columns=['a', 'b', 'c'], index=date_range('2012', freq='h', periods=5))
df = df.iloc[[0, 2, 2, 3]].copy()
dti = df.index
tdi = pd.TimedeltaIndex(dti.asi8)
msg = 'None of \\[TimedeltaIndex.* are in the \\[index\\]'
with pytest.raises(KeyError, match=msg):
    df.loc[tdi]
with pytest.raises(KeyError, match=msg):
    df['a'].loc[tdi]
```

## Next Steps


---

*Source: test_loc.py:2963 | Complexity: Intermediate | Last updated: 2026-06-02*
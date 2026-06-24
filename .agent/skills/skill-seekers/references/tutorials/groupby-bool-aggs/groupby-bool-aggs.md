# How To: Groupby Bool Aggs

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test groupby bool aggs

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `builtins`
- `datetime`
- `string`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.core.dtypes.common`
- `pandas.core.dtypes.missing`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.groupby`
- `pandas.util`
- `scipy.stats`

**Setup Required:**
```python
# Fixtures: skipna, agg_func, vals
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'key': ['a'] * 3 + ['b'] * 3, 'val': vals * 2})
```

### Step 2: Assign exp = getattr(...)

```python
exp = getattr(builtins, agg_func)(vals)
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame([exp] * 2, columns=['val'], index=pd.Index(['a', 'b'], name='key'))
```

### Step 4: Assign result = getattr(...)

```python
result = getattr(df.groupby('key'), agg_func)(skipna=skipna)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign exp = False

```python
exp = False
```


## Complete Example

```python
# Setup
# Fixtures: skipna, agg_func, vals

# Workflow
df = DataFrame({'key': ['a'] * 3 + ['b'] * 3, 'val': vals * 2})
exp = getattr(builtins, agg_func)(vals)
if skipna and all(isna(vals)) and (agg_func == 'any'):
    exp = False
expected = DataFrame([exp] * 2, columns=['val'], index=pd.Index(['a', 'b'], name='key'))
result = getattr(df.groupby('key'), agg_func)(skipna=skipna)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_reductions.py:46 | Complexity: Intermediate | Last updated: 2026-06-02*
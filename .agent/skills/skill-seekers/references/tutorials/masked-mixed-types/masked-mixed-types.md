# How To: Masked Mixed Types

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test masked mixed types

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
# Fixtures: dtype1, dtype2, exp_col1, exp_col2
```

## Step-by-Step Guide

### Step 1: Assign data = value

```python
data = [1.0, np.nan]
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'col1': pd.array(data, dtype=dtype1), 'col2': pd.array(data, dtype=dtype2)})
```

### Step 3: Assign result = df.groupby.agg(...)

```python
result = df.groupby([1, 1]).agg('all', skipna=False)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'col1': exp_col1, 'col2': exp_col2}, index=np.array([1]))
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: dtype1, dtype2, exp_col1, exp_col2

# Workflow
data = [1.0, np.nan]
df = DataFrame({'col1': pd.array(data, dtype=dtype1), 'col2': pd.array(data, dtype=dtype2)})
result = df.groupby([1, 1]).agg('all', skipna=False)
expected = DataFrame({'col1': exp_col1, 'col2': exp_col2}, index=np.array([1]))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_reductions.py:141 | Complexity: Intermediate | Last updated: 2026-06-02*
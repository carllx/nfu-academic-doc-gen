# How To: Dup Labels Output Shape

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test dup labels output shape

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.groupby`

**Setup Required:**
```python
# Fixtures: groupby_func, idx
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([[1, 1]], columns=idx)
```

**Verification:**
```python
assert result.shape == (1, 2)
```

### Step 2: Assign grp_by = df.groupby(...)

```python
grp_by = df.groupby([0])
```

### Step 3: Assign args = get_groupby_method_args(...)

```python
args = get_groupby_method_args(groupby_func, df)
```

### Step 4: Assign warn = value

```python
warn = FutureWarning if groupby_func == 'fillna' else None
```

### Step 5: Assign warn_msg = 'DataFrameGroupBy.fillna is deprecated'

```python
warn_msg = 'DataFrameGroupBy.fillna is deprecated'
```

**Verification:**
```python
assert result.shape == (1, 2)
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result.columns, idx)
```

### Step 7: Call pytest.skip()

```python
pytest.skip(f'Not applicable for {groupby_func}')
```

### Step 8: Assign result = getattr(...)

```python
result = getattr(grp_by, groupby_func)(*args)
```


## Complete Example

```python
# Setup
# Fixtures: groupby_func, idx

# Workflow
if groupby_func in {'size', 'ngroup', 'cumcount'}:
    pytest.skip(f'Not applicable for {groupby_func}')
df = DataFrame([[1, 1]], columns=idx)
grp_by = df.groupby([0])
args = get_groupby_method_args(groupby_func, df)
warn = FutureWarning if groupby_func == 'fillna' else None
warn_msg = 'DataFrameGroupBy.fillna is deprecated'
with tm.assert_produces_warning(warn, match=warn_msg):
    result = getattr(grp_by, groupby_func)(*args)
assert result.shape == (1, 2)
tm.assert_index_equal(result.columns, idx)
```

## Next Steps


---

*Source: test_all_methods.py:69 | Complexity: Advanced | Last updated: 2026-06-02*
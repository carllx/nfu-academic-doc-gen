# How To: Multiindex Group All Columns When Empty

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multiindex group all columns when empty

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
# Fixtures: groupby_func
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame.set_index(...)

```python
df = DataFrame({'a': [], 'b': [], 'c': []}).set_index(['a', 'b', 'c'])
```

### Step 2: Assign gb = df.groupby(...)

```python
gb = df.groupby(['a', 'b', 'c'], group_keys=False)
```

### Step 3: Assign method = getattr(...)

```python
method = getattr(gb, groupby_func)
```

### Step 4: Assign args = get_groupby_method_args(...)

```python
args = get_groupby_method_args(groupby_func, df)
```

### Step 5: Assign warn = value

```python
warn = FutureWarning if groupby_func == 'fillna' else None
```

### Step 6: Assign warn_msg = 'DataFrameGroupBy.fillna is deprecated'

```python
warn_msg = 'DataFrameGroupBy.fillna is deprecated'
```

### Step 7: Assign expected = value

```python
expected = df.index
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 9: Assign result = value

```python
result = method(*args).index
```


## Complete Example

```python
# Setup
# Fixtures: groupby_func

# Workflow
df = DataFrame({'a': [], 'b': [], 'c': []}).set_index(['a', 'b', 'c'])
gb = df.groupby(['a', 'b', 'c'], group_keys=False)
method = getattr(gb, groupby_func)
args = get_groupby_method_args(groupby_func, df)
warn = FutureWarning if groupby_func == 'fillna' else None
warn_msg = 'DataFrameGroupBy.fillna is deprecated'
with tm.assert_produces_warning(warn, match=warn_msg):
    result = method(*args).index
expected = df.index
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_all_methods.py:22 | Complexity: Advanced | Last updated: 2026-06-02*
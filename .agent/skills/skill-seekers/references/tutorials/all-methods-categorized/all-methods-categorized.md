# How To: All Methods Categorized

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test all methods categorized

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `inspect`
- `pytest`
- `pandas`
- `pandas.core.groupby.base`
- `pandas.core.groupby.generic`

**Setup Required:**
```python
# Fixtures: multiindex_dataframe_random_data
```

## Step-by-Step Guide

### Step 1: Assign grp = multiindex_dataframe_random_data.groupby(...)

```python
grp = multiindex_dataframe_random_data.groupby(multiindex_dataframe_random_data.iloc[:, 0])
```

**Verification:**
```python
assert not reduction_kernels & transformation_kernels
```

### Step 2: Assign names = value

```python
names = {_ for _ in dir(grp) if not _.startswith('_')} - set(multiindex_dataframe_random_data.columns)
```

**Verification:**
```python
assert not reduction_kernels & groupby_other_methods
```

### Step 3: Assign new_names = set(...)

```python
new_names = set(names)
```

**Verification:**
```python
assert not transformation_kernels & groupby_other_methods
```

### Step 4: Assign all_categorized = value

```python
all_categorized = reduction_kernels | transformation_kernels | groupby_other_methods
```

### Step 5: Assign msg = value

```python
msg = f'\nThere are uncategorized methods defined on the Grouper class:\n{new_names}.\n\nWas a new method recently added?\n\nEvery public method On Grouper must appear in exactly one the\nfollowing three lists defined in pandas.core.groupby.base:\n- `reduction_kernels`\n- `transformation_kernels`\n- `groupby_other_methods`\nsee the comments in pandas/core/groupby/base.py for guidance on\nhow to fix this test.\n        '
```

### Step 6: Assign msg = value

```python
msg = f"\nSome methods which are supposed to be on the Grouper class\nare missing:\n{all_categorized - names}.\n\nThey're still defined in one of the lists that live in pandas/core/groupby/base.py.\nIf you removed a method, you should update them\n"
```


## Complete Example

```python
# Setup
# Fixtures: multiindex_dataframe_random_data

# Workflow
grp = multiindex_dataframe_random_data.groupby(multiindex_dataframe_random_data.iloc[:, 0])
names = {_ for _ in dir(grp) if not _.startswith('_')} - set(multiindex_dataframe_random_data.columns)
new_names = set(names)
new_names -= reduction_kernels
new_names -= transformation_kernels
new_names -= groupby_other_methods
assert not reduction_kernels & transformation_kernels
assert not reduction_kernels & groupby_other_methods
assert not transformation_kernels & groupby_other_methods
if new_names:
    msg = f'\nThere are uncategorized methods defined on the Grouper class:\n{new_names}.\n\nWas a new method recently added?\n\nEvery public method On Grouper must appear in exactly one the\nfollowing three lists defined in pandas.core.groupby.base:\n- `reduction_kernels`\n- `transformation_kernels`\n- `groupby_other_methods`\nsee the comments in pandas/core/groupby/base.py for guidance on\nhow to fix this test.\n        '
    raise AssertionError(msg)
all_categorized = reduction_kernels | transformation_kernels | groupby_other_methods
if names != all_categorized:
    msg = f"\nSome methods which are supposed to be on the Grouper class\nare missing:\n{all_categorized - names}.\n\nThey're still defined in one of the lists that live in pandas/core/groupby/base.py.\nIf you removed a method, you should update them\n"
    raise AssertionError(msg)
```

## Next Steps


---

*Source: test_api.py:101 | Complexity: Intermediate | Last updated: 2026-06-02*
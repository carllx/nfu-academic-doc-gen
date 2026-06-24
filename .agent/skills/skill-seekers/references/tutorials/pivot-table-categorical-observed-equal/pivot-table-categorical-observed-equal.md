# How To: Pivot Table Categorical Observed Equal

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test pivot table categorical observed equal

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `itertools`
- `re`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api.types`
- `pandas.core.reshape`
- `pandas.core.reshape.pivot`

**Setup Required:**
```python
# Fixtures: observed
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'col1': list('abcde'), 'col2': list('fghij'), 'col3': [1, 2, 3, 4, 5]})
```

### Step 2: Assign expected = df.pivot_table(...)

```python
expected = df.pivot_table(index='col1', values='col3', columns='col2', aggfunc='sum', fill_value=0)
```

### Step 3: Assign expected.index = expected.index.astype(...)

```python
expected.index = expected.index.astype('category')
```

### Step 4: Assign expected.columns = expected.columns.astype(...)

```python
expected.columns = expected.columns.astype('category')
```

### Step 5: Assign df.col1 = df.col1.astype(...)

```python
df.col1 = df.col1.astype('category')
```

### Step 6: Assign df.col2 = df.col2.astype(...)

```python
df.col2 = df.col2.astype('category')
```

### Step 7: Assign result = df.pivot_table(...)

```python
result = df.pivot_table(index='col1', values='col3', columns='col2', aggfunc='sum', fill_value=0, observed=observed)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: observed

# Workflow
df = DataFrame({'col1': list('abcde'), 'col2': list('fghij'), 'col3': [1, 2, 3, 4, 5]})
expected = df.pivot_table(index='col1', values='col3', columns='col2', aggfunc='sum', fill_value=0)
expected.index = expected.index.astype('category')
expected.columns = expected.columns.astype('category')
df.col1 = df.col1.astype('category')
df.col2 = df.col2.astype('category')
result = df.pivot_table(index='col1', values='col3', columns='col2', aggfunc='sum', fill_value=0, observed=observed)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_pivot.py:122 | Complexity: Advanced | Last updated: 2026-06-02*
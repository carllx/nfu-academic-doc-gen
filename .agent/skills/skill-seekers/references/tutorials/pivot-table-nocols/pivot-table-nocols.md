# How To: Pivot Table Nocols

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test pivot table nocols

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'rows': ['a', 'b', 'c'], 'cols': ['x', 'y', 'z'], 'values': [1, 2, 3]})
```

### Step 2: Assign rs = df.pivot_table(...)

```python
rs = df.pivot_table(columns='cols', aggfunc='sum')
```

### Step 3: Assign xp = value

```python
xp = df.pivot_table(index='cols', aggfunc='sum').T
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(rs, xp)
```

### Step 5: Assign rs = df.pivot_table(...)

```python
rs = df.pivot_table(columns='cols', aggfunc={'values': 'mean'})
```

### Step 6: Assign xp = value

```python
xp = df.pivot_table(index='cols', aggfunc={'values': 'mean'}).T
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(rs, xp)
```


## Complete Example

```python
# Workflow
df = DataFrame({'rows': ['a', 'b', 'c'], 'cols': ['x', 'y', 'z'], 'values': [1, 2, 3]})
rs = df.pivot_table(columns='cols', aggfunc='sum')
xp = df.pivot_table(index='cols', aggfunc='sum').T
tm.assert_frame_equal(rs, xp)
rs = df.pivot_table(columns='cols', aggfunc={'values': 'mean'})
xp = df.pivot_table(index='cols', aggfunc={'values': 'mean'}).T
tm.assert_frame_equal(rs, xp)
```

## Next Steps


---

*Source: test_pivot.py:149 | Complexity: Intermediate | Last updated: 2026-06-02*
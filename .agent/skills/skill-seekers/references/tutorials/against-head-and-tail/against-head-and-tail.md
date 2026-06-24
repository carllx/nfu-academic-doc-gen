# How To: Against Head And Tail

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test against head and tail

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: arg, method, simulated
```

## Step-by-Step Guide

### Step 1: Assign n_groups = 100

```python
n_groups = 100
```

### Step 2: Assign n_rows_per_group = 30

```python
n_rows_per_group = 30
```

### Step 3: Assign data = value

```python
data = {'group': [f'group {g}' for j in range(n_rows_per_group) for g in range(n_groups)], 'value': [f'group {g} row {j}' for j in range(n_rows_per_group) for g in range(n_groups)]}
```

### Step 4: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame(data)
```

### Step 5: Assign grouped = df.groupby(...)

```python
grouped = df.groupby('group', as_index=False)
```

### Step 6: Assign size = value

```python
size = arg if arg >= 0 else n_rows_per_group + arg
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign result = value

```python
result = grouped._positional_selector[:arg]
```

### Step 9: Assign result = value

```python
result = grouped._positional_selector[-arg:]
```

### Step 10: Assign indices = value

```python
indices = [j * n_groups + i for j in range(size) for i in range(n_groups) if j * n_groups + i < n_groups * n_rows_per_group]
```

### Step 11: Assign expected = value

```python
expected = df.iloc[indices]
```

### Step 12: Assign expected = grouped.head(...)

```python
expected = grouped.head(arg)
```

### Step 13: Assign indices = value

```python
indices = [(n_rows_per_group + j - size) * n_groups + i for j in range(size) for i in range(n_groups) if (n_rows_per_group + j - size) * n_groups + i >= 0]
```

### Step 14: Assign expected = value

```python
expected = df.iloc[indices]
```

### Step 15: Assign expected = grouped.tail(...)

```python
expected = grouped.tail(arg)
```


## Complete Example

```python
# Setup
# Fixtures: arg, method, simulated

# Workflow
n_groups = 100
n_rows_per_group = 30
data = {'group': [f'group {g}' for j in range(n_rows_per_group) for g in range(n_groups)], 'value': [f'group {g} row {j}' for j in range(n_rows_per_group) for g in range(n_groups)]}
df = pd.DataFrame(data)
grouped = df.groupby('group', as_index=False)
size = arg if arg >= 0 else n_rows_per_group + arg
if method == 'head':
    result = grouped._positional_selector[:arg]
    if simulated:
        indices = [j * n_groups + i for j in range(size) for i in range(n_groups) if j * n_groups + i < n_groups * n_rows_per_group]
        expected = df.iloc[indices]
    else:
        expected = grouped.head(arg)
else:
    result = grouped._positional_selector[-arg:]
    if simulated:
        indices = [(n_rows_per_group + j - size) * n_groups + i for j in range(size) for i in range(n_groups) if (n_rows_per_group + j - size) * n_groups + i >= 0]
        expected = df.iloc[indices]
    else:
        expected = grouped.tail(arg)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_indexing.py:167 | Complexity: Advanced | Last updated: 2026-06-02*
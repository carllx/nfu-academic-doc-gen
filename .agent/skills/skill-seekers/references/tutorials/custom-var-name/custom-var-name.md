# How To: Custom Var Name

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test custom var name

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: df, var_name
```

## Step-by-Step Guide

### Step 1: Assign result5 = df.melt(...)

```python
result5 = df.melt(var_name=var_name)
```

**Verification:**
```python
assert result5.columns.tolist() == ['var', 'value']
```

### Step 2: Assign result6 = df.melt(...)

```python
result6 = df.melt(id_vars=['id1'], var_name=var_name)
```

**Verification:**
```python
assert result6.columns.tolist() == ['id1', 'var', 'value']
```

### Step 3: Assign result7 = df.melt(...)

```python
result7 = df.melt(id_vars=['id1', 'id2'], var_name=var_name)
```

**Verification:**
```python
assert result7.columns.tolist() == ['id1', 'id2', 'var', 'value']
```

### Step 4: Assign result8 = df.melt(...)

```python
result8 = df.melt(id_vars=['id1', 'id2'], value_vars='A', var_name=var_name)
```

**Verification:**
```python
assert result8.columns.tolist() == ['id1', 'id2', 'var', 'value']
```

### Step 5: Assign result9 = df.melt(...)

```python
result9 = df.melt(id_vars=['id1', 'id2'], value_vars=['A', 'B'], var_name=var_name)
```

### Step 6: Assign expected9 = DataFrame(...)

```python
expected9 = DataFrame({'id1': df['id1'].tolist() * 2, 'id2': df['id2'].tolist() * 2, var_name: ['A'] * 10 + ['B'] * 10, 'value': df['A'].tolist() + df['B'].tolist()}, columns=['id1', 'id2', var_name, 'value'])
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result9, expected9)
```


## Complete Example

```python
# Setup
# Fixtures: df, var_name

# Workflow
result5 = df.melt(var_name=var_name)
assert result5.columns.tolist() == ['var', 'value']
result6 = df.melt(id_vars=['id1'], var_name=var_name)
assert result6.columns.tolist() == ['id1', 'var', 'value']
result7 = df.melt(id_vars=['id1', 'id2'], var_name=var_name)
assert result7.columns.tolist() == ['id1', 'id2', 'var', 'value']
result8 = df.melt(id_vars=['id1', 'id2'], value_vars='A', var_name=var_name)
assert result8.columns.tolist() == ['id1', 'id2', 'var', 'value']
result9 = df.melt(id_vars=['id1', 'id2'], value_vars=['A', 'B'], var_name=var_name)
expected9 = DataFrame({'id1': df['id1'].tolist() * 2, 'id2': df['id2'].tolist() * 2, var_name: ['A'] * 10 + ['B'] * 10, 'value': df['A'].tolist() + df['B'].tolist()}, columns=['id1', 'id2', var_name, 'value'])
tm.assert_frame_equal(result9, expected9)
```

## Next Steps


---

*Source: test_melt.py:180 | Complexity: Intermediate | Last updated: 2026-06-02*
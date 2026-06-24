# How To: Custom Var And Value Name

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test custom var and value name

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
# Fixtures: df, value_name, var_name
```

## Step-by-Step Guide

### Step 1: Assign result15 = df.melt(...)

```python
result15 = df.melt(var_name=var_name, value_name=value_name)
```

**Verification:**
```python
assert result15.columns.tolist() == ['var', 'val']
```

### Step 2: Assign result16 = df.melt(...)

```python
result16 = df.melt(id_vars=['id1'], var_name=var_name, value_name=value_name)
```

**Verification:**
```python
assert result16.columns.tolist() == ['id1', 'var', 'val']
```

### Step 3: Assign result17 = df.melt(...)

```python
result17 = df.melt(id_vars=['id1', 'id2'], var_name=var_name, value_name=value_name)
```

**Verification:**
```python
assert result17.columns.tolist() == ['id1', 'id2', 'var', 'val']
```

### Step 4: Assign result18 = df.melt(...)

```python
result18 = df.melt(id_vars=['id1', 'id2'], value_vars='A', var_name=var_name, value_name=value_name)
```

**Verification:**
```python
assert result18.columns.tolist() == ['id1', 'id2', 'var', 'val']
```

### Step 5: Assign result19 = df.melt(...)

```python
result19 = df.melt(id_vars=['id1', 'id2'], value_vars=['A', 'B'], var_name=var_name, value_name=value_name)
```

**Verification:**
```python
assert result20.columns.tolist() == ['foo', 'value']
```

### Step 6: Assign expected19 = DataFrame(...)

```python
expected19 = DataFrame({'id1': df['id1'].tolist() * 2, 'id2': df['id2'].tolist() * 2, var_name: ['A'] * 10 + ['B'] * 10, value_name: df['A'].tolist() + df['B'].tolist()}, columns=['id1', 'id2', var_name, value_name])
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result19, expected19)
```

### Step 8: Assign df20 = df.copy(...)

```python
df20 = df.copy()
```

### Step 9: Assign df20.columns.name = 'foo'

```python
df20.columns.name = 'foo'
```

### Step 10: Assign result20 = df20.melt(...)

```python
result20 = df20.melt()
```

**Verification:**
```python
assert result20.columns.tolist() == ['foo', 'value']
```


## Complete Example

```python
# Setup
# Fixtures: df, value_name, var_name

# Workflow
result15 = df.melt(var_name=var_name, value_name=value_name)
assert result15.columns.tolist() == ['var', 'val']
result16 = df.melt(id_vars=['id1'], var_name=var_name, value_name=value_name)
assert result16.columns.tolist() == ['id1', 'var', 'val']
result17 = df.melt(id_vars=['id1', 'id2'], var_name=var_name, value_name=value_name)
assert result17.columns.tolist() == ['id1', 'id2', 'var', 'val']
result18 = df.melt(id_vars=['id1', 'id2'], value_vars='A', var_name=var_name, value_name=value_name)
assert result18.columns.tolist() == ['id1', 'id2', 'var', 'val']
result19 = df.melt(id_vars=['id1', 'id2'], value_vars=['A', 'B'], var_name=var_name, value_name=value_name)
expected19 = DataFrame({'id1': df['id1'].tolist() * 2, 'id2': df['id2'].tolist() * 2, var_name: ['A'] * 10 + ['B'] * 10, value_name: df['A'].tolist() + df['B'].tolist()}, columns=['id1', 'id2', var_name, value_name])
tm.assert_frame_equal(result19, expected19)
df20 = df.copy()
df20.columns.name = 'foo'
result20 = df20.melt()
assert result20.columns.tolist() == ['foo', 'value']
```

## Next Steps


---

*Source: test_melt.py:236 | Complexity: Advanced | Last updated: 2026-06-02*
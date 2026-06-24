# How To: Custom Value Name

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test custom value name

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
# Fixtures: df, value_name
```

## Step-by-Step Guide

### Step 1: Assign result10 = df.melt(...)

```python
result10 = df.melt(value_name=value_name)
```

**Verification:**
```python
assert result10.columns.tolist() == ['variable', 'val']
```

### Step 2: Assign result11 = df.melt(...)

```python
result11 = df.melt(id_vars=['id1'], value_name=value_name)
```

**Verification:**
```python
assert result11.columns.tolist() == ['id1', 'variable', 'val']
```

### Step 3: Assign result12 = df.melt(...)

```python
result12 = df.melt(id_vars=['id1', 'id2'], value_name=value_name)
```

**Verification:**
```python
assert result12.columns.tolist() == ['id1', 'id2', 'variable', 'val']
```

### Step 4: Assign result13 = df.melt(...)

```python
result13 = df.melt(id_vars=['id1', 'id2'], value_vars='A', value_name=value_name)
```

**Verification:**
```python
assert result13.columns.tolist() == ['id1', 'id2', 'variable', 'val']
```

### Step 5: Assign result14 = df.melt(...)

```python
result14 = df.melt(id_vars=['id1', 'id2'], value_vars=['A', 'B'], value_name=value_name)
```

### Step 6: Assign expected14 = DataFrame(...)

```python
expected14 = DataFrame({'id1': df['id1'].tolist() * 2, 'id2': df['id2'].tolist() * 2, 'variable': ['A'] * 10 + ['B'] * 10, value_name: df['A'].tolist() + df['B'].tolist()}, columns=['id1', 'id2', 'variable', value_name])
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result14, expected14)
```


## Complete Example

```python
# Setup
# Fixtures: df, value_name

# Workflow
result10 = df.melt(value_name=value_name)
assert result10.columns.tolist() == ['variable', 'val']
result11 = df.melt(id_vars=['id1'], value_name=value_name)
assert result11.columns.tolist() == ['id1', 'variable', 'val']
result12 = df.melt(id_vars=['id1', 'id2'], value_name=value_name)
assert result12.columns.tolist() == ['id1', 'id2', 'variable', 'val']
result13 = df.melt(id_vars=['id1', 'id2'], value_vars='A', value_name=value_name)
assert result13.columns.tolist() == ['id1', 'id2', 'variable', 'val']
result14 = df.melt(id_vars=['id1', 'id2'], value_vars=['A', 'B'], value_name=value_name)
expected14 = DataFrame({'id1': df['id1'].tolist() * 2, 'id2': df['id2'].tolist() * 2, 'variable': ['A'] * 10 + ['B'] * 10, value_name: df['A'].tolist() + df['B'].tolist()}, columns=['id1', 'id2', 'variable', value_name])
tm.assert_frame_equal(result14, expected14)
```

## Next Steps


---

*Source: test_melt.py:207 | Complexity: Intermediate | Last updated: 2026-06-02*
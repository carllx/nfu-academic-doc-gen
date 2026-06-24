# How To: Numeric Like Ops

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test numeric like ops

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'value': np.random.default_rng(2).integers(0, 10000, 100)})
```

### Step 2: Assign labels = value

```python
labels = [f'{i} - {i + 499}' for i in range(0, 10000, 500)]
```

### Step 3: Assign cat_labels = Categorical(...)

```python
cat_labels = Categorical(labels, labels)
```

### Step 4: Assign df = df.sort_values(...)

```python
df = df.sort_values(by=['value'], ascending=True)
```

### Step 5: Assign unknown = pd.cut(...)

```python
df['value_group'] = pd.cut(df.value, range(0, 10500, 500), right=False, labels=cat_labels)
```

### Step 6: Assign s = value

```python
s = df['value_group']
```

### Step 7: Assign msg = value

```python
msg = f'Series cannot perform the operation {str_rep}|unsupported operand'
```

### Step 8: Assign msg = value

```python
msg = f"does not support reduction '{op}'"
```

### Step 9: Call getattr()

```python
getattr(df, op)(df)
```

### Step 10: Call getattr()

```python
getattr(s, op)(numeric_only=False)
```


## Complete Example

```python
# Workflow
df = DataFrame({'value': np.random.default_rng(2).integers(0, 10000, 100)})
labels = [f'{i} - {i + 499}' for i in range(0, 10000, 500)]
cat_labels = Categorical(labels, labels)
df = df.sort_values(by=['value'], ascending=True)
df['value_group'] = pd.cut(df.value, range(0, 10500, 500), right=False, labels=cat_labels)
for op, str_rep in [('__add__', '\\+'), ('__sub__', '-'), ('__mul__', '\\*'), ('__truediv__', '/')]:
    msg = f'Series cannot perform the operation {str_rep}|unsupported operand'
    with pytest.raises(TypeError, match=msg):
        getattr(df, op)(df)
s = df['value_group']
for op in ['kurt', 'skew', 'var', 'std', 'mean', 'sum', 'median']:
    msg = f"does not support reduction '{op}'"
    with pytest.raises(TypeError, match=msg):
        getattr(s, op)(numeric_only=False)
```

## Next Steps


---

*Source: test_operators.py:358 | Complexity: Advanced | Last updated: 2026-06-02*
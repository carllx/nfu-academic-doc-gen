# How To: Matmul Message Shapes

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test matmul message shapes

## Prerequisites

**Required Modules:**
- `operator`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign a = np.random.default_rng.random(...)

```python
a = np.random.default_rng(2).random((10, 4))
```

### Step 2: Assign b = np.random.default_rng.random(...)

```python
b = np.random.default_rng(2).random((5, 3))
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(b)
```

### Step 4: Assign msg = 'shapes \\(10, 4\\) and \\(5, 3\\) not aligned'

```python
msg = 'shapes \\(10, 4\\) and \\(5, 3\\) not aligned'
```

### Step 5: a @ df

```python
a @ df
```

### Step 6: a.tolist() @ df

```python
a.tolist() @ df
```


## Complete Example

```python
# Workflow
a = np.random.default_rng(2).random((10, 4))
b = np.random.default_rng(2).random((5, 3))
df = DataFrame(b)
msg = 'shapes \\(10, 4\\) and \\(5, 3\\) not aligned'
with pytest.raises(ValueError, match=msg):
    a @ df
with pytest.raises(ValueError, match=msg):
    a.tolist() @ df
```

## Next Steps


---

*Source: test_matmul.py:86 | Complexity: Intermediate | Last updated: 2026-06-02*
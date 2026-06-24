# How To: Broadcasting Dot Cases

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test broadcasting dot cases

## Prerequisites

**Required Modules:**
- `itertools`
- `warnings`
- `pytest`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign a = np.random.rand(...)

```python
a = np.random.rand(1, 5, 4)
```

### Step 2: Assign b = np.random.rand(...)

```python
b = np.random.rand(4, 6)
```

### Step 3: Assign c = np.random.rand(...)

```python
c = np.random.rand(5, 6)
```

### Step 4: Assign d = np.random.rand(...)

```python
d = np.random.rand(10)
```

### Step 5: Call self.optimize_compare()

```python
self.optimize_compare('ijk,kl,jl', operands=[a, b, c])
```

### Step 6: Call self.optimize_compare()

```python
self.optimize_compare('ijk,kl,jl,i->i', operands=[a, b, c, d])
```

### Step 7: Assign e = np.random.rand(...)

```python
e = np.random.rand(1, 1, 5, 4)
```

### Step 8: Assign f = np.random.rand(...)

```python
f = np.random.rand(7, 7)
```

### Step 9: Call self.optimize_compare()

```python
self.optimize_compare('abjk,kl,jl', operands=[e, b, c])
```

### Step 10: Call self.optimize_compare()

```python
self.optimize_compare('abjk,kl,jl,ab->ab', operands=[e, b, c, f])
```

### Step 11: Assign g = np.arange.reshape(...)

```python
g = np.arange(64).reshape(2, 4, 8)
```

### Step 12: Call self.optimize_compare()

```python
self.optimize_compare('obk,ijk->ioj', operands=[g, g])
```


## Complete Example

```python
# Workflow
a = np.random.rand(1, 5, 4)
b = np.random.rand(4, 6)
c = np.random.rand(5, 6)
d = np.random.rand(10)
self.optimize_compare('ijk,kl,jl', operands=[a, b, c])
self.optimize_compare('ijk,kl,jl,i->i', operands=[a, b, c, d])
e = np.random.rand(1, 1, 5, 4)
f = np.random.rand(7, 7)
self.optimize_compare('abjk,kl,jl', operands=[e, b, c])
self.optimize_compare('abjk,kl,jl,ab->ab', operands=[e, b, c, f])
g = np.arange(64).reshape(2, 4, 8)
self.optimize_compare('obk,ijk->ioj', operands=[g, g])
```

## Next Steps


---

*Source: test_einsum.py:1066 | Complexity: Advanced | Last updated: 2026-06-02*
# How To: Simple Cycles Small

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test simple cycles small

## Prerequisites

**Required Modules:**
- `random`
- `itertools`
- `math`
- `pytest`
- `networkx`
- `networkx.algorithms.traversal.edgedfs`


## Step-by-Step Guide

### Step 1: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

**Verification:**
```python
assert len(c) == 1
```

### Step 2: Call nx.add_cycle()

```python
nx.add_cycle(G, [1, 2, 3])
```

**Verification:**
```python
assert self.is_cyclic_permutation(c[0], [1, 2, 3])
```

### Step 3: Assign c = sorted(...)

```python
c = sorted(nx.simple_cycles(G))
```

**Verification:**
```python
assert len(cc) == 2
```

### Step 4: Call nx.add_cycle()

```python
nx.add_cycle(G, [10, 20, 30])
```

**Verification:**
```python
assert any((self.is_cyclic_permutation(c, rc) for rc in ca))
```

### Step 5: Assign cc = sorted(...)

```python
cc = sorted(nx.simple_cycles(G))
```

**Verification:**
```python
assert len(cc) == 2
```

### Step 6: Assign ca = value

```python
ca = [[1, 2, 3], [10, 20, 30]]
```

**Verification:**
```python
assert any((self.is_cyclic_permutation(c, rc) for rc in ca))
```


## Complete Example

```python
# Workflow
G = nx.DiGraph()
nx.add_cycle(G, [1, 2, 3])
c = sorted(nx.simple_cycles(G))
assert len(c) == 1
assert self.is_cyclic_permutation(c[0], [1, 2, 3])
nx.add_cycle(G, [10, 20, 30])
cc = sorted(nx.simple_cycles(G))
assert len(cc) == 2
ca = [[1, 2, 3], [10, 20, 30]]
for c in cc:
    assert any((self.is_cyclic_permutation(c, rc) for rc in ca))
```

## Next Steps


---

*Source: test_cycles.py:111 | Complexity: Intermediate | Last updated: 2026-06-02*
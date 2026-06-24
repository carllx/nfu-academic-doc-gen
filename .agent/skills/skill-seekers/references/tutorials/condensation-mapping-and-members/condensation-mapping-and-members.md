# How To: Condensation Mapping And Members

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test condensation mapping and members

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign unknown = value

```python
G, C = self.gc[1]
```

**Verification:**
```python
assert all((n in G for n in mapping))
```

### Step 2: Assign C = sorted(...)

```python
C = sorted(C, key=len, reverse=True)
```

**Verification:**
```python
assert all((0 == cN for n, cN in mapping.items() if n in C[0]))
```

### Step 3: Assign cG = nx.condensation(...)

```python
cG = nx.condensation(G)
```

**Verification:**
```python
assert all((1 == cN for n, cN in mapping.items() if n in C[1]))
```

### Step 4: Assign mapping = value

```python
mapping = cG.graph['mapping']
```

**Verification:**
```python
assert set(C[n]) == cG.nodes[n]['members']
```


## Complete Example

```python
# Workflow
G, C = self.gc[1]
C = sorted(C, key=len, reverse=True)
cG = nx.condensation(G)
mapping = cG.graph['mapping']
assert all((n in G for n in mapping))
assert all((0 == cN for n, cN in mapping.items() if n in C[0]))
assert all((1 == cN for n, cN in mapping.items() if n in C[1]))
for n, d in cG.nodes(data=True):
    assert set(C[n]) == cG.nodes[n]['members']
```

## Next Steps


---

*Source: test_strongly_connected.py:151 | Complexity: Intermediate | Last updated: 2026-06-02*
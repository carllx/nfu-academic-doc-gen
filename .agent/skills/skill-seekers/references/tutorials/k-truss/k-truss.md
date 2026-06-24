# How To: K Truss

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test k truss

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign k_truss_subgraph = nx.k_truss(...)

```python
k_truss_subgraph = nx.k_truss(self.G, -1)
```

**Verification:**
```python
assert sorted(k_truss_subgraph.nodes()) == list(range(1, 21))
```

### Step 2: Assign k_truss_subgraph = nx.k_truss(...)

```python
k_truss_subgraph = nx.k_truss(self.G, 0)
```

**Verification:**
```python
assert sorted(k_truss_subgraph.nodes()) == list(range(1, 21))
```

### Step 3: Assign k_truss_subgraph = nx.k_truss(...)

```python
k_truss_subgraph = nx.k_truss(self.G, 1)
```

**Verification:**
```python
assert sorted(k_truss_subgraph.nodes()) == list(range(1, 21))
```

### Step 4: Assign k_truss_subgraph = nx.k_truss(...)

```python
k_truss_subgraph = nx.k_truss(self.G, 2)
```

**Verification:**
```python
assert sorted(k_truss_subgraph.nodes()) == list(range(1, 21))
```

### Step 5: Assign k_truss_subgraph = nx.k_truss(...)

```python
k_truss_subgraph = nx.k_truss(self.G, 3)
```

**Verification:**
```python
assert sorted(k_truss_subgraph.nodes()) == list(range(1, 13))
```

### Step 6: Assign k_truss_subgraph = nx.k_truss(...)

```python
k_truss_subgraph = nx.k_truss(self.G, 4)
```

**Verification:**
```python
assert sorted(k_truss_subgraph.nodes()) == list(range(1, 9))
```

### Step 7: Assign k_truss_subgraph = nx.k_truss(...)

```python
k_truss_subgraph = nx.k_truss(self.G, 5)
```

**Verification:**
```python
assert sorted(k_truss_subgraph.nodes()) == []
```


## Complete Example

```python
# Workflow
k_truss_subgraph = nx.k_truss(self.G, -1)
assert sorted(k_truss_subgraph.nodes()) == list(range(1, 21))
k_truss_subgraph = nx.k_truss(self.G, 0)
assert sorted(k_truss_subgraph.nodes()) == list(range(1, 21))
k_truss_subgraph = nx.k_truss(self.G, 1)
assert sorted(k_truss_subgraph.nodes()) == list(range(1, 21))
k_truss_subgraph = nx.k_truss(self.G, 2)
assert sorted(k_truss_subgraph.nodes()) == list(range(1, 21))
k_truss_subgraph = nx.k_truss(self.G, 3)
assert sorted(k_truss_subgraph.nodes()) == list(range(1, 13))
k_truss_subgraph = nx.k_truss(self.G, 4)
assert sorted(k_truss_subgraph.nodes()) == list(range(1, 9))
k_truss_subgraph = nx.k_truss(self.G, 5)
assert sorted(k_truss_subgraph.nodes()) == []
```

## Next Steps


---

*Source: test_core.py:181 | Complexity: Intermediate | Last updated: 2026-06-02*
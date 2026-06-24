# How To: Mandatory Integrality

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test mandatory integrality

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign byte_block_size = 32

```python
byte_block_size = 32
```

### Step 2: Assign ex_1_broken = nx.DiGraph(...)

```python
ex_1_broken = nx.DiGraph()
```

### Step 3: Call ex_1_broken.add_edge()

```python
ex_1_broken.add_edge(1, 2, **{EWL: 3.2})
```

### Step 4: Call ex_1_broken.add_edge()

```python
ex_1_broken.add_edge(1, 4, **{EWL: 2.4})
```

### Step 5: Call ex_1_broken.add_edge()

```python
ex_1_broken.add_edge(2, 3, **{EWL: 4.0})
```

### Step 6: Call ex_1_broken.add_edge()

```python
ex_1_broken.add_edge(2, 5, **{EWL: 6.3})
```

### Step 7: Assign unknown = 1.2

```python
ex_1_broken.nodes[1][NWL] = 1.2
```

### Step 8: Assign unknown = 1

```python
ex_1_broken.nodes[2][NWL] = 1
```

### Step 9: Assign unknown = 1

```python
ex_1_broken.nodes[3][NWL] = 1
```

### Step 10: Assign unknown = 1

```python
ex_1_broken.nodes[4][NWL] = 1
```

### Step 11: Assign unknown = 2

```python
ex_1_broken.nodes[5][NWL] = 2
```

### Step 12: Call nx.community.lukes_partitioning()

```python
nx.community.lukes_partitioning(ex_1_broken, byte_block_size, node_weight=NWL, edge_weight=EWL)
```


## Complete Example

```python
# Workflow
byte_block_size = 32
ex_1_broken = nx.DiGraph()
ex_1_broken.add_edge(1, 2, **{EWL: 3.2})
ex_1_broken.add_edge(1, 4, **{EWL: 2.4})
ex_1_broken.add_edge(2, 3, **{EWL: 4.0})
ex_1_broken.add_edge(2, 5, **{EWL: 6.3})
ex_1_broken.nodes[1][NWL] = 1.2
ex_1_broken.nodes[2][NWL] = 1
ex_1_broken.nodes[3][NWL] = 1
ex_1_broken.nodes[4][NWL] = 1
ex_1_broken.nodes[5][NWL] = 2
with pytest.raises(TypeError):
    nx.community.lukes_partitioning(ex_1_broken, byte_block_size, node_weight=NWL, edge_weight=EWL)
```

## Next Steps


---

*Source: test_lukes.py:133 | Complexity: Advanced | Last updated: 2026-06-02*
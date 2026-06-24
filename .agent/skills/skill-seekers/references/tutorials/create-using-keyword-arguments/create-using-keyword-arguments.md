# How To: Create Using Keyword Arguments

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test create using keyword arguments

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.classes`
- `networkx.generators.directed`
- `numpy`


## Step-by-Step Guide

### Step 1: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, gn_graph, 100, create_using=Graph())
```

**Verification:**
```python
assert sorted(G.edges()) == sorted(MG.edges())
```

### Step 2: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, gnr_graph, 100, 0.5, create_using=Graph())
```

**Verification:**
```python
assert sorted(G.edges()) == sorted(MG.edges())
```

### Step 3: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, gnc_graph, 100, create_using=Graph())
```

**Verification:**
```python
assert sorted(G.edges()) == sorted(MG.edges())
```

### Step 4: Assign G = gn_graph(...)

```python
G = gn_graph(100, seed=1)
```

### Step 5: Assign MG = gn_graph(...)

```python
MG = gn_graph(100, create_using=MultiDiGraph(), seed=1)
```

**Verification:**
```python
assert sorted(G.edges()) == sorted(MG.edges())
```

### Step 6: Assign G = gnr_graph(...)

```python
G = gnr_graph(100, 0.5, seed=1)
```

### Step 7: Assign MG = gnr_graph(...)

```python
MG = gnr_graph(100, 0.5, create_using=MultiDiGraph(), seed=1)
```

**Verification:**
```python
assert sorted(G.edges()) == sorted(MG.edges())
```

### Step 8: Assign G = gnc_graph(...)

```python
G = gnc_graph(100, seed=1)
```

### Step 9: Assign MG = gnc_graph(...)

```python
MG = gnc_graph(100, create_using=MultiDiGraph(), seed=1)
```

**Verification:**
```python
assert sorted(G.edges()) == sorted(MG.edges())
```

### Step 10: Assign G = scale_free_graph(...)

```python
G = scale_free_graph(100, alpha=0.3, beta=0.4, gamma=0.3, delta_in=0.3, delta_out=0.1, initial_graph=nx.cycle_graph(4, create_using=MultiDiGraph), seed=1)
```

### Step 11: Call pytest.raises()

```python
pytest.raises(ValueError, scale_free_graph, 100, 0.5, 0.4, 0.3)
```

### Step 12: Call pytest.raises()

```python
pytest.raises(ValueError, scale_free_graph, 100, alpha=-0.3)
```

### Step 13: Call pytest.raises()

```python
pytest.raises(ValueError, scale_free_graph, 100, beta=-0.3)
```

### Step 14: Call pytest.raises()

```python
pytest.raises(ValueError, scale_free_graph, 100, gamma=-0.3)
```


## Complete Example

```python
# Workflow
pytest.raises(nx.NetworkXError, gn_graph, 100, create_using=Graph())
pytest.raises(nx.NetworkXError, gnr_graph, 100, 0.5, create_using=Graph())
pytest.raises(nx.NetworkXError, gnc_graph, 100, create_using=Graph())
G = gn_graph(100, seed=1)
MG = gn_graph(100, create_using=MultiDiGraph(), seed=1)
assert sorted(G.edges()) == sorted(MG.edges())
G = gnr_graph(100, 0.5, seed=1)
MG = gnr_graph(100, 0.5, create_using=MultiDiGraph(), seed=1)
assert sorted(G.edges()) == sorted(MG.edges())
G = gnc_graph(100, seed=1)
MG = gnc_graph(100, create_using=MultiDiGraph(), seed=1)
assert sorted(G.edges()) == sorted(MG.edges())
G = scale_free_graph(100, alpha=0.3, beta=0.4, gamma=0.3, delta_in=0.3, delta_out=0.1, initial_graph=nx.cycle_graph(4, create_using=MultiDiGraph), seed=1)
pytest.raises(ValueError, scale_free_graph, 100, 0.5, 0.4, 0.3)
pytest.raises(ValueError, scale_free_graph, 100, alpha=-0.3)
pytest.raises(ValueError, scale_free_graph, 100, beta=-0.3)
pytest.raises(ValueError, scale_free_graph, 100, gamma=-0.3)
```

## Next Steps


---

*Source: test_directed.py:40 | Complexity: Advanced | Last updated: 2026-06-02*
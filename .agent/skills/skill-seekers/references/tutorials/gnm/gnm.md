# How To: Gnm

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test gnm

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = nx.gnm_random_graph(...)

```python
G = nx.gnm_random_graph(10, 3)
```

**Verification:**
```python
assert len(G) == 10
```

### Step 2: Assign G = nx.gnm_random_graph(...)

```python
G = nx.gnm_random_graph(10, 3, seed=42)
```

**Verification:**
```python
assert G.number_of_edges() == 3
```

### Step 3: Assign G = nx.gnm_random_graph(...)

```python
G = nx.gnm_random_graph(10, 100)
```

**Verification:**
```python
assert len(G) == 10
```

### Step 4: Assign G = nx.gnm_random_graph(...)

```python
G = nx.gnm_random_graph(10, 100, directed=True)
```

**Verification:**
```python
assert G.number_of_edges() == 3
```

### Step 5: Assign G = nx.gnm_random_graph(...)

```python
G = nx.gnm_random_graph(10, -1.1)
```

**Verification:**
```python
assert len(G) == 10
```


## Complete Example

```python
# Workflow
G = nx.gnm_random_graph(10, 3)
assert len(G) == 10
assert G.number_of_edges() == 3
G = nx.gnm_random_graph(10, 3, seed=42)
assert len(G) == 10
assert G.number_of_edges() == 3
G = nx.gnm_random_graph(10, 100)
assert len(G) == 10
assert G.number_of_edges() == 45
G = nx.gnm_random_graph(10, 100, directed=True)
assert len(G) == 10
assert G.number_of_edges() == 90
G = nx.gnm_random_graph(10, -1.1)
assert len(G) == 10
assert G.number_of_edges() == 0
```

## Next Steps


---

*Source: test_random_graphs.py:268 | Complexity: Intermediate | Last updated: 2026-06-02*
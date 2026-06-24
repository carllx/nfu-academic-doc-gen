# How To: Empty Graph

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test empty graph

## Prerequisites

**Required Modules:**
- `itertools`
- `typing`
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign G = nx.empty_graph(...)

```python
G = nx.empty_graph()
```

**Verification:**
```python
assert nx.number_of_nodes(G) == 0
```

### Step 2: Assign G = nx.empty_graph(...)

```python
G = nx.empty_graph(42)
```

**Verification:**
```python
assert nx.number_of_nodes(G) == 42
```

### Step 3: Assign G = nx.empty_graph(...)

```python
G = nx.empty_graph('abc')
```

**Verification:**
```python
assert nx.number_of_edges(G) == 0
```

### Step 4: Assign G = nx.empty_graph(...)

```python
G = nx.empty_graph(42, create_using=nx.DiGraph(name='duh'))
```

**Verification:**
```python
assert len(G) == 3
```

### Step 5: Assign G = nx.empty_graph(...)

```python
G = nx.empty_graph(42, create_using=nx.MultiGraph(name='duh'))
```

**Verification:**
```python
assert G.size() == 0
```

### Step 6: Assign pete = nx.petersen_graph(...)

```python
pete = nx.petersen_graph()
```

**Verification:**
```python
assert nx.number_of_nodes(G) == 42
```

### Step 7: Assign G = nx.empty_graph(...)

```python
G = nx.empty_graph(42, create_using=pete)
```

**Verification:**
```python
assert nx.number_of_edges(G) == 0
```


## Complete Example

```python
# Workflow
G = nx.empty_graph()
assert nx.number_of_nodes(G) == 0
G = nx.empty_graph(42)
assert nx.number_of_nodes(G) == 42
assert nx.number_of_edges(G) == 0
G = nx.empty_graph('abc')
assert len(G) == 3
assert G.size() == 0
G = nx.empty_graph(42, create_using=nx.DiGraph(name='duh'))
assert nx.number_of_nodes(G) == 42
assert nx.number_of_edges(G) == 0
assert isinstance(G, nx.DiGraph)
G = nx.empty_graph(42, create_using=nx.MultiGraph(name='duh'))
assert nx.number_of_nodes(G) == 42
assert nx.number_of_edges(G) == 0
assert isinstance(G, nx.MultiGraph)
pete = nx.petersen_graph()
G = nx.empty_graph(42, create_using=pete)
assert nx.number_of_nodes(G) == 42
assert nx.number_of_edges(G) == 0
assert isinstance(G, nx.Graph)
```

## Next Steps


---

*Source: test_classic.py:303 | Complexity: Intermediate | Last updated: 2026-06-02*
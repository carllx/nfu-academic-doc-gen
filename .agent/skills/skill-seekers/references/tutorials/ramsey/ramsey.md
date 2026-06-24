# How To: Ramsey

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test ramsey

## Prerequisites

**Required Modules:**
- `networkx`
- `networkx.algorithms.approximation`


## Step-by-Step Guide

### Step 1: Assign graph = nx.complete_graph(...)

```python
graph = nx.complete_graph(10)
```

**Verification:**
```python
assert cdens == 1.0, 'clique not correctly found by ramsey!'
```

### Step 2: Assign unknown = apxa.ramsey_R2(...)

```python
c, i = apxa.ramsey_R2(graph)
```

**Verification:**
```python
assert idens == 0.0, 'i-set not correctly found by ramsey!'
```

### Step 3: Assign cdens = nx.density(...)

```python
cdens = nx.density(graph.subgraph(c))
```

**Verification:**
```python
assert c == {0}, 'clique not correctly found by ramsey!'
```

### Step 4: Assign idens = nx.density(...)

```python
idens = nx.density(graph.subgraph(i))
```

**Verification:**
```python
assert i == {0}, 'i-set not correctly found by ramsey!'
```

### Step 5: Assign graph = nx.trivial_graph(...)

```python
graph = nx.trivial_graph()
```

**Verification:**
```python
assert cdens == 1.0, 'clique not correctly found by ramsey!'
```

### Step 6: Assign unknown = apxa.ramsey_R2(...)

```python
c, i = apxa.ramsey_R2(graph)
```

**Verification:**
```python
assert idens == 0.0, 'i-set not correctly found by ramsey!'
```

### Step 7: Assign graph = nx.barbell_graph(...)

```python
graph = nx.barbell_graph(10, 5, nx.Graph())
```

**Verification:**
```python
assert cc == c
```

### Step 8: Assign unknown = apxa.ramsey_R2(...)

```python
c, i = apxa.ramsey_R2(graph)
```

**Verification:**
```python
assert ii == i
```

### Step 9: Assign cdens = nx.density(...)

```python
cdens = nx.density(graph.subgraph(c))
```

**Verification:**
```python
assert cdens == 1.0, 'clique not correctly found by ramsey!'
```

### Step 10: Assign idens = nx.density(...)

```python
idens = nx.density(graph.subgraph(i))
```

**Verification:**
```python
assert idens == 0.0, 'i-set not correctly found by ramsey!'
```

### Step 11: Call graph.add_edges_from()

```python
graph.add_edges_from([(n, n) for n in range(0, len(graph), 2)])
```

### Step 12: Assign unknown = apxa.ramsey_R2(...)

```python
cc, ii = apxa.ramsey_R2(graph)
```

**Verification:**
```python
assert cc == c
```


## Complete Example

```python
# Workflow
graph = nx.complete_graph(10)
c, i = apxa.ramsey_R2(graph)
cdens = nx.density(graph.subgraph(c))
assert cdens == 1.0, 'clique not correctly found by ramsey!'
idens = nx.density(graph.subgraph(i))
assert idens == 0.0, 'i-set not correctly found by ramsey!'
graph = nx.trivial_graph()
c, i = apxa.ramsey_R2(graph)
assert c == {0}, 'clique not correctly found by ramsey!'
assert i == {0}, 'i-set not correctly found by ramsey!'
graph = nx.barbell_graph(10, 5, nx.Graph())
c, i = apxa.ramsey_R2(graph)
cdens = nx.density(graph.subgraph(c))
assert cdens == 1.0, 'clique not correctly found by ramsey!'
idens = nx.density(graph.subgraph(i))
assert idens == 0.0, 'i-set not correctly found by ramsey!'
graph.add_edges_from([(n, n) for n in range(0, len(graph), 2)])
cc, ii = apxa.ramsey_R2(graph)
assert cc == c
assert ii == i
```

## Next Steps


---

*Source: test_ramsey.py:5 | Complexity: Advanced | Last updated: 2026-06-02*
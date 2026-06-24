# How To: Contract Loop Graph

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Tests for node contraction when nodes have loops.

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: 'Tests for node contraction when nodes have loops.'

```python
'Tests for node contraction when nodes have loops.'
```

**Verification:**
```python
assert edges_equal(actual.edges, expected.edges)
```

### Step 2: Assign G = nx.cycle_graph(...)

```python
G = nx.cycle_graph(4)
```

**Verification:**
```python
assert edges_equal(actual.edges, expected.edges)
```

### Step 3: Call G.add_edge()

```python
G.add_edge(0, 0)
```

### Step 4: Assign actual = nx.contracted_nodes(...)

```python
actual = nx.contracted_nodes(G, 0, 1)
```

### Step 5: Assign expected = nx.complete_graph(...)

```python
expected = nx.complete_graph([0, 2, 3])
```

### Step 6: Call expected.add_edge()

```python
expected.add_edge(0, 0)
```

**Verification:**
```python
assert edges_equal(actual.edges, expected.edges)
```

### Step 7: Assign actual = nx.contracted_nodes(...)

```python
actual = nx.contracted_nodes(G, 1, 0)
```

### Step 8: Assign expected = nx.complete_graph(...)

```python
expected = nx.complete_graph([1, 2, 3])
```

### Step 9: Call expected.add_edge()

```python
expected.add_edge(1, 1)
```

**Verification:**
```python
assert edges_equal(actual.edges, expected.edges)
```


## Complete Example

```python
# Workflow
'Tests for node contraction when nodes have loops.'
G = nx.cycle_graph(4)
G.add_edge(0, 0)
actual = nx.contracted_nodes(G, 0, 1)
expected = nx.complete_graph([0, 2, 3])
expected.add_edge(0, 0)
assert edges_equal(actual.edges, expected.edges)
actual = nx.contracted_nodes(G, 1, 0)
expected = nx.complete_graph([1, 2, 3])
expected.add_edge(1, 1)
assert edges_equal(actual.edges, expected.edges)
```

## Next Steps


---

*Source: test_contraction.py:466 | Complexity: Advanced | Last updated: 2026-06-02*
# How To: Directed Class

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test directed class

## Prerequisites

**Required Modules:**
- `gc`
- `pickle`
- `platform`
- `weakref`
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign G = self.Graph(...)

```python
G = self.Graph()
```

**Verification:**
```python
assert isinstance(H, newDiGraph)
```

### Step 2: Assign G = value

```python
G = newDiGraph() if G.is_directed() else newGraph()
```

**Verification:**
```python
assert isinstance(H, newGraph)
```

### Step 3: Assign H = G.to_directed(...)

```python
H = G.to_directed()
```

**Verification:**
```python
assert isinstance(H, newDiGraph)
```

### Step 4: Assign H = G.to_undirected(...)

```python
H = G.to_undirected()
```

**Verification:**
```python
assert isinstance(H, newGraph)
```


## Complete Example

```python
# Workflow
G = self.Graph()

class newGraph(G.to_undirected_class()):

    def to_directed_class(self):
        return newDiGraph

    def to_undirected_class(self):
        return newGraph

class newDiGraph(G.to_directed_class()):

    def to_directed_class(self):
        return newDiGraph

    def to_undirected_class(self):
        return newGraph
G = newDiGraph() if G.is_directed() else newGraph()
H = G.to_directed()
assert isinstance(H, newDiGraph)
H = G.to_undirected()
assert isinstance(H, newGraph)
```

## Next Steps


---

*Source: test_graph.py:533 | Complexity: Intermediate | Last updated: 2026-06-02*
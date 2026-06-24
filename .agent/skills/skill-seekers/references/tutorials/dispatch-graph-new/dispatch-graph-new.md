# How To: Dispatch Graph New

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, mock, workflow, integration

## Overview

Workflow: test dispatch graph new

## Prerequisites

**Required Modules:**
- `pickle`
- `pytest`
- `networkx`
- `networkx.classes.tests.dispatch_interface`
- `networkx.classes.tests.dispatch_interface`
- `networkx.classes.tests`
- `networkx.classes.tests.dispatch_interface`
- `networkx.classes.tests.dispatch_interface`


## Step-by-Step Guide

### Step 1: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

**Verification:**
```python
assert not isinstance(G, LoopbackGraph)
```

### Step 2: Assign G = nx.Graph(...)

```python
G = nx.Graph(backend='networkx')
```

**Verification:**
```python
assert type(G) is nx.Graph
```

### Step 3: Assign G = nx.Graph(...)

```python
G = nx.Graph(backend='nx_loopback')
```

**Verification:**
```python
assert 'backend' not in G.graph
```

### Step 4: Assign G1 = nx.Graph(...)

```python
G1 = nx.Graph([(0, 1), (1, 2)])
```

**Verification:**
```python
assert isinstance(G, LoopbackGraph)
```

### Step 5: Assign G2 = nx.Graph(...)

```python
G2 = nx.Graph([(0, 1), (1, 2)], backend='nx_loopback')
```

**Verification:**
```python
assert 'backend' not in G.graph
```

### Step 6: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

**Verification:**
```python
assert not isinstance(G1, LoopbackGraph)
```

### Step 7: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

**Verification:**
```python
assert isinstance(G2, LoopbackGraph)
```

### Step 8: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

**Verification:**
```python
assert nx.utils.misc.graphs_equal(G1, G2)
```


## Complete Example

```python
# Workflow
from networkx.classes.tests.dispatch_interface import LoopbackGraph
G = nx.Graph()
assert not isinstance(G, LoopbackGraph)
G = nx.Graph(backend='networkx')
assert type(G) is nx.Graph
assert 'backend' not in G.graph
G = nx.Graph(backend='nx_loopback')
assert isinstance(G, LoopbackGraph)
assert 'backend' not in G.graph
G1 = nx.Graph([(0, 1), (1, 2)])
assert not isinstance(G1, LoopbackGraph)
G2 = nx.Graph([(0, 1), (1, 2)], backend='nx_loopback')
assert isinstance(G2, LoopbackGraph)
assert nx.utils.misc.graphs_equal(G1, G2)
with nx.config.backend_priority(classes=['nx_loopback']):
    G = nx.Graph()
    assert isinstance(G, LoopbackGraph)
    G = nx.DiGraph()
    assert not isinstance(G, LoopbackGraph)
G = nx.Graph()
assert not isinstance(G, LoopbackGraph)
```

## Next Steps


---

*Source: test_backends.py:194 | Complexity: Advanced | Last updated: 2026-06-02*
# How To: Zero Deg

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test zero deg

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

**Verification:**
```python
assert c == {1: 0, 3: 1}
```

### Step 2: Call G.add_edge()

```python
G.add_edge(1, 2)
```

**Verification:**
```python
assert c == {0: 0, 1: 0}
```

### Step 3: Call G.add_edge()

```python
G.add_edge(1, 3)
```

**Verification:**
```python
assert c == {0: 0, 1: 3}
```

### Step 4: Call G.add_edge()

```python
G.add_edge(1, 4)
```

**Verification:**
```python
assert c == {0: 0, 1: 3}
```

### Step 5: Assign c = nx.average_degree_connectivity(...)

```python
c = nx.average_degree_connectivity(G)
```

**Verification:**
```python
assert c == {0: 0, 3: 0}
```

### Step 6: Assign c = nx.average_degree_connectivity(...)

```python
c = nx.average_degree_connectivity(G, source='in', target='in')
```

**Verification:**
```python
assert c == {0: 0, 3: 1}
```

### Step 7: Assign c = nx.average_degree_connectivity(...)

```python
c = nx.average_degree_connectivity(G, source='in', target='out')
```

**Verification:**
```python
assert c == {0: 0, 3: 1}
```

### Step 8: Assign c = nx.average_degree_connectivity(...)

```python
c = nx.average_degree_connectivity(G, source='in', target='in+out')
```

**Verification:**
```python
assert c == {0: 0, 1: 3}
```

### Step 9: Assign c = nx.average_degree_connectivity(...)

```python
c = nx.average_degree_connectivity(G, source='out', target='out')
```

**Verification:**
```python
assert c == {0: 0, 3: 0}
```

### Step 10: Assign c = nx.average_degree_connectivity(...)

```python
c = nx.average_degree_connectivity(G, source='out', target='in')
```

**Verification:**
```python
assert c == {0: 0, 3: 1}
```

### Step 11: Assign c = nx.average_degree_connectivity(...)

```python
c = nx.average_degree_connectivity(G, source='out', target='in+out')
```

**Verification:**
```python
assert c == {0: 0, 3: 1}
```


## Complete Example

```python
# Workflow
G = nx.DiGraph()
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(1, 4)
c = nx.average_degree_connectivity(G)
assert c == {1: 0, 3: 1}
c = nx.average_degree_connectivity(G, source='in', target='in')
assert c == {0: 0, 1: 0}
c = nx.average_degree_connectivity(G, source='in', target='out')
assert c == {0: 0, 1: 3}
c = nx.average_degree_connectivity(G, source='in', target='in+out')
assert c == {0: 0, 1: 3}
c = nx.average_degree_connectivity(G, source='out', target='out')
assert c == {0: 0, 3: 0}
c = nx.average_degree_connectivity(G, source='out', target='in')
assert c == {0: 0, 3: 1}
c = nx.average_degree_connectivity(G, source='out', target='in+out')
assert c == {0: 0, 3: 1}
```

## Next Steps


---

*Source: test_connectivity.py:90 | Complexity: Advanced | Last updated: 2026-06-02*
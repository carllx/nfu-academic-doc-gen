# How To: Eccentricity

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test eccentricity

## Prerequisites

**Required Modules:**
- `itertools`
- `math`
- `random`
- `pytest`
- `networkx`
- `networkx`
- `networkx.algorithms.distance_measures`


## Step-by-Step Guide

### Step 1: Assign e = nx.eccentricity(...)

```python
e = nx.eccentricity(self.G)
```

**Verification:**
```python
assert nx.eccentricity(self.G, 1) == 6
```

### Step 2: Assign sp = dict(...)

```python
sp = dict(nx.shortest_path_length(self.G))
```

**Verification:**
```python
assert e[1] == 6
```

### Step 3: Assign e = nx.eccentricity(...)

```python
e = nx.eccentricity(self.G, sp=sp)
```

**Verification:**
```python
assert e[1] == 6
```

### Step 4: Assign e = nx.eccentricity(...)

```python
e = nx.eccentricity(self.G, v=1)
```

**Verification:**
```python
assert e == 6
```

### Step 5: Assign e = nx.eccentricity(...)

```python
e = nx.eccentricity(self.G, v=[1, 1])
```

**Verification:**
```python
assert e[1] == 6
```

### Step 6: Assign e = nx.eccentricity(...)

```python
e = nx.eccentricity(self.G, v=[1, 2])
```

**Verification:**
```python
assert e[1] == 6
```

### Step 7: Assign G = nx.path_graph(...)

```python
G = nx.path_graph(1)
```

**Verification:**
```python
assert e[0] == 0
```

### Step 8: Assign e = nx.eccentricity(...)

```python
e = nx.eccentricity(G)
```

**Verification:**
```python
assert e == 0
```

### Step 9: Assign e = nx.eccentricity(...)

```python
e = nx.eccentricity(G, v=0)
```

**Verification:**
```python
assert e == {}
```

### Step 10: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, nx.eccentricity, G, 1)
```

### Step 11: Assign G = nx.empty_graph(...)

```python
G = nx.empty_graph()
```

### Step 12: Assign e = nx.eccentricity(...)

```python
e = nx.eccentricity(G)
```

**Verification:**
```python
assert e == {}
```


## Complete Example

```python
# Workflow
assert nx.eccentricity(self.G, 1) == 6
e = nx.eccentricity(self.G)
assert e[1] == 6
sp = dict(nx.shortest_path_length(self.G))
e = nx.eccentricity(self.G, sp=sp)
assert e[1] == 6
e = nx.eccentricity(self.G, v=1)
assert e == 6
e = nx.eccentricity(self.G, v=[1, 1])
assert e[1] == 6
e = nx.eccentricity(self.G, v=[1, 2])
assert e[1] == 6
G = nx.path_graph(1)
e = nx.eccentricity(G)
assert e[0] == 0
e = nx.eccentricity(G, v=0)
assert e == 0
pytest.raises(nx.NetworkXError, nx.eccentricity, G, 1)
G = nx.empty_graph()
e = nx.eccentricity(G)
assert e == {}
```

## Next Steps


---

*Source: test_distance_measures.py:51 | Complexity: Advanced | Last updated: 2026-06-02*
# How To: Predecessor Target

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test predecessor target

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = nx.path_graph(...)

```python
G = nx.path_graph(4)
```

**Verification:**
```python
assert p == [2]
```

### Step 2: Assign p = nx.predecessor(...)

```python
p = nx.predecessor(G, 0, 3)
```

**Verification:**
```python
assert p == []
```

### Step 3: Assign p = nx.predecessor(...)

```python
p = nx.predecessor(G, 0, 3, cutoff=2)
```

**Verification:**
```python
assert p == [2]
```

### Step 4: Assign unknown = nx.predecessor(...)

```python
p, s = nx.predecessor(G, 0, 3, return_seen=True)
```

**Verification:**
```python
assert s == 3
```

### Step 5: Assign unknown = nx.predecessor(...)

```python
p, s = nx.predecessor(G, 0, 3, cutoff=2, return_seen=True)
```

**Verification:**
```python
assert p == []
```


## Complete Example

```python
# Workflow
G = nx.path_graph(4)
p = nx.predecessor(G, 0, 3)
assert p == [2]
p = nx.predecessor(G, 0, 3, cutoff=2)
assert p == []
p, s = nx.predecessor(G, 0, 3, return_seen=True)
assert p == [2]
assert s == 3
p, s = nx.predecessor(G, 0, 3, cutoff=2, return_seen=True)
assert p == []
assert s == -1
```

## Next Steps


---

*Source: test_unweighted.py:133 | Complexity: Intermediate | Last updated: 2026-06-02*
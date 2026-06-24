# How To: Rich Club Leq 3 Nodes Unnormalized

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test rich club leq 3 nodes unnormalized

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

**Verification:**
```python
assert rc == {}
```

### Step 2: Assign rc = nx.rich_club_coefficient(...)

```python
rc = nx.rich_club_coefficient(G, normalized=False)
```

**Verification:**
```python
assert rc == {}
```

### Step 3: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

**Verification:**
```python
assert rc == {0: 1}
```

### Step 4: Call G.add_edge()

```python
G.add_edge(0, 1)
```

**Verification:**
```python
assert rc == {0: 1}
```

### Step 5: Assign rc = nx.rich_club_coefficient(...)

```python
rc = nx.rich_club_coefficient(G, normalized=False)
```

**Verification:**
```python
assert rc == {0: 2 / 3}
```

### Step 6: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

**Verification:**
```python
assert rc == {0: 1, 1: 1}
```

### Step 7: Call G.add_nodes_from()

```python
G.add_nodes_from([0, 1, 2])
```

### Step 8: Call G.add_edge()

```python
G.add_edge(0, 1)
```

### Step 9: Assign rc = nx.rich_club_coefficient(...)

```python
rc = nx.rich_club_coefficient(G, normalized=False)
```

**Verification:**
```python
assert rc == {0: 1}
```

### Step 10: Call G.add_edge()

```python
G.add_edge(1, 2)
```

### Step 11: Assign rc = nx.rich_club_coefficient(...)

```python
rc = nx.rich_club_coefficient(G, normalized=False)
```

**Verification:**
```python
assert rc == {0: 2 / 3}
```

### Step 12: Call G.add_edge()

```python
G.add_edge(0, 2)
```

### Step 13: Assign rc = nx.rich_club_coefficient(...)

```python
rc = nx.rich_club_coefficient(G, normalized=False)
```

**Verification:**
```python
assert rc == {0: 1, 1: 1}
```

### Step 14: Call G.add_node()

```python
G.add_node(i)
```

### Step 15: Assign rc = nx.rich_club_coefficient(...)

```python
rc = nx.rich_club_coefficient(G, normalized=False)
```

**Verification:**
```python
assert rc == {}
```


## Complete Example

```python
# Workflow
G = nx.Graph()
rc = nx.rich_club_coefficient(G, normalized=False)
assert rc == {}
for i in range(3):
    G.add_node(i)
    rc = nx.rich_club_coefficient(G, normalized=False)
    assert rc == {}
G = nx.Graph()
G.add_edge(0, 1)
rc = nx.rich_club_coefficient(G, normalized=False)
assert rc == {0: 1}
G = nx.Graph()
G.add_nodes_from([0, 1, 2])
G.add_edge(0, 1)
rc = nx.rich_club_coefficient(G, normalized=False)
assert rc == {0: 1}
G.add_edge(1, 2)
rc = nx.rich_club_coefficient(G, normalized=False)
assert rc == {0: 2 / 3}
G.add_edge(0, 2)
rc = nx.rich_club_coefficient(G, normalized=False)
assert rc == {0: 1, 1: 1}
```

## Next Steps


---

*Source: test_richclub.py:94 | Complexity: Advanced | Last updated: 2026-06-02*
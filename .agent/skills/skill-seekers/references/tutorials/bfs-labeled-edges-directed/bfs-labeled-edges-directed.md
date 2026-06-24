# How To: Bfs Labeled Edges Directed

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test bfs labeled edges directed

## Prerequisites

**Required Modules:**
- `functools`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign D = nx.cycle_graph(...)

```python
D = nx.cycle_graph(5, create_using=nx.DiGraph)
```

**Verification:**
```python
assert expected == answer
```

### Step 2: Assign expected = value

```python
expected = [(0, 1, 'tree'), (1, 2, 'tree'), (2, 3, 'tree'), (3, 4, 'tree'), (4, 0, 'reverse')]
```

**Verification:**
```python
assert expected == answer
```

### Step 3: Assign answer = list(...)

```python
answer = list(nx.bfs_labeled_edges(D, 0))
```

**Verification:**
```python
assert expected == answer
```

### Step 4: Call D.add_edge()

```python
D.add_edge(4, 4)
```

**Verification:**
```python
assert expected == answer
```

### Step 5: Call expected.append()

```python
expected.append((4, 4, 'level'))
```

### Step 6: Assign answer = list(...)

```python
answer = list(nx.bfs_labeled_edges(D, 0))
```

**Verification:**
```python
assert expected == answer
```

### Step 7: Call D.add_edge()

```python
D.add_edge(0, 2)
```

### Step 8: Call D.add_edge()

```python
D.add_edge(1, 5)
```

### Step 9: Call D.add_edge()

```python
D.add_edge(2, 5)
```

### Step 10: Call D.remove_edge()

```python
D.remove_edge(4, 4)
```

### Step 11: Assign expected = value

```python
expected = [(0, 1, 'tree'), (0, 2, 'tree'), (1, 2, 'level'), (1, 5, 'tree'), (2, 3, 'tree'), (2, 5, 'forward'), (3, 4, 'tree'), (4, 0, 'reverse')]
```

### Step 12: Assign answer = list(...)

```python
answer = list(nx.bfs_labeled_edges(D, 0))
```

**Verification:**
```python
assert expected == answer
```

### Step 13: Assign G = D.to_undirected(...)

```python
G = D.to_undirected()
```

### Step 14: Call G.add_edge()

```python
G.add_edge(4, 4)
```

### Step 15: Assign expected = value

```python
expected = [(0, 1, 'tree'), (0, 2, 'tree'), (0, 4, 'tree'), (1, 2, 'level'), (1, 5, 'tree'), (2, 3, 'tree'), (2, 5, 'forward'), (4, 3, 'forward'), (4, 4, 'level')]
```

### Step 16: Assign answer = list(...)

```python
answer = list(nx.bfs_labeled_edges(G, 0))
```

**Verification:**
```python
assert expected == answer
```


## Complete Example

```python
# Workflow
D = nx.cycle_graph(5, create_using=nx.DiGraph)
expected = [(0, 1, 'tree'), (1, 2, 'tree'), (2, 3, 'tree'), (3, 4, 'tree'), (4, 0, 'reverse')]
answer = list(nx.bfs_labeled_edges(D, 0))
assert expected == answer
D.add_edge(4, 4)
expected.append((4, 4, 'level'))
answer = list(nx.bfs_labeled_edges(D, 0))
assert expected == answer
D.add_edge(0, 2)
D.add_edge(1, 5)
D.add_edge(2, 5)
D.remove_edge(4, 4)
expected = [(0, 1, 'tree'), (0, 2, 'tree'), (1, 2, 'level'), (1, 5, 'tree'), (2, 3, 'tree'), (2, 5, 'forward'), (3, 4, 'tree'), (4, 0, 'reverse')]
answer = list(nx.bfs_labeled_edges(D, 0))
assert expected == answer
G = D.to_undirected()
G.add_edge(4, 4)
expected = [(0, 1, 'tree'), (0, 2, 'tree'), (0, 4, 'tree'), (1, 2, 'level'), (1, 5, 'tree'), (2, 3, 'tree'), (2, 5, 'forward'), (4, 3, 'forward'), (4, 4, 'level')]
answer = list(nx.bfs_labeled_edges(G, 0))
assert expected == answer
```

## Next Steps


---

*Source: test_bfs.py:78 | Complexity: Advanced | Last updated: 2026-06-02*
# How To: Hardcoded

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test hardcoded

## Prerequisites

**Required Modules:**
- `random`
- `time`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign edges_1 = value

```python
edges_1 = [('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'e'), ('b', 'f'), ('e', 'j'), ('e', 'k'), ('c', 'g'), ('c', 'h'), ('g', 'm'), ('d', 'i'), ('f', 'l')]
```

**Verification:**
```python
assert isomorphism in (isomorphism1, isomorphism2)
```

### Step 2: Assign edges_2 = value

```python
edges_2 = [('v', 'y'), ('v', 'z'), ('u', 'x'), ('q', 'u'), ('q', 'v'), ('p', 't'), ('n', 'p'), ('n', 'q'), ('n', 'o'), ('o', 'r'), ('o', 's'), ('s', 'w')]
```

**Verification:**
```python
assert _check_isomorphism(t1, t2, isomorphism)
```

### Step 3: Assign isomorphism1 = value

```python
isomorphism1 = [('a', 'n'), ('b', 'q'), ('c', 'o'), ('d', 'p'), ('e', 'v'), ('f', 'u'), ('g', 's'), ('h', 'r'), ('i', 't'), ('j', 'y'), ('k', 'z'), ('l', 'x'), ('m', 'w')]
```

**Verification:**
```python
assert isomorphism in (isomorphism1, isomorphism2)
```

### Step 4: Assign isomorphism2 = value

```python
isomorphism2 = [('a', 'n'), ('b', 'q'), ('c', 'o'), ('d', 'p'), ('e', 'v'), ('f', 'u'), ('g', 's'), ('h', 'r'), ('i', 't'), ('j', 'z'), ('k', 'y'), ('l', 'x'), ('m', 'w')]
```

**Verification:**
```python
assert _check_isomorphism(t1, t2, isomorphism)
```

### Step 5: Assign t1 = nx.Graph(...)

```python
t1 = nx.Graph()
```

### Step 6: Call t1.add_edges_from()

```python
t1.add_edges_from(edges_1)
```

### Step 7: Assign root1 = 'a'

```python
root1 = 'a'
```

### Step 8: Assign t2 = nx.Graph(...)

```python
t2 = nx.Graph()
```

### Step 9: Call t2.add_edges_from()

```python
t2.add_edges_from(edges_2)
```

### Step 10: Assign root2 = 'n'

```python
root2 = 'n'
```

### Step 11: Assign isomorphism = sorted(...)

```python
isomorphism = sorted(nx.isomorphism.rooted_tree_isomorphism(t1, root1, t2, root2))
```

**Verification:**
```python
assert isomorphism in (isomorphism1, isomorphism2)
```

### Step 12: Assign t1 = nx.DiGraph(...)

```python
t1 = nx.DiGraph()
```

### Step 13: Call t1.add_edges_from()

```python
t1.add_edges_from(edges_1)
```

### Step 14: Assign root1 = 'a'

```python
root1 = 'a'
```

### Step 15: Assign t2 = nx.DiGraph(...)

```python
t2 = nx.DiGraph()
```

### Step 16: Call t2.add_edges_from()

```python
t2.add_edges_from(edges_2)
```

### Step 17: Assign root2 = 'n'

```python
root2 = 'n'
```

### Step 18: Assign isomorphism = sorted(...)

```python
isomorphism = sorted(nx.isomorphism.rooted_tree_isomorphism(t1, root1, t2, root2))
```

**Verification:**
```python
assert isomorphism in (isomorphism1, isomorphism2)
```


## Complete Example

```python
# Workflow
edges_1 = [('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'e'), ('b', 'f'), ('e', 'j'), ('e', 'k'), ('c', 'g'), ('c', 'h'), ('g', 'm'), ('d', 'i'), ('f', 'l')]
edges_2 = [('v', 'y'), ('v', 'z'), ('u', 'x'), ('q', 'u'), ('q', 'v'), ('p', 't'), ('n', 'p'), ('n', 'q'), ('n', 'o'), ('o', 'r'), ('o', 's'), ('s', 'w')]
isomorphism1 = [('a', 'n'), ('b', 'q'), ('c', 'o'), ('d', 'p'), ('e', 'v'), ('f', 'u'), ('g', 's'), ('h', 'r'), ('i', 't'), ('j', 'y'), ('k', 'z'), ('l', 'x'), ('m', 'w')]
isomorphism2 = [('a', 'n'), ('b', 'q'), ('c', 'o'), ('d', 'p'), ('e', 'v'), ('f', 'u'), ('g', 's'), ('h', 'r'), ('i', 't'), ('j', 'z'), ('k', 'y'), ('l', 'x'), ('m', 'w')]
t1 = nx.Graph()
t1.add_edges_from(edges_1)
root1 = 'a'
t2 = nx.Graph()
t2.add_edges_from(edges_2)
root2 = 'n'
isomorphism = sorted(nx.isomorphism.rooted_tree_isomorphism(t1, root1, t2, root2))
assert isomorphism in (isomorphism1, isomorphism2)
assert _check_isomorphism(t1, t2, isomorphism)
t1 = nx.DiGraph()
t1.add_edges_from(edges_1)
root1 = 'a'
t2 = nx.DiGraph()
t2.add_edges_from(edges_2)
root2 = 'n'
isomorphism = sorted(nx.isomorphism.rooted_tree_isomorphism(t1, root1, t2, root2))
assert isomorphism in (isomorphism1, isomorphism2)
assert _check_isomorphism(t1, t2, isomorphism)
```

## Next Steps


---

*Source: test_tree_isomorphism.py:41 | Complexity: Advanced | Last updated: 2026-06-02*
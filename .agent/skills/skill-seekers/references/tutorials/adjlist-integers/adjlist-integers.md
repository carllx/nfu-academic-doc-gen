# How To: Adjlist Integers

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test adjlist integers

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `pytest`
- `networkx`
- `networkx.utils`

**Setup Required:**
```python
# Fixtures: tmp_path
```

## Step-by-Step Guide

### Step 1: Assign fname = value

```python
fname = tmp_path / 'adjlist.txt'
```

**Verification:**
```python
assert H is not H2
```

### Step 2: Assign G = nx.convert_node_labels_to_integers(...)

```python
G = nx.convert_node_labels_to_integers(self.G)
```

**Verification:**
```python
assert nodes_equal(list(H), list(G))
```

### Step 3: Call nx.write_adjlist()

```python
nx.write_adjlist(G, fname)
```

**Verification:**
```python
assert edges_equal(list(H.edges()), list(G.edges()))
```

### Step 4: Assign H = nx.read_adjlist(...)

```python
H = nx.read_adjlist(fname, nodetype=int)
```

### Step 5: Assign H2 = nx.read_adjlist(...)

```python
H2 = nx.read_adjlist(fname, nodetype=int)
```

**Verification:**
```python
assert H is not H2
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
fname = tmp_path / 'adjlist.txt'
G = nx.convert_node_labels_to_integers(self.G)
nx.write_adjlist(G, fname)
H = nx.read_adjlist(fname, nodetype=int)
H2 = nx.read_adjlist(fname, nodetype=int)
assert H is not H2
assert nodes_equal(list(H), list(G))
assert edges_equal(list(H.edges()), list(G.edges()))
```

## Next Steps


---

*Source: test_adjlist.py:189 | Complexity: Intermediate | Last updated: 2026-06-02*
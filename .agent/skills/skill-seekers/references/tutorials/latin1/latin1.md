# How To: Latin1

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test latin1

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

### Step 1: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

**Verification:**
```python
assert graphs_equal(G, H)
```

### Step 2: Assign name1 = value

```python
name1 = 'Bj' + chr(246) + 'rk'
```

### Step 3: Assign name2 = value

```python
name2 = chr(220) + 'ber'
```

### Step 4: Call G.add_edge()

```python
G.add_edge(name1, 'Radiohead', **{name2: 3})
```

### Step 5: Assign fname = value

```python
fname = tmp_path / 'adjlist.txt'
```

### Step 6: Call nx.write_multiline_adjlist()

```python
nx.write_multiline_adjlist(G, fname, encoding='latin-1')
```

### Step 7: Assign H = nx.read_multiline_adjlist(...)

```python
H = nx.read_multiline_adjlist(fname, encoding='latin-1')
```

**Verification:**
```python
assert graphs_equal(G, H)
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
G = nx.Graph()
name1 = 'Bj' + chr(246) + 'rk'
name2 = chr(220) + 'ber'
G.add_edge(name1, 'Radiohead', **{name2: 3})
fname = tmp_path / 'adjlist.txt'
nx.write_multiline_adjlist(G, fname, encoding='latin-1')
H = nx.read_multiline_adjlist(fname, encoding='latin-1')
assert graphs_equal(G, H)
```

## Next Steps


---

*Source: test_adjlist.py:150 | Complexity: Intermediate | Last updated: 2026-06-02*
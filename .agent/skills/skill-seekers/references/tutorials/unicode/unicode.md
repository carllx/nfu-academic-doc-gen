# How To: Unicode

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test unicode

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
name1 = chr(2344) + chr(123) + chr(6543)
```

### Step 3: Assign name2 = value

```python
name2 = chr(5543) + chr(1543) + chr(324)
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
nx.write_multiline_adjlist(G, fname)
```

### Step 7: Assign H = nx.read_multiline_adjlist(...)

```python
H = nx.read_multiline_adjlist(fname)
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
name1 = chr(2344) + chr(123) + chr(6543)
name2 = chr(5543) + chr(1543) + chr(324)
G.add_edge(name1, 'Radiohead', **{name2: 3})
fname = tmp_path / 'adjlist.txt'
nx.write_multiline_adjlist(G, fname)
H = nx.read_multiline_adjlist(fname)
assert graphs_equal(G, H)
```

## Next Steps


---

*Source: test_adjlist.py:130 | Complexity: Intermediate | Last updated: 2026-06-02*
# How To: Pydot Issue 7581

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Validate that `nx_pydot.pydot_layout` handles nodes
    with characters like "
", " ".

    Those characters cause `pydot` to escape and quote them on output,
    which caused #7581.
    

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

### Step 1: 'Validate that `nx_pydot.pydot_layout` handles nodes\n    with characters like "\n", " ".\n\n    Those characters cause `pydot` to escape and quote them on output,\n    which caused #7581.\n    '

```python
'Validate that `nx_pydot.pydot_layout` handles nodes\n    with characters like "\n", " ".\n\n    Those characters cause `pydot` to escape and quote them on output,\n    which caused #7581.\n    '
```

**Verification:**
```python
assert isinstance(graph_layout, dict)
```

### Step 2: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

**Verification:**
```python
assert graphs_equal(G, G2)
```

### Step 3: Call G.add_edges_from()

```python
G.add_edges_from([('A\nbig test', 'B'), ('A\nbig test', 'C'), ('B', 'C')])
```

### Step 4: Assign graph_layout = nx.nx_pydot.pydot_layout(...)

```python
graph_layout = nx.nx_pydot.pydot_layout(G, prog='dot')
```

**Verification:**
```python
assert isinstance(graph_layout, dict)
```

### Step 5: Assign P = nx.nx_pydot.to_pydot(...)

```python
P = nx.nx_pydot.to_pydot(G)
```

### Step 6: Assign G2 = nx.Graph(...)

```python
G2 = nx.Graph(nx.nx_pydot.from_pydot(P))
```

**Verification:**
```python
assert graphs_equal(G, G2)
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
'Validate that `nx_pydot.pydot_layout` handles nodes\n    with characters like "\n", " ".\n\n    Those characters cause `pydot` to escape and quote them on output,\n    which caused #7581.\n    '
G = nx.Graph()
G.add_edges_from([('A\nbig test', 'B'), ('A\nbig test', 'C'), ('B', 'C')])
graph_layout = nx.nx_pydot.pydot_layout(G, prog='dot')
assert isinstance(graph_layout, dict)
P = nx.nx_pydot.to_pydot(G)
G2 = nx.Graph(nx.nx_pydot.from_pydot(P))
assert graphs_equal(G, G2)
```

## Next Steps


---

*Source: test_pydot.py:93 | Complexity: Intermediate | Last updated: 2026-06-02*
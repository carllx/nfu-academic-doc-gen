# How To: Read Write

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test read write

## Prerequisites

**Required Modules:**
- `io`
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign G = nx.MultiGraph(...)

```python
G = nx.MultiGraph()
```

**Verification:**
```python
assert graphs_equal(G, H)
```

### Step 2: Assign unknown = 'G'

```python
G.graph['name'] = 'G'
```

### Step 3: Call G.add_edge()

```python
G.add_edge('1', '2', key='0')
```

### Step 4: Assign fh = StringIO(...)

```python
fh = StringIO()
```

### Step 5: Call nx.nx_pydot.write_dot()

```python
nx.nx_pydot.write_dot(G, fh)
```

### Step 6: Call fh.seek()

```python
fh.seek(0)
```

### Step 7: Assign H = nx.nx_pydot.read_dot(...)

```python
H = nx.nx_pydot.read_dot(fh)
```

**Verification:**
```python
assert graphs_equal(G, H)
```


## Complete Example

```python
# Workflow
G = nx.MultiGraph()
G.graph['name'] = 'G'
G.add_edge('1', '2', key='0')
fh = StringIO()
nx.nx_pydot.write_dot(G, fh)
fh.seek(0)
H = nx.nx_pydot.read_dot(fh)
assert graphs_equal(G, H)
```

## Next Steps


---

*Source: test_pydot.py:82 | Complexity: Intermediate | Last updated: 2026-06-02*
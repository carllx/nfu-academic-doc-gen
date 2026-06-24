# How To: View Pygraphviz Path

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test view pygraphviz path

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `warnings`
- `pytest`
- `networkx`
- `networkx.utils`

**Setup Required:**
```python
# Fixtures: tmp_path
```

## Step-by-Step Guide

### Step 1: Assign G = nx.complete_graph(...)

```python
G = nx.complete_graph(3)
```

**Verification:**
```python
assert out_path == input_path
```

### Step 2: Assign input_path = str(...)

```python
input_path = str(tmp_path / 'graph.png')
```

**Verification:**
```python
assert len(data) > 0
```

### Step 3: Assign unknown = nx.nx_agraph.view_pygraphviz(...)

```python
out_path, A = nx.nx_agraph.view_pygraphviz(G, path=input_path, show=False)
```

**Verification:**
```python
assert out_path == input_path
```

### Step 4: Assign data = fh.read(...)

```python
data = fh.read()
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
G = nx.complete_graph(3)
input_path = str(tmp_path / 'graph.png')
out_path, A = nx.nx_agraph.view_pygraphviz(G, path=input_path, show=False)
assert out_path == input_path
with open(input_path, 'rb') as fh:
    data = fh.read()
assert len(data) > 0
```

## Next Steps


---

*Source: test_agraph.py:89 | Complexity: Intermediate | Last updated: 2026-06-02*
# How To: Pygraphviz Layout Root

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test pygraphviz layout root

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `warnings`
- `pytest`
- `networkx`
- `networkx.utils`

**Setup Required:**
```python
# Fixtures: root
```

## Step-by-Step Guide

### Step 1: Assign G = nx.complete_graph(...)

```python
G = nx.complete_graph(5)
```

**Verification:**
```python
assert pygv_layout[1] == a1_pos
```

### Step 2: Assign A = nx.nx_agraph.to_agraph(...)

```python
A = nx.nx_agraph.to_agraph(G)
```

### Step 3: Assign pygv_layout = nx.nx_agraph.pygraphviz_layout(...)

```python
pygv_layout = nx.nx_agraph.pygraphviz_layout(G, prog='circo', root=root)
```

### Step 4: Call A.layout()

```python
A.layout(args=f'-Groot={root}', prog='circo')
```

### Step 5: Assign a1_pos = tuple(...)

```python
a1_pos = tuple((float(v) for v in dict(A.get_node('1').attr)['pos'].split(',')))
```

**Verification:**
```python
assert pygv_layout[1] == a1_pos
```


## Complete Example

```python
# Setup
# Fixtures: root

# Workflow
G = nx.complete_graph(5)
A = nx.nx_agraph.to_agraph(G)
pygv_layout = nx.nx_agraph.pygraphviz_layout(G, prog='circo', root=root)
A.layout(args=f'-Groot={root}', prog='circo')
a1_pos = tuple((float(v) for v in dict(A.get_node('1').attr)['pos'].split(',')))
assert pygv_layout[1] == a1_pos
```

## Next Steps


---

*Source: test_agraph.py:197 | Complexity: Intermediate | Last updated: 2026-06-02*
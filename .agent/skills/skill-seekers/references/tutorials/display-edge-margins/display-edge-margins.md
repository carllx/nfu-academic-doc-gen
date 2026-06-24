# How To: Display Edge Margins

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, mock, workflow, integration

## Overview

Workflow: Test that there is a wider gap between the node and the start of an
incident edge when min_source_margin is specified.

This test checks that the use os min_{source/target}_margin edge
attributes result is shorter (more padding) between the edges and
source and target nodes.


As a crude visual example, let 's' and 't' represent source and target
nodes, respectively:

   Default:
   s-----------------------------t

   With margins:
   s   -----------------------   t

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `itertools`
- `os`
- `warnings`
- `pytest`
- `networkx`
- `matplotlib.collections`
- `matplotlib.patches`
- `matplotlib.collections`
- `matplotlib.collections`
- `matplotlib.patches`
- `matplotlib.collections`
- `matplotlib.collections`

**Setup Required:**
```python
# Fixtures: node_shape
```

## Step-by-Step Guide

### Step 1: "\n    Test that there is a wider gap between the node and the start of an\n    incident edge when min_source_margin is specified.\n\n    This test checks that the use os min_{source/target}_margin edge\n    attributes result is shorter (more padding) between the edges and\n    source and target nodes.\n\n\n    As a crude visual example, let 's' and 't' represent source and target\n    nodes, respectively:\n\n       Default:\n       s-----------------------------t\n\n       With margins:\n       s   -----------------------   t\n\n    "

```python
"\n    Test that there is a wider gap between the node and the start of an\n    incident edge when min_source_margin is specified.\n\n    This test checks that the use os min_{source/target}_margin edge\n    attributes result is shorter (more padding) between the edges and\n    source and target nodes.\n\n\n    As a crude visual example, let 's' and 't' represent source and target\n    nodes, respectively:\n\n       Default:\n       s-----------------------------t\n\n       With margins:\n       s   -----------------------   t\n\n    "
```

**Verification:**
```python
assert padded_extent[0] > default_extent[0]
```

### Step 2: Assign ax = plt.figure.add_subplot(...)

```python
ax = plt.figure().add_subplot(111)
```

**Verification:**
```python
assert padded_extent[1] < default_extent[1]
```

### Step 3: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph([(0, 1)])
```

### Step 4: Call nx.set_node_attributes()

```python
nx.set_node_attributes(G, {0: (0, 0), 1: (1, 1)}, 'pos')
```

### Step 5: Call nx.display()

```python
nx.display(G, canvas=ax, node_shape=node_shape)
```

### Step 6: Assign default_arrow = value

```python
default_arrow = [f for f in ax.get_children() if isinstance(f, mpl.patches.FancyArrowPatch)][0]
```

### Step 7: Assign default_extent = value

```python
default_extent = default_arrow.get_extents().corners()[::2, 0]
```

### Step 8: Assign ax = plt.figure.add_subplot(...)

```python
ax = plt.figure().add_subplot(111)
```

### Step 9: Call nx.display()

```python
nx.display(G, canvas=ax, edge_source_margin=100, edge_target_margin=100, node_shape=node_shape)
```

### Step 10: Assign padded_arrow = value

```python
padded_arrow = [f for f in ax.get_children() if isinstance(f, mpl.patches.FancyArrowPatch)][0]
```

### Step 11: Assign padded_extent = value

```python
padded_extent = padded_arrow.get_extents().corners()[::2, 0]
```

**Verification:**
```python
assert padded_extent[0] > default_extent[0]
```

### Step 12: Call plt.close()

```python
plt.close()
```


## Complete Example

```python
# Setup
# Fixtures: node_shape

# Workflow
"\n    Test that there is a wider gap between the node and the start of an\n    incident edge when min_source_margin is specified.\n\n    This test checks that the use os min_{source/target}_margin edge\n    attributes result is shorter (more padding) between the edges and\n    source and target nodes.\n\n\n    As a crude visual example, let 's' and 't' represent source and target\n    nodes, respectively:\n\n       Default:\n       s-----------------------------t\n\n       With margins:\n       s   -----------------------   t\n\n    "
ax = plt.figure().add_subplot(111)
G = nx.DiGraph([(0, 1)])
nx.set_node_attributes(G, {0: (0, 0), 1: (1, 1)}, 'pos')
nx.display(G, canvas=ax, node_shape=node_shape)
default_arrow = [f for f in ax.get_children() if isinstance(f, mpl.patches.FancyArrowPatch)][0]
default_extent = default_arrow.get_extents().corners()[::2, 0]
ax = plt.figure().add_subplot(111)
nx.display(G, canvas=ax, edge_source_margin=100, edge_target_margin=100, node_shape=node_shape)
padded_arrow = [f for f in ax.get_children() if isinstance(f, mpl.patches.FancyArrowPatch)][0]
padded_extent = padded_arrow.get_extents().corners()[::2, 0]
assert padded_extent[0] > default_extent[0]
assert padded_extent[1] < default_extent[1]
plt.close()
```

## Next Steps


---

*Source: test_pylab.py:444 | Complexity: Advanced | Last updated: 2026-06-02*
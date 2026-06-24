# How To: Display Edge Width

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, mock, workflow, integration

## Overview

Workflow: test display edge width

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
# Fixtures: param_value, expected, graph_type
```

## Step-by-Step Guide

### Step 1: Assign G = nx.path_graph(...)

```python
G = nx.path_graph(3, create_using=graph_type)
```

**Verification:**
```python
assert widths == expected
```

### Step 2: Call nx.set_edge_attributes()

```python
nx.set_edge_attributes(G, {(0, 1): 5, (1, 2): 10}, 'width')
```

### Step 3: Assign canvas = plt.figure.add_subplot(...)

```python
canvas = plt.figure().add_subplot(111)
```

### Step 4: Call nx.display()

```python
nx.display(G, edge_width=param_value, canvas=canvas)
```

**Verification:**
```python
assert widths == expected
```

### Step 5: Assign widths = value

```python
widths = [f.get_linewidth() for f in canvas.get_children() if isinstance(f, mpl.patches.FancyArrowPatch)]
```

### Step 6: Assign widths = list(...)

```python
widths = list([l for l in canvas.collections if isinstance(l, mpl.collections.LineCollection)][0].get_linewidths())
```


## Complete Example

```python
# Setup
# Fixtures: param_value, expected, graph_type

# Workflow
G = nx.path_graph(3, create_using=graph_type)
nx.set_edge_attributes(G, {(0, 1): 5, (1, 2): 10}, 'width')
canvas = plt.figure().add_subplot(111)
nx.display(G, edge_width=param_value, canvas=canvas)
if G.is_directed():
    widths = [f.get_linewidth() for f in canvas.get_children() if isinstance(f, mpl.patches.FancyArrowPatch)]
else:
    widths = list([l for l in canvas.collections if isinstance(l, mpl.collections.LineCollection)][0].get_linewidths())
assert widths == expected
```

## Next Steps


---

*Source: test_pylab.py:294 | Complexity: Intermediate | Last updated: 2026-06-02*
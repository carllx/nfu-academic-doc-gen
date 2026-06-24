# How To: Display Edge Single Color

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, mock, workflow, integration

## Overview

Workflow: test display edge single color

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
# Fixtures: edge_color, expected, graph_type
```

## Step-by-Step Guide

### Step 1: Assign G = nx.path_graph(...)

```python
G = nx.path_graph(3, create_using=graph_type)
```

**Verification:**
```python
assert all((mpl.colors.same_color(c, expected) for c in colors))
```

### Step 2: Call nx.set_edge_attributes()

```python
nx.set_edge_attributes(G, '#0000FF', 'color')
```

### Step 3: Assign canvas = plt.figure.add_subplot(...)

```python
canvas = plt.figure().add_subplot(111)
```

### Step 4: Call nx.display()

```python
nx.display(G, edge_color=edge_color, canvas=canvas)
```

**Verification:**
```python
assert all((mpl.colors.same_color(c, expected) for c in colors))
```

### Step 5: Call plt.close()

```python
plt.close()
```

### Step 6: Assign colors = value

```python
colors = [f.get_fc() for f in canvas.get_children() if isinstance(f, mpl.patches.FancyArrowPatch)]
```

### Step 7: Assign colors = unknown.get_colors(...)

```python
colors = [l for l in canvas.collections if isinstance(l, mpl.collections.LineCollection)][0].get_colors()
```


## Complete Example

```python
# Setup
# Fixtures: edge_color, expected, graph_type

# Workflow
G = nx.path_graph(3, create_using=graph_type)
nx.set_edge_attributes(G, '#0000FF', 'color')
canvas = plt.figure().add_subplot(111)
nx.display(G, edge_color=edge_color, canvas=canvas)
if G.is_directed():
    colors = [f.get_fc() for f in canvas.get_children() if isinstance(f, mpl.patches.FancyArrowPatch)]
else:
    colors = [l for l in canvas.collections if isinstance(l, mpl.collections.LineCollection)][0].get_colors()
assert all((mpl.colors.same_color(c, expected) for c in colors))
plt.close()
```

## Next Steps


---

*Source: test_pylab.py:143 | Complexity: Intermediate | Last updated: 2026-06-02*
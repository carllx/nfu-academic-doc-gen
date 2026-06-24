# How To: Display Edge Colormaps

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, mock, workflow, integration

## Overview

Workflow: test display edge colormaps

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
# Fixtures: graph_type
```

## Step-by-Step Guide

### Step 1: Assign G = nx.path_graph(...)

```python
G = nx.path_graph(3, create_using=graph_type)
```

**Verification:**
```python
assert mpl.colors.same_color(expected[0], G.edges[0, 1]['color'])
```

### Step 2: Call nx.set_edge_attributes()

```python
nx.set_edge_attributes(G, {(0, 1): 0, (1, 2): 1}, 'weight')
```

**Verification:**
```python
assert mpl.colors.same_color(expected[1], G.edges[1, 2]['color'])
```

### Step 3: Assign cmap = value

```python
cmap = mpl.colormaps['plasma']
```

**Verification:**
```python
assert mpl.colors.same_color(expected, colors)
```

### Step 4: Call nx.apply_matplotlib_colors()

```python
nx.apply_matplotlib_colors(G, 'weight', 'color', cmap, nodes=False)
```

### Step 5: Assign canvas = plt.figure.add_subplot(...)

```python
canvas = plt.figure().add_subplot(111)
```

### Step 6: Call nx.display()

```python
nx.display(G, canvas=canvas)
```

### Step 7: Assign mapper = mpl.cm.ScalarMappable(...)

```python
mapper = mpl.cm.ScalarMappable(cmap=cmap)
```

### Step 8: Call mapper.set_clim()

```python
mapper.set_clim(0, 1)
```

### Step 9: Assign expected = value

```python
expected = [mapper.to_rgba(0), mapper.to_rgba(1)]
```

**Verification:**
```python
assert mpl.colors.same_color(expected[0], G.edges[0, 1]['color'])
```

### Step 10: Call plt.close()

```python
plt.close()
```

### Step 11: Assign colors = value

```python
colors = [f.get_facecolor() for f in canvas.get_children() if isinstance(f, mpl.patches.FancyArrowPatch)]
```

### Step 12: Assign colors = unknown.get_colors(...)

```python
colors = [l for l in canvas.collections if isinstance(l, mpl.collections.LineCollection)][0].get_colors()
```


## Complete Example

```python
# Setup
# Fixtures: graph_type

# Workflow
G = nx.path_graph(3, create_using=graph_type)
nx.set_edge_attributes(G, {(0, 1): 0, (1, 2): 1}, 'weight')
cmap = mpl.colormaps['plasma']
nx.apply_matplotlib_colors(G, 'weight', 'color', cmap, nodes=False)
canvas = plt.figure().add_subplot(111)
nx.display(G, canvas=canvas)
mapper = mpl.cm.ScalarMappable(cmap=cmap)
mapper.set_clim(0, 1)
expected = [mapper.to_rgba(0), mapper.to_rgba(1)]
if G.is_directed():
    colors = [f.get_facecolor() for f in canvas.get_children() if isinstance(f, mpl.patches.FancyArrowPatch)]
else:
    colors = [l for l in canvas.collections if isinstance(l, mpl.collections.LineCollection)][0].get_colors()
assert mpl.colors.same_color(expected[0], G.edges[0, 1]['color'])
assert mpl.colors.same_color(expected[1], G.edges[1, 2]['color'])
assert mpl.colors.same_color(expected, colors)
plt.close()
```

## Next Steps


---

*Source: test_pylab.py:236 | Complexity: Advanced | Last updated: 2026-06-02*
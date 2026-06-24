# How To: Display Node Colormaps

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test display node colormaps

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
assert mpl.colors.same_color(expected[0], G.nodes[0]['color'])
```

### Step 2: Call nx.set_node_attributes()

```python
nx.set_node_attributes(G, {0: 0, 1: 0.5, 2: 1}, 'weight')
```

**Verification:**
```python
assert mpl.colors.same_color(expected[1], G.nodes[1]['color'])
```

### Step 3: Assign cmap = value

```python
cmap = mpl.colormaps['plasma']
```

**Verification:**
```python
assert mpl.colors.same_color(expected[2], G.nodes[2]['color'])
```

### Step 4: Call nx.apply_matplotlib_colors()

```python
nx.apply_matplotlib_colors(G, 'weight', 'color', cmap)
```

**Verification:**
```python
assert mpl.colors.same_color(expected, colors)
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
expected = [mapper.to_rgba(0), mapper.to_rgba(0.5), mapper.to_rgba(1)]
```

### Step 10: Assign colors = unknown.get_edgecolors(...)

```python
colors = [s for s in canvas.collections if isinstance(s, mpl.collections.PathCollection)][0].get_edgecolors()
```

**Verification:**
```python
assert mpl.colors.same_color(expected[0], G.nodes[0]['color'])
```

### Step 11: Call plt.close()

```python
plt.close()
```


## Complete Example

```python
# Setup
# Fixtures: graph_type

# Workflow
G = nx.path_graph(3, create_using=graph_type)
nx.set_node_attributes(G, {0: 0, 1: 0.5, 2: 1}, 'weight')
cmap = mpl.colormaps['plasma']
nx.apply_matplotlib_colors(G, 'weight', 'color', cmap)
canvas = plt.figure().add_subplot(111)
nx.display(G, canvas=canvas)
mapper = mpl.cm.ScalarMappable(cmap=cmap)
mapper.set_clim(0, 1)
expected = [mapper.to_rgba(0), mapper.to_rgba(0.5), mapper.to_rgba(1)]
colors = [s for s in canvas.collections if isinstance(s, mpl.collections.PathCollection)][0].get_edgecolors()
assert mpl.colors.same_color(expected[0], G.nodes[0]['color'])
assert mpl.colors.same_color(expected[1], G.nodes[1]['color'])
assert mpl.colors.same_color(expected[2], G.nodes[2]['color'])
assert mpl.colors.same_color(expected, colors)
plt.close()
```

## Next Steps


---

*Source: test_pylab.py:265 | Complexity: Advanced | Last updated: 2026-06-02*
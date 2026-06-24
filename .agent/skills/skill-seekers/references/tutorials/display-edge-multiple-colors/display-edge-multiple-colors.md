# How To: Display Edge Multiple Colors

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, mock, workflow, integration

## Overview

Workflow: test display edge multiple colors

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
assert mpl.colors.same_color(colors, expected)
```

### Step 2: Call nx.set_edge_attributes()

```python
nx.set_edge_attributes(G, {(0, 1): '#FF0000', (1, 2): (0, 0, 1)}, 'color')
```

### Step 3: Assign ax = plt.figure.add_subplot(...)

```python
ax = plt.figure().add_subplot(111)
```

### Step 4: Call nx.display()

```python
nx.display(G, canvas=ax)
```

### Step 5: Assign expected = value

```python
expected = ['red', 'blue']
```

**Verification:**
```python
assert mpl.colors.same_color(colors, expected)
```

### Step 6: Call plt.close()

```python
plt.close()
```

### Step 7: Assign colors = value

```python
colors = [f.get_fc() for f in ax.get_children() if isinstance(f, mpl.patches.FancyArrowPatch)]
```

### Step 8: Assign colors = unknown.get_colors(...)

```python
colors = [l for l in ax.collections if isinstance(l, mpl.collections.LineCollection)][0].get_colors()
```


## Complete Example

```python
# Setup
# Fixtures: graph_type

# Workflow
G = nx.path_graph(3, create_using=graph_type)
nx.set_edge_attributes(G, {(0, 1): '#FF0000', (1, 2): (0, 0, 1)}, 'color')
ax = plt.figure().add_subplot(111)
nx.display(G, canvas=ax)
expected = ['red', 'blue']
if G.is_directed():
    colors = [f.get_fc() for f in ax.get_children() if isinstance(f, mpl.patches.FancyArrowPatch)]
else:
    colors = [l for l in ax.collections if isinstance(l, mpl.collections.LineCollection)][0].get_colors()
assert mpl.colors.same_color(colors, expected)
plt.close()
```

## Next Steps


---

*Source: test_pylab.py:165 | Complexity: Advanced | Last updated: 2026-06-02*
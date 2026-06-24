# How To: Display Edge Style

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, mock, workflow, integration

## Overview

Workflow: test display edge style

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
assert styles == expected
```

### Step 2: Call nx.set_edge_attributes()

```python
nx.set_edge_attributes(G, {(0, 1): '-', (1, 2): ':'}, 'style')
```

### Step 3: Assign canvas = plt.figure.add_subplot(...)

```python
canvas = plt.figure().add_subplot(111)
```

### Step 4: Call nx.display()

```python
nx.display(G, edge_style=param_value, canvas=canvas)
```

**Verification:**
```python
assert styles == expected
```

### Step 5: Call plt.close()

```python
plt.close()
```

### Step 6: Assign styles = value

```python
styles = [f.get_linestyle() for f in canvas.get_children() if isinstance(f, mpl.patches.FancyArrowPatch)]
```

### Step 7: Assign linestyles = value

```python
linestyles = {(0, None): '-', (0, (1, 1.65)): ':'}
```

### Step 8: Assign styles = value

```python
styles = [linestyles[s[0], tuple(s[1]) if s[1] is not None else None] for s in [l for l in canvas.collections if isinstance(l, mpl.collections.LineCollection)][0].get_linestyles()]
```


## Complete Example

```python
# Setup
# Fixtures: param_value, expected, graph_type

# Workflow
G = nx.path_graph(3, create_using=graph_type)
nx.set_edge_attributes(G, {(0, 1): '-', (1, 2): ':'}, 'style')
canvas = plt.figure().add_subplot(111)
nx.display(G, edge_style=param_value, canvas=canvas)
if G.is_directed():
    styles = [f.get_linestyle() for f in canvas.get_children() if isinstance(f, mpl.patches.FancyArrowPatch)]
else:
    linestyles = {(0, None): '-', (0, (1, 1.65)): ':'}
    styles = [linestyles[s[0], tuple(s[1]) if s[1] is not None else None] for s in [l for l in canvas.collections if isinstance(l, mpl.collections.LineCollection)][0].get_linestyles()]
assert styles == expected
plt.close()
```

## Next Steps


---

*Source: test_pylab.py:325 | Complexity: Advanced | Last updated: 2026-06-02*
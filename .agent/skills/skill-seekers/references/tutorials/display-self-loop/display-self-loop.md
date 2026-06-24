# How To: Display Self Loop

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: test display self loop

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign ax = plt.axes(...)

```python
ax = plt.axes()
```

**Verification:**
```python
assert bbox.width > 0 and bbox.height > 0
```

### Step 2: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

### Step 3: Call G.add_node()

```python
G.add_node(0)
```

### Step 4: Call G.add_edge()

```python
G.add_edge(0, 0)
```

### Step 5: Call nx.set_node_attributes()

```python
nx.set_node_attributes(G, {0: (0, 0)}, 'pos')
```

### Step 6: Call nx.display()

```python
nx.display(G, canvas=ax)
```

### Step 7: Assign arrow = value

```python
arrow = [f for f in ax.get_children() if isinstance(f, mpl.patches.FancyArrowPatch)][0]
```

### Step 8: Assign bbox = arrow.get_extents(...)

```python
bbox = arrow.get_extents()
```

### Step 9: Call print()

```python
print(bbox.width)
```

### Step 10: Call print()

```python
print(bbox.height)
```

**Verification:**
```python
assert bbox.width > 0 and bbox.height > 0
```

### Step 11: Call plt.delaxes()

```python
plt.delaxes(ax)
```

### Step 12: Call plt.close()

```python
plt.close()
```


## Complete Example

```python
# Workflow
ax = plt.axes()
G = nx.DiGraph()
G.add_node(0)
G.add_edge(0, 0)
nx.set_node_attributes(G, {0: (0, 0)}, 'pos')
nx.display(G, canvas=ax)
arrow = [f for f in ax.get_children() if isinstance(f, mpl.patches.FancyArrowPatch)][0]
bbox = arrow.get_extents()
print(bbox.width)
print(bbox.height)
assert bbox.width > 0 and bbox.height > 0
plt.delaxes(ax)
plt.close()
```

## Next Steps


---

*Source: test_pylab.py:506 | Complexity: Advanced | Last updated: 2026-06-02*
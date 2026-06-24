# How To: Display Edge Position

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, mock, workflow, integration

## Overview

Workflow: test display edge position

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
assert all(abs(act_start - exp_start) < (threshold, threshold)) and all(abs(act_end - exp_end) < (threshold, threshold))
```

### Step 2: Call nx.set_node_attributes()

```python
nx.set_node_attributes(G, {n: (n, n) for n in G.nodes()}, 'pos')
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
expected = [((0, 0), (1, 1)), ((1, 1), (2, 2))]
```

### Step 6: Assign threshold = 0.05

```python
threshold = 0.05
```

### Step 7: Call plt.close()

```python
plt.close()
```

### Step 8: Assign end_points = value

```python
end_points = [(f.get_path().vertices[0, :], f.get_path().vertices[-2, :]) for f in ax.get_children() if isinstance(f, mpl.patches.FancyArrowPatch)]
```

### Step 9: Assign line_collection = value

```python
line_collection = [l for l in ax.collections if isinstance(l, mpl.collections.LineCollection)][0]
```

### Step 10: Assign end_points = value

```python
end_points = [(p.vertices[0, :], p.vertices[-1, :]) for p in line_collection.get_paths()]
```

### Step 11: Assign unknown = a

```python
act_start, act_end = a
```

### Step 12: Assign unknown = e

```python
exp_start, exp_end = e
```

**Verification:**
```python
assert all(abs(act_start - exp_start) < (threshold, threshold)) and all(abs(act_end - exp_end) < (threshold, threshold))
```


## Complete Example

```python
# Setup
# Fixtures: graph_type

# Workflow
G = nx.path_graph(3, create_using=graph_type)
nx.set_node_attributes(G, {n: (n, n) for n in G.nodes()}, 'pos')
ax = plt.figure().add_subplot(111)
nx.display(G, canvas=ax)
if G.is_directed():
    end_points = [(f.get_path().vertices[0, :], f.get_path().vertices[-2, :]) for f in ax.get_children() if isinstance(f, mpl.patches.FancyArrowPatch)]
else:
    line_collection = [l for l in ax.collections if isinstance(l, mpl.collections.LineCollection)][0]
    end_points = [(p.vertices[0, :], p.vertices[-1, :]) for p in line_collection.get_paths()]
expected = [((0, 0), (1, 1)), ((1, 1), (2, 2))]
threshold = 0.05
for a, e in zip(end_points, expected):
    act_start, act_end = a
    exp_start, exp_end = e
    assert all(abs(act_start - exp_start) < (threshold, threshold)) and all(abs(act_end - exp_end) < (threshold, threshold))
plt.close()
```

## Next Steps


---

*Source: test_pylab.py:186 | Complexity: Advanced | Last updated: 2026-06-02*
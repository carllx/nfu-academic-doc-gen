# How To: Display Position Function

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test display position function

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

### Step 1: Assign G = nx.karate_club_graph(...)

```python
G = nx.karate_club_graph()
```

**Verification:**
```python
assert all(pos[n] == act_pos[n])
```

### Step 2: Assign pos = fixed_layout(...)

```python
pos = fixed_layout(G)
```

### Step 3: Assign ax = plt.figure.add_subplot(...)

```python
ax = plt.figure().add_subplot(111)
```

### Step 4: Call nx.display()

```python
nx.display(G, node_pos=fixed_layout, canvas=ax)
```

### Step 5: Assign act_pos = value

```python
act_pos = {n: tuple(p) for n, p in zip(G.nodes(), ax.get_children()[0].get_offsets().data)}
```

### Step 6: Call plt.close()

```python
plt.close()
```

**Verification:**
```python
assert all(pos[n] == act_pos[n])
```


## Complete Example

```python
# Workflow
G = nx.karate_club_graph()

def fixed_layout(G):
    return nx.spring_layout(G, seed=314159)
pos = fixed_layout(G)
ax = plt.figure().add_subplot(111)
nx.display(G, node_pos=fixed_layout, canvas=ax)
act_pos = {n: tuple(p) for n, p in zip(G.nodes(), ax.get_children()[0].get_offsets().data)}
for n in G.nodes():
    assert all(pos[n] == act_pos[n])
plt.close()
```

## Next Steps


---

*Source: test_pylab.py:217 | Complexity: Intermediate | Last updated: 2026-06-02*
# How To: Default Scale And Center

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test default scale and center

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `math`


## Step-by-Step Guide

### Step 1: Assign sc = value

```python
sc = self.check_scale_and_center
```

### Step 2: Assign c = value

```python
c = (0, 0)
```

### Step 3: Assign G = nx.complete_graph(...)

```python
G = nx.complete_graph(9)
```

### Step 4: Call G.add_node()

```python
G.add_node(9)
```

### Step 5: Call sc()

```python
sc(nx.random_layout(G), scale=0.5, center=(0.5, 0.5))
```

### Step 6: Call sc()

```python
sc(nx.spring_layout(G), scale=1, center=c)
```

### Step 7: Call sc()

```python
sc(nx.spectral_layout(G), scale=1, center=c)
```

### Step 8: Call sc()

```python
sc(nx.circular_layout(G), scale=1, center=c)
```

### Step 9: Call sc()

```python
sc(nx.shell_layout(G), scale=1, center=c)
```

### Step 10: Call sc()

```python
sc(nx.spiral_layout(G), scale=1, center=c)
```

### Step 11: Call sc()

```python
sc(nx.kamada_kawai_layout(G), scale=1, center=c)
```

### Step 12: Assign c = value

```python
c = (0, 0, 0)
```

### Step 13: Call sc()

```python
sc(nx.kamada_kawai_layout(G, dim=3), scale=1, center=c)
```


## Complete Example

```python
# Workflow
sc = self.check_scale_and_center
c = (0, 0)
G = nx.complete_graph(9)
G.add_node(9)
sc(nx.random_layout(G), scale=0.5, center=(0.5, 0.5))
sc(nx.spring_layout(G), scale=1, center=c)
sc(nx.spectral_layout(G), scale=1, center=c)
sc(nx.circular_layout(G), scale=1, center=c)
sc(nx.shell_layout(G), scale=1, center=c)
sc(nx.spiral_layout(G), scale=1, center=c)
sc(nx.kamada_kawai_layout(G), scale=1, center=c)
c = (0, 0, 0)
sc(nx.kamada_kawai_layout(G, dim=3), scale=1, center=c)
```

## Next Steps


---

*Source: test_layout.py:133 | Complexity: Advanced | Last updated: 2026-06-02*
# How To: Exception Pos Single Graph

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test exception pos single graph

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `networkx`

**Setup Required:**
```python
# Fixtures: to_latex
```

## Step-by-Step Guide

### Step 1: Assign G = nx.path_graph(...)

```python
G = nx.path_graph(4)
```

### Step 2: Call to_latex()

```python
to_latex(G, pos='pos')
```

### Step 3: Assign pos = value

```python
pos = {0: (1, 2), 1: (0, 1), 2: (2, 1)}
```

### Step 4: Assign unknown = value

```python
pos[3] = (1, 2, 3)
```

### Step 5: Assign unknown = 2

```python
pos[3] = 2
```

### Step 6: Assign unknown = value

```python
pos[3] = (3, 2)
```

### Step 7: Call to_latex()

```python
to_latex(G, pos)
```

### Step 8: Call to_latex()

```python
to_latex(G, pos)
```

### Step 9: Call to_latex()

```python
to_latex(G, pos)
```

### Step 10: Call to_latex()

```python
to_latex(G, pos)
```


## Complete Example

```python
# Setup
# Fixtures: to_latex

# Workflow
G = nx.path_graph(4)
to_latex(G, pos='pos')
pos = {0: (1, 2), 1: (0, 1), 2: (2, 1)}
with pytest.raises(nx.NetworkXError):
    to_latex(G, pos)
pos[3] = (1, 2, 3)
with pytest.raises(nx.NetworkXError):
    to_latex(G, pos)
pos[3] = 2
with pytest.raises(nx.NetworkXError):
    to_latex(G, pos)
pos[3] = (3, 2)
to_latex(G, pos)
```

## Next Steps


---

*Source: test_latex.py:226 | Complexity: Advanced | Last updated: 2026-06-02*
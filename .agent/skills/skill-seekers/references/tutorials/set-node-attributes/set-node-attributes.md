# How To: Set Node Attributes

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test set node attributes

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `random`
- `pytest`
- `networkx`
- `networkx.utils`

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
assert G.nodes[0][attr] == vals
```

### Step 2: Assign vals = 100

```python
vals = 100
```

**Verification:**
```python
assert G.nodes[1][attr] == vals
```

### Step 3: Assign attr = 'hello'

```python
attr = 'hello'
```

**Verification:**
```python
assert G.nodes[2][attr] == vals
```

### Step 4: Call nx.set_node_attributes()

```python
nx.set_node_attributes(G, vals, attr)
```

**Verification:**
```python
assert G.nodes[0][attr] == 0
```

### Step 5: Assign G = nx.path_graph(...)

```python
G = nx.path_graph(3, create_using=graph_type)
```

**Verification:**
```python
assert G.nodes[1][attr] == 1
```

### Step 6: Assign vals = dict(...)

```python
vals = dict(zip(sorted(G.nodes()), range(len(G))))
```

**Verification:**
```python
assert G.nodes[2][attr] == 2
```

### Step 7: Assign attr = 'hi'

```python
attr = 'hi'
```

**Verification:**
```python
assert G.nodes[0] == {}
```

### Step 8: Call nx.set_node_attributes()

```python
nx.set_node_attributes(G, vals, attr)
```

**Verification:**
```python
assert G.nodes[1]['hi'] == 0
```

### Step 9: Assign G = nx.path_graph(...)

```python
G = nx.path_graph(3, create_using=graph_type)
```

**Verification:**
```python
assert G.nodes[2]['hello'] == 200
```

### Step 10: Assign d = value

```python
d = {'hi': 0, 'hello': 200}
```

### Step 11: Assign vals = dict.fromkeys(...)

```python
vals = dict.fromkeys(G.nodes(), d)
```

### Step 12: Call vals.pop()

```python
vals.pop(0)
```

### Step 13: Call nx.set_node_attributes()

```python
nx.set_node_attributes(G, vals)
```

**Verification:**
```python
assert G.nodes[0] == {}
```


## Complete Example

```python
# Setup
# Fixtures: graph_type

# Workflow
G = nx.path_graph(3, create_using=graph_type)
vals = 100
attr = 'hello'
nx.set_node_attributes(G, vals, attr)
assert G.nodes[0][attr] == vals
assert G.nodes[1][attr] == vals
assert G.nodes[2][attr] == vals
G = nx.path_graph(3, create_using=graph_type)
vals = dict(zip(sorted(G.nodes()), range(len(G))))
attr = 'hi'
nx.set_node_attributes(G, vals, attr)
assert G.nodes[0][attr] == 0
assert G.nodes[1][attr] == 1
assert G.nodes[2][attr] == 2
G = nx.path_graph(3, create_using=graph_type)
d = {'hi': 0, 'hello': 200}
vals = dict.fromkeys(G.nodes(), d)
vals.pop(0)
nx.set_node_attributes(G, vals)
assert G.nodes[0] == {}
assert G.nodes[1]['hi'] == 0
assert G.nodes[2]['hello'] == 200
```

## Next Steps


---

*Source: test_function.py:486 | Complexity: Advanced | Last updated: 2026-06-02*
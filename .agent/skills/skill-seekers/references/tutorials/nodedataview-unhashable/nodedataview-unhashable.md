# How To: Nodedataview Unhashable

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test nodedataview unhashable

## Prerequisites

**Required Modules:**
- `pickle`
- `copy`
- `pytest`
- `networkx`
- `networkx.classes`
- `networkx.classes.reportviews`
- `pickle`
- `pickle`
- `pickle`
- `pickle`
- `pickle`


## Step-by-Step Guide

### Step 1: Assign G = nx.path_graph(...)

```python
G = nx.path_graph(9)
```

### Step 2: Assign unknown = 'bar'

```python
G.nodes[3]['foo'] = 'bar'
```

### Step 3: Assign nvs = value

```python
nvs = [G.nodes.data()]
```

### Step 4: Call nvs.append()

```python
nvs.append(G.nodes.data(True))
```

### Step 5: Assign H = G.copy(...)

```python
H = G.copy()
```

### Step 6: Assign unknown = value

```python
H.nodes[4]['foo'] = {1, 2, 3}
```

### Step 7: Call nvs.append()

```python
nvs.append(H.nodes.data(True))
```

### Step 8: Assign Gn = G.nodes.data(...)

```python
Gn = G.nodes.data(False)
```

### Step 9: Call set()

```python
set(Gn)
```

### Step 10: Gn | Gn

```python
Gn | Gn
```

### Step 11: Assign Gn = G.nodes.data(...)

```python
Gn = G.nodes.data('foo')
```

### Step 12: Call set()

```python
set(Gn)
```

### Step 13: Gn | Gn

```python
Gn | Gn
```

### Step 14: Call pytest.raises()

```python
pytest.raises(TypeError, set, nv)
```

### Step 15: Call pytest.raises()

```python
pytest.raises(TypeError, eval, 'nv | nv', locals())
```


## Complete Example

```python
# Workflow
G = nx.path_graph(9)
G.nodes[3]['foo'] = 'bar'
nvs = [G.nodes.data()]
nvs.append(G.nodes.data(True))
H = G.copy()
H.nodes[4]['foo'] = {1, 2, 3}
nvs.append(H.nodes.data(True))
for nv in nvs:
    pytest.raises(TypeError, set, nv)
    pytest.raises(TypeError, eval, 'nv | nv', locals())
Gn = G.nodes.data(False)
set(Gn)
Gn | Gn
Gn = G.nodes.data('foo')
set(Gn)
Gn | Gn
```

## Next Steps


---

*Source: test_reportviews.py:179 | Complexity: Advanced | Last updated: 2026-06-02*
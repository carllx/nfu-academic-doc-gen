# How To: Missing Viz Attributes

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test missing viz attributes

## Prerequisites

**Required Modules:**
- `io`
- `time`
- `pytest`
- `networkx`
- `math`


## Step-by-Step Guide

### Step 1: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

**Verification:**
```python
assert sorted(G.nodes()) == sorted(H.nodes())
```

### Step 2: Call G.add_node()

```python
G.add_node(0, label='1', color='green')
```

**Verification:**
```python
assert sorted((sorted(e) for e in G.edges())) == sorted((sorted(e) for e in H.edges()))
```

### Step 3: Assign unknown = value

```python
G.nodes[0]['viz'] = {'size': 54}
```

**Verification:**
```python
assert H.nodes[0]['viz']['color']['a'] == 1.0
```

### Step 4: Assign unknown = value

```python
G.nodes[0]['viz']['position'] = {'x': 0, 'y': 1, 'z': 0}
```

**Verification:**
```python
assert sorted(G.nodes()) == sorted(H.nodes())
```

### Step 5: Assign unknown = value

```python
G.nodes[0]['viz']['color'] = {'r': 0, 'g': 0, 'b': 256}
```

**Verification:**
```python
assert sorted((sorted(e) for e in G.edges())) == sorted((sorted(e) for e in H.edges()))
```

### Step 6: Assign unknown = 'http://random.url'

```python
G.nodes[0]['viz']['shape'] = 'http://random.url'
```

### Step 7: Assign unknown = 2

```python
G.nodes[0]['viz']['thickness'] = 2
```

### Step 8: Assign fh = io.BytesIO(...)

```python
fh = io.BytesIO()
```

### Step 9: Call nx.write_gexf()

```python
nx.write_gexf(G, fh, version='1.1draft')
```

### Step 10: Call fh.seek()

```python
fh.seek(0)
```

### Step 11: Assign H = nx.read_gexf(...)

```python
H = nx.read_gexf(fh, node_type=int)
```

**Verification:**
```python
assert sorted(G.nodes()) == sorted(H.nodes())
```

### Step 12: Assign fh = io.BytesIO(...)

```python
fh = io.BytesIO()
```

### Step 13: Call nx.write_gexf()

```python
nx.write_gexf(G, fh, version='1.2draft')
```

### Step 14: Call fh.seek()

```python
fh.seek(0)
```

### Step 15: Assign H = nx.read_gexf(...)

```python
H = nx.read_gexf(fh, node_type=int)
```

**Verification:**
```python
assert H.nodes[0]['viz']['color']['a'] == 1.0
```

### Step 16: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

### Step 17: Call G.add_node()

```python
G.add_node(0, label='1', color='green')
```

### Step 18: Assign unknown = value

```python
G.nodes[0]['viz'] = {'size': 54}
```

### Step 19: Assign unknown = value

```python
G.nodes[0]['viz']['position'] = {'x': 0, 'y': 1, 'z': 0}
```

### Step 20: Assign unknown = value

```python
G.nodes[0]['viz']['color'] = {'r': 0, 'g': 0, 'b': 256, 'a': 0.5}
```

### Step 21: Assign unknown = 'ftp://random.url'

```python
G.nodes[0]['viz']['shape'] = 'ftp://random.url'
```

### Step 22: Assign unknown = 2

```python
G.nodes[0]['viz']['thickness'] = 2
```

### Step 23: Assign fh = io.BytesIO(...)

```python
fh = io.BytesIO()
```

### Step 24: Call nx.write_gexf()

```python
nx.write_gexf(G, fh)
```

### Step 25: Call fh.seek()

```python
fh.seek(0)
```

### Step 26: Assign H = nx.read_gexf(...)

```python
H = nx.read_gexf(fh, node_type=int)
```

**Verification:**
```python
assert sorted(G.nodes()) == sorted(H.nodes())
```


## Complete Example

```python
# Workflow
G = nx.Graph()
G.add_node(0, label='1', color='green')
G.nodes[0]['viz'] = {'size': 54}
G.nodes[0]['viz']['position'] = {'x': 0, 'y': 1, 'z': 0}
G.nodes[0]['viz']['color'] = {'r': 0, 'g': 0, 'b': 256}
G.nodes[0]['viz']['shape'] = 'http://random.url'
G.nodes[0]['viz']['thickness'] = 2
fh = io.BytesIO()
nx.write_gexf(G, fh, version='1.1draft')
fh.seek(0)
H = nx.read_gexf(fh, node_type=int)
assert sorted(G.nodes()) == sorted(H.nodes())
assert sorted((sorted(e) for e in G.edges())) == sorted((sorted(e) for e in H.edges()))
fh = io.BytesIO()
nx.write_gexf(G, fh, version='1.2draft')
fh.seek(0)
H = nx.read_gexf(fh, node_type=int)
assert H.nodes[0]['viz']['color']['a'] == 1.0
G = nx.Graph()
G.add_node(0, label='1', color='green')
G.nodes[0]['viz'] = {'size': 54}
G.nodes[0]['viz']['position'] = {'x': 0, 'y': 1, 'z': 0}
G.nodes[0]['viz']['color'] = {'r': 0, 'g': 0, 'b': 256, 'a': 0.5}
G.nodes[0]['viz']['shape'] = 'ftp://random.url'
G.nodes[0]['viz']['thickness'] = 2
fh = io.BytesIO()
nx.write_gexf(G, fh)
fh.seek(0)
H = nx.read_gexf(fh, node_type=int)
assert sorted(G.nodes()) == sorted(H.nodes())
assert sorted((sorted(e) for e in G.edges())) == sorted((sorted(e) for e in H.edges()))
```

## Next Steps


---

*Source: test_gexf.py:532 | Complexity: Advanced | Last updated: 2026-06-02*
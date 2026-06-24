# How To: Specials

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test specials

## Prerequisites

**Required Modules:**
- `io`
- `time`
- `pytest`
- `networkx`
- `math`


## Step-by-Step Guide

### Step 1: Assign unknown = value

```python
inf, nan = (float('inf'), float('nan'))
```

**Verification:**
```python
assert b'INF' in filetext
```

### Step 2: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

**Verification:**
```python
assert b'NaN' in filetext
```

### Step 3: Call G.add_node()

```python
G.add_node(1, testattr=inf, strdata='inf', key='a')
```

**Verification:**
```python
assert b'-INF' in filetext
```

### Step 4: Call G.add_node()

```python
G.add_node(2, testattr=nan, strdata='nan', key='b')
```

**Verification:**
```python
assert H.nodes[1]['testattr'] == inf
```

### Step 5: Call G.add_node()

```python
G.add_node(3, testattr=-inf, strdata='-inf', key='c')
```

**Verification:**
```python
assert isnan(H.nodes[2]['testattr'])
```

### Step 6: Assign fh = io.BytesIO(...)

```python
fh = io.BytesIO()
```

**Verification:**
```python
assert H.nodes[3]['testattr'] == -inf
```

### Step 7: Call nx.write_gexf()

```python
nx.write_gexf(G, fh)
```

**Verification:**
```python
assert H.nodes[1]['strdata'] == 'inf'
```

### Step 8: Call fh.seek()

```python
fh.seek(0)
```

**Verification:**
```python
assert H.nodes[2]['strdata'] == 'nan'
```

### Step 9: Assign filetext = fh.read(...)

```python
filetext = fh.read()
```

**Verification:**
```python
assert H.nodes[3]['strdata'] == '-inf'
```

### Step 10: Call fh.seek()

```python
fh.seek(0)
```

**Verification:**
```python
assert H.nodes[1]['networkx_key'] == 'a'
```

### Step 11: Assign H = nx.read_gexf(...)

```python
H = nx.read_gexf(fh, node_type=int)
```

**Verification:**
```python
assert H.nodes[2]['networkx_key'] == 'b'
```


## Complete Example

```python
# Workflow
from math import isnan
inf, nan = (float('inf'), float('nan'))
G = nx.Graph()
G.add_node(1, testattr=inf, strdata='inf', key='a')
G.add_node(2, testattr=nan, strdata='nan', key='b')
G.add_node(3, testattr=-inf, strdata='-inf', key='c')
fh = io.BytesIO()
nx.write_gexf(G, fh)
fh.seek(0)
filetext = fh.read()
fh.seek(0)
H = nx.read_gexf(fh, node_type=int)
assert b'INF' in filetext
assert b'NaN' in filetext
assert b'-INF' in filetext
assert H.nodes[1]['testattr'] == inf
assert isnan(H.nodes[2]['testattr'])
assert H.nodes[3]['testattr'] == -inf
assert H.nodes[1]['strdata'] == 'inf'
assert H.nodes[2]['strdata'] == 'nan'
assert H.nodes[3]['strdata'] == '-inf'
assert H.nodes[1]['networkx_key'] == 'a'
assert H.nodes[2]['networkx_key'] == 'b'
assert H.nodes[3]['networkx_key'] == 'c'
```

## Next Steps


---

*Source: test_gexf.py:461 | Complexity: Advanced | Last updated: 2026-06-02*
# How To: Preserve Multi Edge Data

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test that data and keys of edges are preserved on consequent
write and reads

## Prerequisites

**Required Modules:**
- `io`
- `pytest`
- `networkx`
- `networkx.readwrite.graphml`
- `networkx.utils`
- `xml.etree.ElementTree`
- `xml.etree.ElementTree`
- `xml.etree.ElementTree`
- `xml.etree.ElementTree`
- `json`
- `lxml.etree`


## Step-by-Step Guide

### Step 1: '\n        Test that data and keys of edges are preserved on consequent\n        write and reads\n        '

```python
'\n        Test that data and keys of edges are preserved on consequent\n        write and reads\n        '
```

**Verification:**
```python
assert edges_equal(G.edges(data=True, keys=True), H.edges(data=True, keys=True))
```

### Step 2: Assign G = nx.MultiGraph(...)

```python
G = nx.MultiGraph()
```

**Verification:**
```python
assert G._adj == H._adj
```

### Step 3: Call G.add_node()

```python
G.add_node(1)
```

**Verification:**
```python
assert Gadj == HH._adj
```

### Step 4: Call G.add_node()

```python
G.add_node(2)
```

**Verification:**
```python
assert Gadj == HH._adj
```

### Step 5: Call G.add_edges_from()

```python
G.add_edges_from([(1, 2), (1, 2, {'key': 'data_key1'}), (1, 2, {'id': 'data_id2'}), (1, 2, {'key': 'data_key3', 'id': 'data_id3'}), (1, 2, 103, {'key': 'data_key4'}), (1, 2, 104, {'id': 'data_id5'}), (1, 2, 105, {'key': 'data_key6', 'id': 'data_id7'})])
```

### Step 6: Assign fh = io.BytesIO(...)

```python
fh = io.BytesIO()
```

### Step 7: Call nx.write_graphml()

```python
nx.write_graphml(G, fh)
```

### Step 8: Call fh.seek()

```python
fh.seek(0)
```

### Step 9: Assign H = nx.read_graphml(...)

```python
H = nx.read_graphml(fh, node_type=int)
```

**Verification:**
```python
assert edges_equal(G.edges(data=True, keys=True), H.edges(data=True, keys=True))
```

### Step 10: Assign Gadj = value

```python
Gadj = {str(node): {str(nbr): {str(ekey): dd for ekey, dd in key_dict.items()} for nbr, key_dict in nbr_dict.items()} for node, nbr_dict in G._adj.items()}
```

### Step 11: Call fh.seek()

```python
fh.seek(0)
```

### Step 12: Assign HH = nx.read_graphml(...)

```python
HH = nx.read_graphml(fh, node_type=str, edge_key_type=str)
```

**Verification:**
```python
assert Gadj == HH._adj
```

### Step 13: Call fh.seek()

```python
fh.seek(0)
```

### Step 14: Assign string_fh = fh.read(...)

```python
string_fh = fh.read()
```

### Step 15: Assign HH = nx.parse_graphml(...)

```python
HH = nx.parse_graphml(string_fh, node_type=str, edge_key_type=str)
```

**Verification:**
```python
assert Gadj == HH._adj
```


## Complete Example

```python
# Workflow
'\n        Test that data and keys of edges are preserved on consequent\n        write and reads\n        '
G = nx.MultiGraph()
G.add_node(1)
G.add_node(2)
G.add_edges_from([(1, 2), (1, 2, {'key': 'data_key1'}), (1, 2, {'id': 'data_id2'}), (1, 2, {'key': 'data_key3', 'id': 'data_id3'}), (1, 2, 103, {'key': 'data_key4'}), (1, 2, 104, {'id': 'data_id5'}), (1, 2, 105, {'key': 'data_key6', 'id': 'data_id7'})])
fh = io.BytesIO()
nx.write_graphml(G, fh)
fh.seek(0)
H = nx.read_graphml(fh, node_type=int)
assert edges_equal(G.edges(data=True, keys=True), H.edges(data=True, keys=True))
assert G._adj == H._adj
Gadj = {str(node): {str(nbr): {str(ekey): dd for ekey, dd in key_dict.items()} for nbr, key_dict in nbr_dict.items()} for node, nbr_dict in G._adj.items()}
fh.seek(0)
HH = nx.read_graphml(fh, node_type=str, edge_key_type=str)
assert Gadj == HH._adj
fh.seek(0)
string_fh = fh.read()
HH = nx.parse_graphml(string_fh, node_type=str, edge_key_type=str)
assert Gadj == HH._adj
```

## Next Steps


---

*Source: test_graphml.py:510 | Complexity: Advanced | Last updated: 2026-06-02*
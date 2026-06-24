# How To: Write Read Simple Directed Graphml

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test write read simple directed graphml

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

### Step 1: Assign G = value

```python
G = self.simple_directed_graph
```

**Verification:**
```python
assert sorted(G.nodes()) == sorted(H.nodes())
```

### Step 2: Assign unknown = 'there'

```python
G.graph['hi'] = 'there'
```

**Verification:**
```python
assert sorted(G.edges()) == sorted(H.edges())
```

### Step 3: Assign fh = io.BytesIO(...)

```python
fh = io.BytesIO()
```

**Verification:**
```python
assert sorted(G.edges(data=True)) == sorted(H.edges(data=True))
```

### Step 4: Call self.writer()

```python
self.writer(G, fh)
```

### Step 5: Call fh.seek()

```python
fh.seek(0)
```

### Step 6: Assign H = nx.read_graphml(...)

```python
H = nx.read_graphml(fh)
```

**Verification:**
```python
assert sorted(G.nodes()) == sorted(H.nodes())
```

### Step 7: Call self.simple_directed_fh.seek()

```python
self.simple_directed_fh.seek(0)
```


## Complete Example

```python
# Workflow
G = self.simple_directed_graph
G.graph['hi'] = 'there'
fh = io.BytesIO()
self.writer(G, fh)
fh.seek(0)
H = nx.read_graphml(fh)
assert sorted(G.nodes()) == sorted(H.nodes())
assert sorted(G.edges()) == sorted(H.edges())
assert sorted(G.edges(data=True)) == sorted(H.edges(data=True))
self.simple_directed_fh.seek(0)
```

## Next Steps


---

*Source: test_graphml.py:1109 | Complexity: Intermediate | Last updated: 2026-06-02*
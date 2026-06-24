# How To: Write Read Simple No Prettyprint

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test write read simple no prettyprint

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

### Step 3: Assign unknown = '1'

```python
G.graph['id'] = '1'
```

**Verification:**
```python
assert sorted(G.edges(data=True)) == sorted(H.edges(data=True))
```

### Step 4: Assign fh = io.BytesIO(...)

```python
fh = io.BytesIO()
```

### Step 5: Call self.writer()

```python
self.writer(G, fh, prettyprint=False)
```

### Step 6: Call fh.seek()

```python
fh.seek(0)
```

### Step 7: Assign H = nx.read_graphml(...)

```python
H = nx.read_graphml(fh)
```

**Verification:**
```python
assert sorted(G.nodes()) == sorted(H.nodes())
```

### Step 8: Call self.simple_directed_fh.seek()

```python
self.simple_directed_fh.seek(0)
```


## Complete Example

```python
# Workflow
G = self.simple_directed_graph
G.graph['hi'] = 'there'
G.graph['id'] = '1'
fh = io.BytesIO()
self.writer(G, fh, prettyprint=False)
fh.seek(0)
H = nx.read_graphml(fh)
assert sorted(G.nodes()) == sorted(H.nodes())
assert sorted(G.edges()) == sorted(H.edges())
assert sorted(G.edges(data=True)) == sorted(H.edges(data=True))
self.simple_directed_fh.seek(0)
```

## Next Steps


---

*Source: test_graphml.py:1127 | Complexity: Advanced | Last updated: 2026-06-02*
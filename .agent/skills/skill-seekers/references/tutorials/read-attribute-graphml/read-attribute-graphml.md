# How To: Read Attribute Graphml

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test read attribute graphml

## Prerequisites

**Required Modules:**
- `io`
- `time`
- `pytest`
- `networkx`
- `math`


## Step-by-Step Guide

### Step 1: Assign G = value

```python
G = self.attribute_graph
```

**Verification:**
```python
assert sorted(G.nodes(True)) == sorted(H.nodes(data=True))
```

### Step 2: Assign H = nx.read_gexf(...)

```python
H = nx.read_gexf(self.attribute_fh)
```

**Verification:**
```python
assert a == b
```

### Step 3: Assign ge = sorted(...)

```python
ge = sorted(G.edges(data=True))
```

### Step 4: Assign he = sorted(...)

```python
he = sorted(H.edges(data=True))
```

### Step 5: Call self.attribute_fh.seek()

```python
self.attribute_fh.seek(0)
```

**Verification:**
```python
assert a == b
```


## Complete Example

```python
# Workflow
G = self.attribute_graph
H = nx.read_gexf(self.attribute_fh)
assert sorted(G.nodes(True)) == sorted(H.nodes(data=True))
ge = sorted(G.edges(data=True))
he = sorted(H.edges(data=True))
for a, b in zip(ge, he):
    assert a == b
self.attribute_fh.seek(0)
```

## Next Steps


---

*Source: test_gexf.py:218 | Complexity: Intermediate | Last updated: 2026-06-02*
# How To: Label Kwarg

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test label kwarg

## Prerequisites

**Required Modules:**
- `codecs`
- `io`
- `math`
- `ast`
- `contextlib`
- `textwrap`
- `pytest`
- `networkx`
- `networkx.readwrite.gml`
- `numpy`


## Step-by-Step Guide

### Step 1: Assign G = nx.parse_gml(...)

```python
G = nx.parse_gml(self.simple_data, label='id')
```

**Verification:**
```python
assert sorted(G.nodes) == [1, 2, 3]
```

### Step 2: Assign labels = value

```python
labels = [G.nodes[n]['label'] for n in sorted(G.nodes)]
```

**Verification:**
```python
assert labels == ['Node 1', 'Node 2', 'Node 3']
```

### Step 3: Assign G = nx.parse_gml(...)

```python
G = nx.parse_gml(self.simple_data, label=None)
```

**Verification:**
```python
assert sorted(G.nodes) == [1, 2, 3]
```

### Step 4: Assign labels = value

```python
labels = [G.nodes[n]['label'] for n in sorted(G.nodes)]
```

**Verification:**
```python
assert labels == ['Node 1', 'Node 2', 'Node 3']
```


## Complete Example

```python
# Workflow
G = nx.parse_gml(self.simple_data, label='id')
assert sorted(G.nodes) == [1, 2, 3]
labels = [G.nodes[n]['label'] for n in sorted(G.nodes)]
assert labels == ['Node 1', 'Node 2', 'Node 3']
G = nx.parse_gml(self.simple_data, label=None)
assert sorted(G.nodes) == [1, 2, 3]
labels = [G.nodes[n]['label'] for n in sorted(G.nodes)]
assert labels == ['Node 1', 'Node 2', 'Node 3']
```

## Next Steps


---

*Source: test_gml.py:571 | Complexity: Intermediate | Last updated: 2026-06-02*
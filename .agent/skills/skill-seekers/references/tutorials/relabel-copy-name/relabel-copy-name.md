# How To: Relabel Copy Name

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test relabel copy name

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.generators.classic`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

**Verification:**
```python
assert H.graph == G.graph
```

### Step 2: Assign H = nx.relabel_nodes(...)

```python
H = nx.relabel_nodes(G, {}, copy=True)
```

**Verification:**
```python
assert H.graph == G.graph
```

### Step 3: Assign H = nx.relabel_nodes(...)

```python
H = nx.relabel_nodes(G, {}, copy=False)
```

**Verification:**
```python
assert H.graph == G.graph
```

### Step 4: Assign G.name = 'first'

```python
G.name = 'first'
```

**Verification:**
```python
assert H.graph == G.graph
```

### Step 5: Assign H = nx.relabel_nodes(...)

```python
H = nx.relabel_nodes(G, {}, copy=True)
```

**Verification:**
```python
assert H.graph == G.graph
```

### Step 6: Assign H = nx.relabel_nodes(...)

```python
H = nx.relabel_nodes(G, {}, copy=False)
```

**Verification:**
```python
assert H.graph == G.graph
```


## Complete Example

```python
# Workflow
G = nx.Graph()
H = nx.relabel_nodes(G, {}, copy=True)
assert H.graph == G.graph
H = nx.relabel_nodes(G, {}, copy=False)
assert H.graph == G.graph
G.name = 'first'
H = nx.relabel_nodes(G, {}, copy=True)
assert H.graph == G.graph
H = nx.relabel_nodes(G, {}, copy=False)
assert H.graph == G.graph
```

## Next Steps


---

*Source: test_relabel.py:176 | Complexity: Intermediate | Last updated: 2026-06-02*
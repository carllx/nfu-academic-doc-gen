# How To: Convert To Integers2

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test convert to integers2

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.generators.classic`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign G = empty_graph(...)

```python
G = empty_graph()
```

**Verification:**
```python
assert sorted(degH) == sorted(degG)
```

### Step 2: Call G.add_edges_from()

```python
G.add_edges_from([('C', 'D'), ('A', 'B'), ('A', 'C'), ('B', 'C')])
```

**Verification:**
```python
assert H.nodes[0]['label'] == 'A'
```

### Step 3: Assign H = nx.convert_node_labels_to_integers(...)

```python
H = nx.convert_node_labels_to_integers(G, ordering='sorted')
```

**Verification:**
```python
assert H.nodes[1]['label'] == 'B'
```

### Step 4: Assign degH = value

```python
degH = (d for n, d in H.degree())
```

**Verification:**
```python
assert H.nodes[2]['label'] == 'C'
```

### Step 5: Assign degG = value

```python
degG = (d for n, d in G.degree())
```

**Verification:**
```python
assert H.nodes[3]['label'] == 'D'
```

### Step 6: Assign H = nx.convert_node_labels_to_integers(...)

```python
H = nx.convert_node_labels_to_integers(G, ordering='sorted', label_attribute='label')
```

**Verification:**
```python
assert H.nodes[0]['label'] == 'A'
```


## Complete Example

```python
# Workflow
G = empty_graph()
G.add_edges_from([('C', 'D'), ('A', 'B'), ('A', 'C'), ('B', 'C')])
H = nx.convert_node_labels_to_integers(G, ordering='sorted')
degH = (d for n, d in H.degree())
degG = (d for n, d in G.degree())
assert sorted(degH) == sorted(degG)
H = nx.convert_node_labels_to_integers(G, ordering='sorted', label_attribute='label')
assert H.nodes[0]['label'] == 'A'
assert H.nodes[1]['label'] == 'B'
assert H.nodes[2]['label'] == 'C'
assert H.nodes[3]['label'] == 'D'
```

## Next Steps


---

*Source: test_relabel.py:70 | Complexity: Intermediate | Last updated: 2026-06-02*
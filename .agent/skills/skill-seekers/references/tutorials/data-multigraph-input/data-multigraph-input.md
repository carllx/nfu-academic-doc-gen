# How To: Data Multigraph Input

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test data multigraph input

## Prerequisites

**Required Modules:**
- `collections`
- `pytest`
- `networkx`
- `networkx.utils`
- `test_graph`
- `test_graph`


## Step-by-Step Guide

### Step 1: Assign edata0 = value

```python
edata0 = {'w': 200, 's': 'foo'}
```

**Verification:**
```python
assert list(G.edges(keys=True, data=True)) == multiple_edge
```

### Step 2: Assign edata1 = value

```python
edata1 = {'w': 201, 's': 'bar'}
```

**Verification:**
```python
assert list(G.edges(keys=True, data=True)) == multiple_edge
```

### Step 3: Assign keydict = value

```python
keydict = {0: edata0, 1: edata1}
```

**Verification:**
```python
assert list(G.edges(keys=True, data=True)) == single_edge
```

### Step 4: Assign dododod = value

```python
dododod = {'a': {'b': keydict}}
```

**Verification:**
```python
assert nx.is_isomorphic(G, H) is True
```

### Step 5: Assign multiple_edge = value

```python
multiple_edge = [('a', 'b', 0, edata0), ('a', 'b', 1, edata1)]
```

**Verification:**
```python
assert nx.is_isomorphic(G, H) == mgi
```

### Step 6: Assign single_edge = value

```python
single_edge = [('a', 'b', 0, keydict)]
```

### Step 7: Assign G = self.Graph(...)

```python
G = self.Graph(dododod, multigraph_input=True)
```

**Verification:**
```python
assert list(G.edges(keys=True, data=True)) == multiple_edge
```

### Step 8: Assign G = self.Graph(...)

```python
G = self.Graph(dododod, multigraph_input=None)
```

**Verification:**
```python
assert list(G.edges(keys=True, data=True)) == multiple_edge
```

### Step 9: Assign G = self.Graph(...)

```python
G = self.Graph(dododod, multigraph_input=False)
```

**Verification:**
```python
assert list(G.edges(keys=True, data=True)) == single_edge
```

### Step 10: Assign G = self.Graph(...)

```python
G = self.Graph(dododod, multigraph_input=True)
```

### Step 11: Assign H = self.Graph(...)

```python
H = self.Graph(nx.to_dict_of_dicts(G))
```

**Verification:**
```python
assert nx.is_isomorphic(G, H) is True
```

### Step 12: Assign H = self.Graph(...)

```python
H = self.Graph(nx.to_dict_of_dicts(G), multigraph_input=mgi)
```

**Verification:**
```python
assert nx.is_isomorphic(G, H) == mgi
```


## Complete Example

```python
# Workflow
edata0 = {'w': 200, 's': 'foo'}
edata1 = {'w': 201, 's': 'bar'}
keydict = {0: edata0, 1: edata1}
dododod = {'a': {'b': keydict}}
multiple_edge = [('a', 'b', 0, edata0), ('a', 'b', 1, edata1)]
single_edge = [('a', 'b', 0, keydict)]
G = self.Graph(dododod, multigraph_input=True)
assert list(G.edges(keys=True, data=True)) == multiple_edge
G = self.Graph(dododod, multigraph_input=None)
assert list(G.edges(keys=True, data=True)) == multiple_edge
G = self.Graph(dododod, multigraph_input=False)
assert list(G.edges(keys=True, data=True)) == single_edge
G = self.Graph(dododod, multigraph_input=True)
H = self.Graph(nx.to_dict_of_dicts(G))
assert nx.is_isomorphic(G, H) is True
for mgi in [True, False]:
    H = self.Graph(nx.to_dict_of_dicts(G), multigraph_input=mgi)
    assert nx.is_isomorphic(G, H) == mgi
```

## Next Steps


---

*Source: test_multigraph.py:203 | Complexity: Advanced | Last updated: 2026-06-02*
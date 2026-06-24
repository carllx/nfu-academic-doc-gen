# How To: Node Attributes

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: Tests that node contraction preserves node attributes.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.utils`

**Setup Required:**
```python
# Fixtures: store_contraction_as, copy, selfloops
```

## Step-by-Step Guide

### Step 1: 'Tests that node contraction preserves node attributes.'

```python
'Tests that node contraction preserves node attributes.'
```

**Verification:**
```python
assert nx.is_isomorphic(actual, expected)
```

### Step 2: Assign G = nx.cycle_graph(...)

```python
G = nx.cycle_graph(4)
```

**Verification:**
```python
assert actual.nodes(data=True) == expected.nodes(data=True)
```

### Step 3: Assign unknown = 'bar'

```python
G.nodes[0]['foo'] = 'bar'
```

**Verification:**
```python
assert actual is G
```

### Step 4: Assign unknown = 'xyzzy'

```python
G.nodes[1]['baz'] = 'xyzzy'
```

### Step 5: Assign actual = nx.contracted_nodes(...)

```python
actual = nx.contracted_nodes(G, 0, 1, copy=copy, self_loops=selfloops, store_contraction_as=store_contraction_as)
```

### Step 6: Assign expected = nx.complete_graph(...)

```python
expected = nx.complete_graph(3)
```

### Step 7: Assign expected = nx.relabel_nodes(...)

```python
expected = nx.relabel_nodes(expected, {1: 2, 2: 3})
```

### Step 8: Assign unknown = 'bar'

```python
expected.nodes[0]['foo'] = 'bar'
```

**Verification:**
```python
assert nx.is_isomorphic(actual, expected)
```

### Step 9: Call expected.add_edge()

```python
expected.add_edge(0, 0)
```

### Step 10: Assign cdict = value

```python
cdict = {1: {'baz': 'xyzzy'}}
```

### Step 11: Call unknown.update()

```python
expected.nodes[0].update({'foo': 'bar', store_contraction_as: cdict})
```

**Verification:**
```python
assert actual is G
```


## Complete Example

```python
# Setup
# Fixtures: store_contraction_as, copy, selfloops

# Workflow
'Tests that node contraction preserves node attributes.'
G = nx.cycle_graph(4)
G.nodes[0]['foo'] = 'bar'
G.nodes[1]['baz'] = 'xyzzy'
actual = nx.contracted_nodes(G, 0, 1, copy=copy, self_loops=selfloops, store_contraction_as=store_contraction_as)
expected = nx.complete_graph(3)
expected = nx.relabel_nodes(expected, {1: 2, 2: 3})
expected.nodes[0]['foo'] = 'bar'
if selfloops:
    expected.add_edge(0, 0)
if store_contraction_as:
    cdict = {1: {'baz': 'xyzzy'}}
    expected.nodes[0].update({'foo': 'bar', store_contraction_as: cdict})
assert nx.is_isomorphic(actual, expected)
assert actual.nodes(data=True) == expected.nodes(data=True)
if not copy:
    assert actual is G
```

## Next Steps


---

*Source: test_contraction.py:401 | Complexity: Advanced | Last updated: 2026-06-02*
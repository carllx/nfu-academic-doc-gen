# How To: As Graph Coverage

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Add test coverage for some hard-to-hit branches.

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx`
- `networkx.generators.internet_as_graphs`


## Step-by-Step Guide

### Step 1: 'Add test coverage for some hard-to-hit branches.'

```python
'Add test coverage for some hard-to-hit branches.'
```

**Verification:**
```python
assert len(G) == 20
```

### Step 2: Assign GG = AS_graph_generator(...)

```python
GG = AS_graph_generator(20, seed=42)
```

**Verification:**
```python
assert len(GG.nodes['M']) == 3
```

### Step 3: Assign G = GG.generate(...)

```python
G = GG.generate()
```

**Verification:**
```python
assert len(GG.nodes['CP']) == 1
```

### Step 4: Assign m_node = nx.utils.arbitrary_element(...)

```python
m_node = nx.utils.arbitrary_element(GG.nodes['M'])
```

**Verification:**
```python
assert all((u in G[v] for u in GG.nodes['M'] for v in GG.nodes['M'] if u != v))
```

### Step 5: Assign cp_node = nx.utils.arbitrary_element(...)

```python
cp_node = nx.utils.arbitrary_element(GG.nodes['CP'])
```

**Verification:**
```python
assert not GG.add_m_peering_link(m_node, 'M')
```

### Step 6: Assign unknown = set(...)

```python
GG.customers[m_node] = set(GG.nodes['M'])
```

**Verification:**
```python
assert not GG.add_m_peering_link(m_node, 'M')
```

### Step 7: Assign unknown = set(...)

```python
GG.providers[cp_node] = set()
```

**Verification:**
```python
assert not GG.add_cp_peering_link(cp_node, 'CP')
```

### Step 8: Call GG.add_node()

```python
GG.add_node(m_node, 'M', 1, 2, 0.5)
```

**Verification:**
```python
assert not GG.add_cp_peering_link(cp_node, 'M')
```


## Complete Example

```python
# Workflow
'Add test coverage for some hard-to-hit branches.'
GG = AS_graph_generator(20, seed=42)
G = GG.generate()
assert len(G) == 20
assert len(GG.nodes['M']) == 3
m_node = nx.utils.arbitrary_element(GG.nodes['M'])
assert len(GG.nodes['CP']) == 1
cp_node = nx.utils.arbitrary_element(GG.nodes['CP'])
assert all((u in G[v] for u in GG.nodes['M'] for v in GG.nodes['M'] if u != v))
assert not GG.add_m_peering_link(m_node, 'M')
GG.customers[m_node] = set(GG.nodes['M'])
assert not GG.add_m_peering_link(m_node, 'M')
GG.providers[cp_node] = set()
assert not GG.add_cp_peering_link(cp_node, 'CP')
assert not GG.add_cp_peering_link(cp_node, 'M')
GG.add_node(m_node, 'M', 1, 2, 0.5)
assert len(GG.nodes['M']) == 3
```

## Next Steps


---

*Source: test_internet_as_graphs.py:184 | Complexity: Advanced | Last updated: 2026-06-02*
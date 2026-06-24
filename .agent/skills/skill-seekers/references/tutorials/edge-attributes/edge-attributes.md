# How To: Edge Attributes

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: Tests that node contraction preserves edge attributes.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.utils`

**Setup Required:**
```python
# Fixtures: store_contraction_as
```

## Step-by-Step Guide

### Step 1: 'Tests that node contraction preserves edge attributes.'

```python
'Tests that node contraction preserves edge attributes.'
```

**Verification:**
```python
assert H.edges['src1', 'dest']['value'] == 'src1-->dest'
```

### Step 2: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph([('src1', 'dest'), ('src2', 'dest')])
```

**Verification:**
```python
assert H.edges['src1', 'dest'][store_contraction_as]['src2', 'dest']['value'] == 'src2-->dest'
```

### Step 3: Assign unknown = 'src1-->dest'

```python
G['src1']['dest']['value'] = 'src1-->dest'
```

**Verification:**
```python
assert store_contraction_as not in H.edges['src1', 'dest']
```

### Step 4: Assign unknown = 'src2-->dest'

```python
G['src2']['dest']['value'] = 'src2-->dest'
```

**Verification:**
```python
assert len(H.edges(('src1', 'dest'))) == 2
```

### Step 5: Assign H = nx.contracted_nodes(...)

```python
H = nx.contracted_nodes(G, 'src1', 'src2', store_contraction_as=store_contraction_as)
```

**Verification:**
```python
assert H.edges['src1', 'dest', 0]['value'] == 'src1-->dest'
```

### Step 6: Assign G = nx.MultiDiGraph(...)

```python
G = nx.MultiDiGraph(G)
```

**Verification:**
```python
assert H.edges['src1', 'dest', 1]['value'] == 'src2-->dest'
```

### Step 7: Assign H = nx.contracted_nodes(...)

```python
H = nx.contracted_nodes(G, 'src1', 'src2', store_contraction_as=store_contraction_as)
```

**Verification:**
```python
assert len(H.edges(('src1', 'dest'))) == 2
```


## Complete Example

```python
# Setup
# Fixtures: store_contraction_as

# Workflow
'Tests that node contraction preserves edge attributes.'
G = nx.DiGraph([('src1', 'dest'), ('src2', 'dest')])
G['src1']['dest']['value'] = 'src1-->dest'
G['src2']['dest']['value'] = 'src2-->dest'
H = nx.contracted_nodes(G, 'src1', 'src2', store_contraction_as=store_contraction_as)
assert H.edges['src1', 'dest']['value'] == 'src1-->dest'
if store_contraction_as:
    assert H.edges['src1', 'dest'][store_contraction_as]['src2', 'dest']['value'] == 'src2-->dest'
else:
    assert store_contraction_as not in H.edges['src1', 'dest']
G = nx.MultiDiGraph(G)
H = nx.contracted_nodes(G, 'src1', 'src2', store_contraction_as=store_contraction_as)
assert len(H.edges(('src1', 'dest'))) == 2
assert H.edges['src1', 'dest', 0]['value'] == 'src1-->dest'
assert H.edges['src1', 'dest', 1]['value'] == 'src2-->dest'
```

## Next Steps


---

*Source: test_contraction.py:435 | Complexity: Intermediate | Last updated: 2026-06-02*
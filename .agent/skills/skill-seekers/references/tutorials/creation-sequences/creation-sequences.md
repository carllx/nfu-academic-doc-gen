# How To: Creation Sequences

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test creation sequences

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms.threshold`


## Step-by-Step Guide

### Step 1: Assign deg = value

```python
deg = [3, 2, 2, 1]
```

**Verification:**
```python
assert ''.join(cs0) == 'ddid'
```

### Step 2: Assign G = nx.generators.havel_hakimi_graph(...)

```python
G = nx.generators.havel_hakimi_graph(deg)
```

**Verification:**
```python
assert cs1 == [(1, 'd'), (2, 'd'), (3, 'i'), (0, 'd')]
```

### Step 3: Assign cs0 = nxt.creation_sequence(...)

```python
cs0 = nxt.creation_sequence(deg)
```

**Verification:**
```python
assert cs2 == [2, 1, 1]
```

### Step 4: Assign H0 = nxt.threshold_graph(...)

```python
H0 = nxt.threshold_graph(cs0)
```

**Verification:**
```python
assert ''.join(nxt.uncompact(cs2)) == 'ddid'
```

### Step 5: Assign cs1 = nxt.creation_sequence(...)

```python
cs1 = nxt.creation_sequence(deg, with_labels=True)
```

**Verification:**
```python
assert nx.could_be_isomorphic(H0, G)
```

### Step 6: Assign H1 = nxt.threshold_graph(...)

```python
H1 = nxt.threshold_graph(cs1)
```

**Verification:**
```python
assert nx.could_be_isomorphic(H0, H1)
```

### Step 7: Assign cs2 = nxt.creation_sequence(...)

```python
cs2 = nxt.creation_sequence(deg, compact=True)
```

**Verification:**
```python
assert nx.could_be_isomorphic(H0, H2)
```

### Step 8: Assign H2 = nxt.threshold_graph(...)

```python
H2 = nxt.threshold_graph(cs2)
```

**Verification:**
```python
assert cs2 == [2, 1, 1]
```

### Step 9: Call nxt.creation_sequence()

```python
nxt.creation_sequence(deg, with_labels=True, compact=True)
```


## Complete Example

```python
# Workflow
deg = [3, 2, 2, 1]
G = nx.generators.havel_hakimi_graph(deg)
with pytest.raises(ValueError):
    nxt.creation_sequence(deg, with_labels=True, compact=True)
cs0 = nxt.creation_sequence(deg)
H0 = nxt.threshold_graph(cs0)
assert ''.join(cs0) == 'ddid'
cs1 = nxt.creation_sequence(deg, with_labels=True)
H1 = nxt.threshold_graph(cs1)
assert cs1 == [(1, 'd'), (2, 'd'), (3, 'i'), (0, 'd')]
cs2 = nxt.creation_sequence(deg, compact=True)
H2 = nxt.threshold_graph(cs2)
assert cs2 == [2, 1, 1]
assert ''.join(nxt.uncompact(cs2)) == 'ddid'
assert nx.could_be_isomorphic(H0, G)
assert nx.could_be_isomorphic(H0, H1)
assert nx.could_be_isomorphic(H0, H2)
```

## Next Steps


---

*Source: test_threshold.py:39 | Complexity: Advanced | Last updated: 2026-06-02*
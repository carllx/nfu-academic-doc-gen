# How To: Parse Edgelist

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test parse edgelist

## Prerequisites

**Required Modules:**
- `io`
- `textwrap`
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign lines = value

```python
lines = ['1;2', '2 3', '3 4']
```

**Verification:**
```python
assert list(G.edges()) == [(2, 3), (3, 4)]
```

### Step 2: Assign G = nx.parse_edgelist(...)

```python
G = nx.parse_edgelist(lines, nodetype=int)
```

**Verification:**
```python
assert list(G.edges()) == [(2, 3), (3, 4)]
```

### Step 3: Assign lines = value

```python
lines = ['1 2', '2 3', '3 4']
```

### Step 4: Call nx.parse_edgelist()

```python
nx.parse_edgelist(lines, nodetype='nope')
```

### Step 5: Assign lines = value

```python
lines = ['1 2 3', '2 3', '3 4']
```

### Step 6: Call nx.parse_edgelist()

```python
nx.parse_edgelist(lines, nodetype=int)
```

### Step 7: Assign lines = value

```python
lines = ['1 2 3', '2 3 27', '3 4 3.0']
```

### Step 8: Call nx.parse_edgelist()

```python
nx.parse_edgelist(lines, nodetype=int, data=(('weight', float), ('capacity', int)))
```

### Step 9: Assign lines = value

```python
lines = ["1 2 't1'", "2 3 't3'", "3 4 't3'"]
```

### Step 10: Call nx.parse_edgelist()

```python
nx.parse_edgelist(lines, nodetype=int, data=(('weight', float),))
```


## Complete Example

```python
# Workflow
lines = ['1;2', '2 3', '3 4']
G = nx.parse_edgelist(lines, nodetype=int)
assert list(G.edges()) == [(2, 3), (3, 4)]
with pytest.raises(TypeError, match='Failed to convert nodes'):
    lines = ['1 2', '2 3', '3 4']
    nx.parse_edgelist(lines, nodetype='nope')
with pytest.raises(TypeError, match='Failed to convert edge data'):
    lines = ['1 2 3', '2 3', '3 4']
    nx.parse_edgelist(lines, nodetype=int)
with pytest.raises(IndexError, match='not the same length'):
    lines = ['1 2 3', '2 3 27', '3 4 3.0']
    nx.parse_edgelist(lines, nodetype=int, data=(('weight', float), ('capacity', int)))
with pytest.raises(TypeError, match='Failed to convert'):
    lines = ["1 2 't1'", "2 3 't3'", "3 4 't3'"]
    nx.parse_edgelist(lines, nodetype=int, data=(('weight', float),))
```

## Next Steps


---

*Source: test_edgelist.py:142 | Complexity: Advanced | Last updated: 2026-06-02*
# How To: Complete Bipartite

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test complete bipartite

## Prerequisites

**Required Modules:**
- `io`
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign G = nx.complete_bipartite_graph(...)

```python
G = nx.complete_bipartite_graph(6, 9)
```

**Verification:**
```python
assert result.getvalue() == expected
```

### Step 2: Assign result = BytesIO(...)

```python
result = BytesIO()
```

### Step 3: Call nx.write_sparse6()

```python
nx.write_sparse6(G, result)
```

### Step 4: Assign expected = value

```python
expected = b'>>sparse6<<:Nk' + b'?G`cJ' * 9 + b'\n'
```

**Verification:**
```python
assert result.getvalue() == expected
```


## Complete Example

```python
# Workflow
G = nx.complete_bipartite_graph(6, 9)
result = BytesIO()
nx.write_sparse6(G, result)
expected = b'>>sparse6<<:Nk' + b'?G`cJ' * 9 + b'\n'
assert result.getvalue() == expected
```

## Next Steps


---

*Source: test_sparse6.py:136 | Complexity: Intermediate | Last updated: 2026-06-02*
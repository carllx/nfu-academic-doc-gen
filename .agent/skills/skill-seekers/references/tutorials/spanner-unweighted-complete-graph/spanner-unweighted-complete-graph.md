# How To: Spanner Unweighted Complete Graph

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test spanner construction on a complete unweighted graph.

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: 'Test spanner construction on a complete unweighted graph.'

```python
'Test spanner construction on a complete unweighted graph.'
```

### Step 2: Assign G = nx.complete_graph(...)

```python
G = nx.complete_graph(20)
```

### Step 3: Assign spanner = nx.spanner(...)

```python
spanner = nx.spanner(G, 4, seed=_seed)
```

### Step 4: Call _test_spanner()

```python
_test_spanner(G, spanner, 4)
```

### Step 5: Assign spanner = nx.spanner(...)

```python
spanner = nx.spanner(G, 10, seed=_seed)
```

### Step 6: Call _test_spanner()

```python
_test_spanner(G, spanner, 10)
```


## Complete Example

```python
# Workflow
'Test spanner construction on a complete unweighted graph.'
G = nx.complete_graph(20)
spanner = nx.spanner(G, 4, seed=_seed)
_test_spanner(G, spanner, 4)
spanner = nx.spanner(G, 10, seed=_seed)
_test_spanner(G, spanner, 10)
```

## Next Steps


---

*Source: test_sparsifiers.py:77 | Complexity: Intermediate | Last updated: 2026-06-02*
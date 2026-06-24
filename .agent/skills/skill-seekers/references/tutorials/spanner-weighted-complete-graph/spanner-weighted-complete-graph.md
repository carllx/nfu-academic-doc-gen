# How To: Spanner Weighted Complete Graph

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test spanner construction on a complete weighted graph.

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: 'Test spanner construction on a complete weighted graph.'

```python
'Test spanner construction on a complete weighted graph.'
```

### Step 2: Assign G = nx.complete_graph(...)

```python
G = nx.complete_graph(20)
```

### Step 3: Call _assign_random_weights()

```python
_assign_random_weights(G, seed=_seed)
```

### Step 4: Assign spanner = nx.spanner(...)

```python
spanner = nx.spanner(G, 4, weight='weight', seed=_seed)
```

### Step 5: Call _test_spanner()

```python
_test_spanner(G, spanner, 4, weight='weight')
```

### Step 6: Assign spanner = nx.spanner(...)

```python
spanner = nx.spanner(G, 10, weight='weight', seed=_seed)
```

### Step 7: Call _test_spanner()

```python
_test_spanner(G, spanner, 10, weight='weight')
```


## Complete Example

```python
# Workflow
'Test spanner construction on a complete weighted graph.'
G = nx.complete_graph(20)
_assign_random_weights(G, seed=_seed)
spanner = nx.spanner(G, 4, weight='weight', seed=_seed)
_test_spanner(G, spanner, 4, weight='weight')
spanner = nx.spanner(G, 10, weight='weight', seed=_seed)
_test_spanner(G, spanner, 10, weight='weight')
```

## Next Steps


---

*Source: test_sparsifiers.py:88 | Complexity: Intermediate | Last updated: 2026-06-02*
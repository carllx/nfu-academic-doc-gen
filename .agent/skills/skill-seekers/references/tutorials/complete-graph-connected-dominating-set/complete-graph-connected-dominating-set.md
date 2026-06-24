# How To: Complete Graph Connected Dominating Set

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: test complete graph connected dominating set

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign K5 = nx.complete_graph(...)

```python
K5 = nx.complete_graph(5)
```

**Verification:**
```python
assert 1 == len(nx.connected_dominating_set(K5))
```

### Step 2: Assign K7 = nx.complete_graph(...)

```python
K7 = nx.complete_graph(7)
```

**Verification:**
```python
assert 1 == len(nx.connected_dominating_set(K7))
```


## Complete Example

```python
# Workflow
K5 = nx.complete_graph(5)
assert 1 == len(nx.connected_dominating_set(K5))
K7 = nx.complete_graph(7)
assert 1 == len(nx.connected_dominating_set(K7))
```

## Next Steps


---

*Source: test_dominating.py:80 | Complexity: Beginner | Last updated: 2026-06-02*
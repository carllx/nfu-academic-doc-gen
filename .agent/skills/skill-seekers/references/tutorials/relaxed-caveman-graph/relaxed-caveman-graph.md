# How To: Relaxed Caveman Graph

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test relaxed caveman graph

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = nx.relaxed_caveman_graph(...)

```python
G = nx.relaxed_caveman_graph(4, 3, 0)
```

**Verification:**
```python
assert len(G) == 12
```

### Step 2: Assign G = nx.relaxed_caveman_graph(...)

```python
G = nx.relaxed_caveman_graph(4, 3, 1)
```

**Verification:**
```python
assert len(G) == 12
```

### Step 3: Assign G = nx.relaxed_caveman_graph(...)

```python
G = nx.relaxed_caveman_graph(4, 3, 0.5)
```

**Verification:**
```python
assert len(G) == 12
```

### Step 4: Assign G = nx.relaxed_caveman_graph(...)

```python
G = nx.relaxed_caveman_graph(4, 3, 0.5, seed=42)
```

**Verification:**
```python
assert len(G) == 12
```


## Complete Example

```python
# Workflow
G = nx.relaxed_caveman_graph(4, 3, 0)
assert len(G) == 12
G = nx.relaxed_caveman_graph(4, 3, 1)
assert len(G) == 12
G = nx.relaxed_caveman_graph(4, 3, 0.5)
assert len(G) == 12
G = nx.relaxed_caveman_graph(4, 3, 0.5, seed=42)
assert len(G) == 12
```

## Next Steps


---

*Source: test_community.py:85 | Complexity: Intermediate | Last updated: 2026-06-02*
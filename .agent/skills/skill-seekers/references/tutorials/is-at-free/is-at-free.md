# How To: Is At Free

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test is at free

## Prerequisites

**Required Modules:**
- `networkx`


## Step-by-Step Guide

### Step 1: Assign is_at_free = value

```python
is_at_free = nx.asteroidal.is_at_free
```

**Verification:**
```python
assert not is_at_free(cycle)
```

### Step 2: Assign cycle = nx.cycle_graph(...)

```python
cycle = nx.cycle_graph(6)
```

**Verification:**
```python
assert is_at_free(path)
```

### Step 3: Assign path = nx.path_graph(...)

```python
path = nx.path_graph(6)
```

**Verification:**
```python
assert is_at_free(small_graph)
```

### Step 4: Assign small_graph = nx.complete_graph(...)

```python
small_graph = nx.complete_graph(2)
```

**Verification:**
```python
assert not is_at_free(petersen)
```

### Step 5: Assign petersen = nx.petersen_graph(...)

```python
petersen = nx.petersen_graph()
```

**Verification:**
```python
assert is_at_free(clique)
```

### Step 6: Assign clique = nx.complete_graph(...)

```python
clique = nx.complete_graph(6)
```

**Verification:**
```python
assert not is_at_free(line_clique)
```

### Step 7: Assign line_clique = nx.line_graph(...)

```python
line_clique = nx.line_graph(clique)
```

**Verification:**
```python
assert not is_at_free(line_clique)
```


## Complete Example

```python
# Workflow
is_at_free = nx.asteroidal.is_at_free
cycle = nx.cycle_graph(6)
assert not is_at_free(cycle)
path = nx.path_graph(6)
assert is_at_free(path)
small_graph = nx.complete_graph(2)
assert is_at_free(small_graph)
petersen = nx.petersen_graph()
assert not is_at_free(petersen)
clique = nx.complete_graph(6)
assert is_at_free(clique)
line_clique = nx.line_graph(clique)
assert not is_at_free(line_clique)
```

## Next Steps


---

*Source: test_asteroidal.py:4 | Complexity: Intermediate | Last updated: 2026-06-02*
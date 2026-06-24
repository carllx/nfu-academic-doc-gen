# How To: Pseudo Sequence

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test pseudo sequence

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.generators`


## Step-by-Step Guide

### Step 1: Assign seq = value

```python
seq = [1000, 3, 3, 3, 3, 2, 2, 2, 1, 1]
```

**Verification:**
```python
assert nx.is_pseudographical(seq)
```

### Step 2: Assign seq = value

```python
seq = [1000, 3, 3, 3, 3, 2, 2, 2, 1, 1, 1]
```

**Verification:**
```python
assert not nx.is_pseudographical(seq)
```

### Step 3: Assign seq = value

```python
seq = [1000, 3, 3, 3, 3, 2, 2, -2, 1, 1]
```

**Verification:**
```python
assert not nx.is_pseudographical(seq)
```

### Step 4: Assign seq = value

```python
seq = [1, 1, 1.1, 1]
```

**Verification:**
```python
assert not nx.is_pseudographical(seq)
```

### Step 5: Assign seq = value

```python
seq = [1, 1, 'rer', 1]
```

**Verification:**
```python
assert not nx.is_pseudographical(seq)
```


## Complete Example

```python
# Workflow
seq = [1000, 3, 3, 3, 3, 2, 2, 2, 1, 1]
assert nx.is_pseudographical(seq)
seq = [1000, 3, 3, 3, 3, 2, 2, 2, 1, 1, 1]
assert not nx.is_pseudographical(seq)
seq = [1000, 3, 3, 3, 3, 2, 2, -2, 1, 1]
assert not nx.is_pseudographical(seq)
seq = [1, 1, 1.1, 1]
assert not nx.is_pseudographical(seq)
seq = [1, 1, 'rer', 1]
assert not nx.is_pseudographical(seq)
```

## Next Steps


---

*Source: test_graphical.py:136 | Complexity: Intermediate | Last updated: 2026-06-02*
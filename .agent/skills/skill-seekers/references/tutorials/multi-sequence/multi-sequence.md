# How To: Multi Sequence

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multi sequence

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
assert not nx.is_multigraphical(seq)
```

### Step 2: Assign seq = value

```python
seq = [6, 5, 4, 4, 2, 1, 1, 1]
```

**Verification:**
```python
assert nx.is_multigraphical(seq)
```

### Step 3: Assign seq = value

```python
seq = [6, 5, 4, -4, 2, 1, 1, 1]
```

**Verification:**
```python
assert not nx.is_multigraphical(seq)
```

### Step 4: Assign seq = value

```python
seq = [1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4]
```

**Verification:**
```python
assert not nx.is_multigraphical(seq)
```

### Step 5: Assign seq = value

```python
seq = [1, 1, 1.1, 1]
```

**Verification:**
```python
assert not nx.is_multigraphical(seq)
```

### Step 6: Assign seq = value

```python
seq = [1, 1, 'rer', 1]
```

**Verification:**
```python
assert not nx.is_multigraphical(seq)
```


## Complete Example

```python
# Workflow
seq = [1000, 3, 3, 3, 3, 2, 2, 2, 1, 1]
assert not nx.is_multigraphical(seq)
seq = [6, 5, 4, 4, 2, 1, 1, 1]
assert nx.is_multigraphical(seq)
seq = [6, 5, 4, -4, 2, 1, 1, 1]
assert not nx.is_multigraphical(seq)
seq = [1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4]
assert not nx.is_multigraphical(seq)
seq = [1, 1, 1.1, 1]
assert not nx.is_multigraphical(seq)
seq = [1, 1, 'rer', 1]
assert not nx.is_multigraphical(seq)
```

## Next Steps


---

*Source: test_graphical.py:116 | Complexity: Intermediate | Last updated: 2026-06-02*
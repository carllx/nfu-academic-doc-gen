# How To: Small Directed Sequences

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test small directed sequences

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.generators`


## Step-by-Step Guide

### Step 1: Assign dout = value

```python
dout = [5, 3, 3, 3, 3, 2, 2, 2, 1, 1, 1]
```

**Verification:**
```python
assert nx.is_digraphical(din, dout)
```

### Step 2: Assign din = value

```python
din = [3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 1]
```

**Verification:**
```python
assert not nx.is_digraphical(din, dout)
```

### Step 3: Assign dout = value

```python
dout = [1000, 3, 3, 3, 3, 2, 2, 2, 1, 1, 1]
```

**Verification:**
```python
assert nx.is_digraphical(din, dout)
```

### Step 4: Assign din = value

```python
din = [103, 102, 102, 102, 102, 102, 102, 102, 102, 102]
```

**Verification:**
```python
assert not nx.is_digraphical(din, dout)
```

### Step 5: Assign dout = value

```python
dout = [1, 1, 1, 1, 1, 2, 2, 2, 3, 4]
```

**Verification:**
```python
assert not nx.is_digraphical(din, dout)
```

### Step 6: Assign din = value

```python
din = [2, 2, 2, 2, 2, 2, 2, 2, 1, 1]
```

**Verification:**
```python
assert not nx.is_digraphical(din, dout)
```

### Step 7: Assign din = value

```python
din = [2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1]
```

**Verification:**
```python
assert not nx.is_digraphical(din, dout)
```

### Step 8: Assign din = value

```python
din = [2, 2, 2, -2, 2, 2, 2, 2, 1, 1, 4]
```

**Verification:**
```python
assert not nx.is_digraphical(din, dout)
```

### Step 9: Assign din, dout = value

```python
din = dout = [1, 1, 1.1, 1]
```

**Verification:**
```python
assert not nx.is_digraphical(din, dout)
```

### Step 10: Assign din, dout = value

```python
din = dout = [1, 1, 'rer', 1]
```

**Verification:**
```python
assert not nx.is_digraphical(din, dout)
```


## Complete Example

```python
# Workflow
dout = [5, 3, 3, 3, 3, 2, 2, 2, 1, 1, 1]
din = [3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 1]
assert nx.is_digraphical(din, dout)
dout = [1000, 3, 3, 3, 3, 2, 2, 2, 1, 1, 1]
din = [103, 102, 102, 102, 102, 102, 102, 102, 102, 102]
assert not nx.is_digraphical(din, dout)
dout = [1, 1, 1, 1, 1, 2, 2, 2, 3, 4]
din = [2, 2, 2, 2, 2, 2, 2, 2, 1, 1]
assert nx.is_digraphical(din, dout)
din = [2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1]
assert not nx.is_digraphical(din, dout)
din = [2, 2, 2, -2, 2, 2, 2, 2, 1, 1, 4]
assert not nx.is_digraphical(din, dout)
din = dout = [1, 1, 1.1, 1]
assert not nx.is_digraphical(din, dout)
din = dout = [1, 1, 'rer', 1]
assert not nx.is_digraphical(din, dout)
```

## Next Steps


---

*Source: test_graphical.py:91 | Complexity: Advanced | Last updated: 2026-06-02*
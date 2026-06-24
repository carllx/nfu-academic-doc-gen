# How To: Is Valid Directed Joint Degree

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test is valid directed joint degree

## Prerequisites

**Required Modules:**
- `time`
- `networkx.algorithms.assortativity`
- `networkx.generators`
- `networkx.generators.joint_degree_seq`


## Step-by-Step Guide

### Step 1: Assign in_degrees = value

```python
in_degrees = [0, 1, 1, 2]
```

**Verification:**
```python
assert is_valid_directed_joint_degree(in_degrees, out_degrees, nkk)
```

### Step 2: Assign out_degrees = value

```python
out_degrees = [1, 1, 1, 1]
```

**Verification:**
```python
assert not is_valid_directed_joint_degree(in_degrees, out_degrees, nkk)
```

### Step 3: Assign nkk = value

```python
nkk = {1: {1: 2, 2: 2}}
```

**Verification:**
```python
assert not is_valid_directed_joint_degree(in_degrees, out_degrees, nkk)
```

### Step 4: Assign nkk = value

```python
nkk = {1: {1: 1.5, 2: 2.5}}
```

**Verification:**
```python
assert not is_valid_directed_joint_degree(in_degrees, out_degrees, nkk)
```

### Step 5: Assign nkk = value

```python
nkk = {1: {1: 2, 2: 1}}
```

**Verification:**
```python
assert not is_valid_directed_joint_degree(in_degrees, out_degrees, nkk)
```

### Step 6: Assign out_degrees = value

```python
out_degrees = [1, 1, 1]
```

### Step 7: Assign nkk = value

```python
nkk = {1: {1: 2, 2: 2}}
```

**Verification:**
```python
assert not is_valid_directed_joint_degree(in_degrees, out_degrees, nkk)
```

### Step 8: Assign in_degrees = value

```python
in_degrees = [0, 1, 2]
```

**Verification:**
```python
assert not is_valid_directed_joint_degree(in_degrees, out_degrees, nkk)
```


## Complete Example

```python
# Workflow
in_degrees = [0, 1, 1, 2]
out_degrees = [1, 1, 1, 1]
nkk = {1: {1: 2, 2: 2}}
assert is_valid_directed_joint_degree(in_degrees, out_degrees, nkk)
nkk = {1: {1: 1.5, 2: 2.5}}
assert not is_valid_directed_joint_degree(in_degrees, out_degrees, nkk)
nkk = {1: {1: 2, 2: 1}}
assert not is_valid_directed_joint_degree(in_degrees, out_degrees, nkk)
out_degrees = [1, 1, 1]
nkk = {1: {1: 2, 2: 2}}
assert not is_valid_directed_joint_degree(in_degrees, out_degrees, nkk)
in_degrees = [0, 1, 2]
assert not is_valid_directed_joint_degree(in_degrees, out_degrees, nkk)
```

## Next Steps


---

*Source: test_joint_degree_seq.py:82 | Complexity: Advanced | Last updated: 2026-06-02*
# How To: Is Valid Joint Degree

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Tests for conditions that invalidate a joint degree dict

## Prerequisites

**Required Modules:**
- `time`
- `networkx.algorithms.assortativity`
- `networkx.generators`
- `networkx.generators.joint_degree_seq`


## Step-by-Step Guide

### Step 1: 'Tests for conditions that invalidate a joint degree dict'

```python
'Tests for conditions that invalidate a joint degree dict'
```

**Verification:**
```python
assert is_valid_joint_degree(joint_degrees)
```

### Step 2: Assign joint_degrees = value

```python
joint_degrees = {1: {4: 1}, 2: {2: 2, 3: 2, 4: 2}, 3: {2: 2, 4: 1}, 4: {1: 1, 2: 2, 3: 1}}
```

**Verification:**
```python
assert not is_valid_joint_degree(joint_degrees_1)
```

### Step 3: Assign joint_degrees_1 = value

```python
joint_degrees_1 = {1: {4: 1.5}, 2: {2: 2, 3: 2, 4: 2}, 3: {2: 2, 4: 1}, 4: {1: 1.5, 2: 2, 3: 1}}
```

**Verification:**
```python
assert not is_valid_joint_degree(joint_degrees_2)
```

### Step 4: Assign joint_degrees_2 = value

```python
joint_degrees_2 = {1: {4: 1}, 2: {2: 2, 3: 2, 4: 3}, 3: {2: 2, 4: 1}, 4: {1: 1, 2: 3, 3: 1}}
```

**Verification:**
```python
assert not is_valid_joint_degree(joint_degrees_3)
```

### Step 5: Assign joint_degrees_3 = value

```python
joint_degrees_3 = {1: {4: 2}, 2: {2: 2, 3: 2, 4: 2}, 3: {2: 2, 4: 1}, 4: {1: 2, 2: 2, 3: 1}}
```

**Verification:**
```python
assert not is_valid_joint_degree(joint_degrees_5)
```

### Step 6: Assign joint_degrees_5 = value

```python
joint_degrees_5 = {1: {1: 9}}
```

**Verification:**
```python
assert not is_valid_joint_degree(joint_degrees_5)
```


## Complete Example

```python
# Workflow
'Tests for conditions that invalidate a joint degree dict'
joint_degrees = {1: {4: 1}, 2: {2: 2, 3: 2, 4: 2}, 3: {2: 2, 4: 1}, 4: {1: 1, 2: 2, 3: 1}}
assert is_valid_joint_degree(joint_degrees)
joint_degrees_1 = {1: {4: 1.5}, 2: {2: 2, 3: 2, 4: 2}, 3: {2: 2, 4: 1}, 4: {1: 1.5, 2: 2, 3: 1}}
assert not is_valid_joint_degree(joint_degrees_1)
joint_degrees_2 = {1: {4: 1}, 2: {2: 2, 3: 2, 4: 3}, 3: {2: 2, 4: 1}, 4: {1: 1, 2: 3, 3: 1}}
assert not is_valid_joint_degree(joint_degrees_2)
joint_degrees_3 = {1: {4: 2}, 2: {2: 2, 3: 2, 4: 2}, 3: {2: 2, 4: 1}, 4: {1: 2, 2: 2, 3: 1}}
assert not is_valid_joint_degree(joint_degrees_3)
joint_degrees_5 = {1: {1: 9}}
assert not is_valid_joint_degree(joint_degrees_5)
```

## Next Steps


---

*Source: test_joint_degree_seq.py:13 | Complexity: Intermediate | Last updated: 2026-06-02*
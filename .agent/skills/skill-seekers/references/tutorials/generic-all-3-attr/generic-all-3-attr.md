# How To: Generic All 3 Attr

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test generic all 3 attr

## Prerequisites

**Required Modules:**
- `math`
- `operator`
- `networkx`
- `networkx.algorithms.isomorphism`


## Step-by-Step Guide

### Step 1: Assign gm = self.GM(...)

```python
gm = self.GM(self.g1, self.g2, edge_match=self.emg2)
```

**Verification:**
```python
assert not gm.is_isomorphic()
```

### Step 2: Assign unknown = 0

```python
self.g2.edges['C', 'D', 0]['weight'] = 0
```

**Verification:**
```python
assert gm.is_isomorphic()
```

### Step 3: Assign unknown = 1

```python
self.g2.edges['C', 'D', 1]['weight'] = 1
```

### Step 4: Assign unknown = 0.35

```python
self.g2.edges['C', 'D', 1]['size'] = 0.35
```

**Verification:**
```python
assert gm.is_isomorphic()
```


## Complete Example

```python
# Workflow
gm = self.GM(self.g1, self.g2, edge_match=self.emg2)
assert not gm.is_isomorphic()
self.g2.edges['C', 'D', 0]['weight'] = 0
self.g2.edges['C', 'D', 1]['weight'] = 1
self.g2.edges['C', 'D', 1]['size'] = 0.35
assert gm.is_isomorphic()
```

## Next Steps


---

*Source: test_vf2userfunc.py:181 | Complexity: Intermediate | Last updated: 2026-06-02*
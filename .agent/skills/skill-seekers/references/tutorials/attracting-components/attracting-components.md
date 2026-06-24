# How To: Attracting Components

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test attracting components

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign ac = list(...)

```python
ac = list(nx.attracting_components(self.G1))
```

**Verification:**
```python
assert {2} in ac
```

### Step 2: Assign ac = list(...)

```python
ac = list(nx.attracting_components(self.G2))
```

**Verification:**
```python
assert {9} in ac
```

### Step 3: Assign ac = value

```python
ac = [tuple(sorted(x)) for x in ac]
```

**Verification:**
```python
assert {10} in ac
```

### Step 4: Assign ac = list(...)

```python
ac = list(nx.attracting_components(self.G3))
```

**Verification:**
```python
assert ac == [(1, 2)]
```

### Step 5: Assign ac = value

```python
ac = [tuple(sorted(x)) for x in ac]
```

**Verification:**
```python
assert (1, 2) in ac
```

### Step 6: Assign ac = list(...)

```python
ac = list(nx.attracting_components(self.G4))
```

**Verification:**
```python
assert (3, 4) in ac
```


## Complete Example

```python
# Workflow
ac = list(nx.attracting_components(self.G1))
assert {2} in ac
assert {9} in ac
assert {10} in ac
ac = list(nx.attracting_components(self.G2))
ac = [tuple(sorted(x)) for x in ac]
assert ac == [(1, 2)]
ac = list(nx.attracting_components(self.G3))
ac = [tuple(sorted(x)) for x in ac]
assert (1, 2) in ac
assert (3, 4) in ac
assert len(ac) == 2
ac = list(nx.attracting_components(self.G4))
assert ac == []
```

## Next Steps


---

*Source: test_attracting.py:32 | Complexity: Intermediate | Last updated: 2026-06-02*
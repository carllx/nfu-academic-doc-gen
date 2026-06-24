# How To: Reverse Reverse Copy

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reverse reverse copy

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.utils`
- `pickle`
- `pickle`
- `pickle`
- `pickle`
- `pickle`


## Step-by-Step Guide

### Step 1: Assign G = self.DG.reverse(...)

```python
G = self.DG.reverse(copy=False)
```

**Verification:**
```python
assert H.nodes == self.DG.nodes
```

### Step 2: Assign H = G.reverse(...)

```python
H = G.reverse(copy=True)
```

**Verification:**
```python
assert H.edges == self.DG.edges
```

### Step 3: Assign G = self.MDG.reverse(...)

```python
G = self.MDG.reverse(copy=False)
```

**Verification:**
```python
assert H.nodes == self.MDG.nodes
```

### Step 4: Assign H = G.reverse(...)

```python
H = G.reverse(copy=True)
```

**Verification:**
```python
assert H.edges == self.MDG.edges
```


## Complete Example

```python
# Workflow
G = self.DG.reverse(copy=False)
H = G.reverse(copy=True)
assert H.nodes == self.DG.nodes
assert H.edges == self.DG.edges
G = self.MDG.reverse(copy=False)
H = G.reverse(copy=True)
assert H.nodes == self.MDG.nodes
assert H.edges == self.MDG.edges
```

## Next Steps


---

*Source: test_graphviews.py:279 | Complexity: Intermediate | Last updated: 2026-06-02*
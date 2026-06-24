# How To: Contains

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test contains

## Prerequisites

**Required Modules:**
- `pickle`
- `copy`
- `pytest`
- `networkx`
- `networkx.classes`
- `networkx.classes.reportviews`
- `pickle`
- `pickle`
- `pickle`
- `pickle`
- `pickle`


## Step-by-Step Guide

### Step 1: Assign G = self.G.copy(...)

```python
G = self.G.copy()
```

**Verification:**
```python
assert (7, {}) in nv
```

### Step 2: Assign nv = G.nodes.data(...)

```python
nv = G.nodes.data()
```

**Verification:**
```python
assert (3, {'foo': 'bar'}) in nv
```

### Step 3: Assign nwv = G.nodes.data(...)

```python
nwv = G.nodes.data('foo')
```

**Verification:**
```python
assert (3, 'bar') in nwv
```

### Step 4: Assign unknown = 'bar'

```python
G.nodes[3]['foo'] = 'bar'
```

**Verification:**
```python
assert (7, None) in nwv
```

### Step 5: Assign nwv_def = G.nodes(...)

```python
nwv_def = G.nodes(data='foo', default='biz')
```

**Verification:**
```python
assert (7, 'biz') in nwv_def
```


## Complete Example

```python
# Workflow
G = self.G.copy()
nv = G.nodes.data()
nwv = G.nodes.data('foo')
G.nodes[3]['foo'] = 'bar'
assert (7, {}) in nv
assert (3, {'foo': 'bar'}) in nv
assert (3, 'bar') in nwv
assert (7, None) in nwv
nwv_def = G.nodes(data='foo', default='biz')
assert (7, 'biz') in nwv_def
assert (3, 'bar') in nwv_def
```

## Next Steps


---

*Source: test_reportviews.py:115 | Complexity: Intermediate | Last updated: 2026-06-02*
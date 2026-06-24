# How To: Eccentricity Weight Fn

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test eccentricity weight fn

## Prerequisites

**Required Modules:**
- `itertools`
- `math`
- `random`
- `pytest`
- `networkx`
- `networkx`
- `networkx.algorithms.distance_measures`


## Step-by-Step Guide

### Step 1: Assign e = nx.eccentricity(...)

```python
e = nx.eccentricity(self.G, weight=self.weight_fn)
```

**Verification:**
```python
assert nx.eccentricity(self.G, 1, weight=self.weight_fn) == 6
```

### Step 2: Assign e = nx.eccentricity(...)

```python
e = nx.eccentricity(self.G, v=1, weight=self.weight_fn)
```

**Verification:**
```python
assert e[1] == 6
```

### Step 3: Assign e = nx.eccentricity(...)

```python
e = nx.eccentricity(self.G, v=[1, 1], weight=self.weight_fn)
```

**Verification:**
```python
assert e == 6
```

### Step 4: Assign e = nx.eccentricity(...)

```python
e = nx.eccentricity(self.G, v=[1, 2], weight=self.weight_fn)
```

**Verification:**
```python
assert e[1] == 6
```


## Complete Example

```python
# Workflow
assert nx.eccentricity(self.G, 1, weight=self.weight_fn) == 6
e = nx.eccentricity(self.G, weight=self.weight_fn)
assert e[1] == 6
e = nx.eccentricity(self.G, v=1, weight=self.weight_fn)
assert e == 6
e = nx.eccentricity(self.G, v=[1, 1], weight=self.weight_fn)
assert e[1] == 6
e = nx.eccentricity(self.G, v=[1, 2], weight=self.weight_fn)
assert e[1] == 6
```

## Next Steps


---

*Source: test_distance_measures.py:220 | Complexity: Intermediate | Last updated: 2026-06-02*
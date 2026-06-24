# How To: Eccentricity Weight None

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test eccentricity weight None

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
e = nx.eccentricity(self.G, weight=None)
```

**Verification:**
```python
assert nx.eccentricity(self.G, 1, weight=None) == 3
```

### Step 2: Assign e = nx.eccentricity(...)

```python
e = nx.eccentricity(self.G, v=1, weight=None)
```

**Verification:**
```python
assert e[1] == 3
```

### Step 3: Assign e = nx.eccentricity(...)

```python
e = nx.eccentricity(self.G, v=[1, 1], weight=None)
```

**Verification:**
```python
assert e == 3
```

### Step 4: Assign e = nx.eccentricity(...)

```python
e = nx.eccentricity(self.G, v=[1, 2], weight=None)
```

**Verification:**
```python
assert e[1] == 3
```


## Complete Example

```python
# Workflow
assert nx.eccentricity(self.G, 1, weight=None) == 3
e = nx.eccentricity(self.G, weight=None)
assert e[1] == 3
e = nx.eccentricity(self.G, v=1, weight=None)
assert e == 3
e = nx.eccentricity(self.G, v=[1, 1], weight=None)
assert e[1] == 3
e = nx.eccentricity(self.G, v=[1, 2], weight=None)
assert e[1] == 3
```

## Next Steps


---

*Source: test_distance_measures.py:187 | Complexity: Intermediate | Last updated: 2026-06-02*
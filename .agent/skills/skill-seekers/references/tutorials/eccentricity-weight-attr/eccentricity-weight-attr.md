# How To: Eccentricity Weight Attr

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test eccentricity weight attr

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
e = nx.eccentricity(self.G, weight='weight')
```

**Verification:**
```python
assert nx.eccentricity(self.G, 1, weight='weight') == 1.5
```

### Step 2: Assign e = nx.eccentricity(...)

```python
e = nx.eccentricity(self.G, v=1, weight='weight')
```

**Verification:**
```python
assert e == nx.eccentricity(self.G, weight='cost') != nx.eccentricity(self.G, weight='high_cost')
```

### Step 3: Assign e = nx.eccentricity(...)

```python
e = nx.eccentricity(self.G, v=[1, 1], weight='weight')
```

**Verification:**
```python
assert e[1] == 1.5
```

### Step 4: Assign e = nx.eccentricity(...)

```python
e = nx.eccentricity(self.G, v=[1, 2], weight='weight')
```

**Verification:**
```python
assert e == 1.5
```


## Complete Example

```python
# Workflow
assert nx.eccentricity(self.G, 1, weight='weight') == 1.5
e = nx.eccentricity(self.G, weight='weight')
assert e == nx.eccentricity(self.G, weight='cost') != nx.eccentricity(self.G, weight='high_cost')
assert e[1] == 1.5
e = nx.eccentricity(self.G, v=1, weight='weight')
assert e == 1.5
e = nx.eccentricity(self.G, v=[1, 1], weight='weight')
assert e[1] == 1.5
e = nx.eccentricity(self.G, v=[1, 2], weight='weight')
assert e[1] == 1.5
```

## Next Steps


---

*Source: test_distance_measures.py:201 | Complexity: Intermediate | Last updated: 2026-06-02*
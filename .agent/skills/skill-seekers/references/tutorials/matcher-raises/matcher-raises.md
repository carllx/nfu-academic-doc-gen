# How To: Matcher Raises

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test matcher raises

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `importlib.resources`
- `random`
- `struct`
- `pytest`
- `networkx`
- `networkx.algorithms`
- `networkx.generators`

**Setup Required:**
```python
# Fixtures: G1, G2
```

## Step-by-Step Guide

### Step 1: Assign undirected_matchers = value

```python
undirected_matchers = [iso.GraphMatcher, iso.MultiGraphMatcher]
```

### Step 2: Assign directed_matchers = value

```python
directed_matchers = [iso.DiGraphMatcher, iso.MultiDiGraphMatcher]
```

### Step 3: Call matcher()

```python
matcher(G1, G2)
```

### Step 4: Assign msg = '\\(Multi-\\)GraphMatcher\\(\\) not defined for directed graphs'

```python
msg = '\\(Multi-\\)GraphMatcher\\(\\) not defined for directed graphs'
```

### Step 5: Call matcher()

```python
matcher(G1.to_directed(), G2.to_directed())
```

### Step 6: Assign msg = '\\(Multi-\\)DiGraphMatcher\\(\\) not defined for undirected graphs'

```python
msg = '\\(Multi-\\)DiGraphMatcher\\(\\) not defined for undirected graphs'
```

### Step 7: Assign msg = 'G1 and G2 must have the same directedness'

```python
msg = 'G1 and G2 must have the same directedness'
```

### Step 8: Call matcher()

```python
matcher(G1.to_directed(), G2.to_directed())
```

### Step 9: Call matcher()

```python
matcher(G1, G2)
```

### Step 10: Call matcher()

```python
matcher(G1, G2.to_directed())
```

### Step 11: Call matcher()

```python
matcher(G1.to_directed(), G2)
```


## Complete Example

```python
# Setup
# Fixtures: G1, G2

# Workflow
undirected_matchers = [iso.GraphMatcher, iso.MultiGraphMatcher]
directed_matchers = [iso.DiGraphMatcher, iso.MultiDiGraphMatcher]
for matcher in undirected_matchers:
    matcher(G1, G2)
    msg = '\\(Multi-\\)GraphMatcher\\(\\) not defined for directed graphs'
    with pytest.raises(nx.NetworkXError, match=msg):
        matcher(G1.to_directed(), G2.to_directed())
for matcher in directed_matchers:
    matcher(G1.to_directed(), G2.to_directed())
    msg = '\\(Multi-\\)DiGraphMatcher\\(\\) not defined for undirected graphs'
    with pytest.raises(nx.NetworkXError, match=msg):
        matcher(G1, G2)
for matcher in undirected_matchers + directed_matchers:
    msg = 'G1 and G2 must have the same directedness'
    with pytest.raises(nx.NetworkXError, match=msg):
        matcher(G1, G2.to_directed())
    with pytest.raises(nx.NetworkXError, match=msg):
        matcher(G1.to_directed(), G2)
```

## Next Steps


---

*Source: test_isomorphvf2.py:249 | Complexity: Advanced | Last updated: 2026-06-02*
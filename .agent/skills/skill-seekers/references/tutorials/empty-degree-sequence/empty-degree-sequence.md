# How To: Empty Degree Sequence

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: Tests that an empty degree sequence yields the null graph.

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: 'Tests that an empty degree sequence yields the null graph.'

```python
'Tests that an empty degree sequence yields the null graph.'
```

**Verification:**
```python
assert len(G) == 0
```

### Step 2: Assign G = nx.configuration_model(...)

```python
G = nx.configuration_model([])
```

**Verification:**
```python
assert len(G) == 0
```


## Complete Example

```python
# Workflow
'Tests that an empty degree sequence yields the null graph.'
G = nx.configuration_model([])
assert len(G) == 0
```

## Next Steps


---

*Source: test_degree_seq.py:12 | Complexity: Beginner | Last updated: 2026-06-02*
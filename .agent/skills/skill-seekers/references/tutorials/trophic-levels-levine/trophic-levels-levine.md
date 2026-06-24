# How To: Trophic Levels Levine

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate array: Example from Figure 5 in Stephen Levine (1980) J. theor. Biol. 83,
195-207

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign expected_q = np.array(...)

```python
expected_q = np.array([[0, 0, 0.0, 0], [0.2, 0, 0.6, 0], [0, 0, 0, 0.2], [0.3, 0, 0.7, 0]])
```


## Complete Example

```python
# Workflow
expected_q = np.array([[0, 0, 0.0, 0], [0.2, 0, 0.6, 0], [0, 0, 0, 0.2], [0.3, 0, 0.7, 0]])
```

## Next Steps


---

*Source: test_trophic.py:47 | Complexity: Beginner | Last updated: 2026-06-02*
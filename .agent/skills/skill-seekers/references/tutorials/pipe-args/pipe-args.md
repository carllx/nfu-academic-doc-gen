# How To: Pipe Args

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate DataFrame: test pipe args

## Prerequisites

**Required Modules:**
- `numpy`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'group': ['A', 'A', 'B', 'B', 'C'], 'x': [1.0, 2.0, 3.0, 2.0, 5.0], 'y': [10.0, 100.0, 1000.0, -100.0, -1000.0]})
```


## Complete Example

```python
# Workflow
df = DataFrame({'group': ['A', 'A', 'B', 'B', 'C'], 'x': [1.0, 2.0, 3.0, 2.0, 5.0], 'y': [10.0, 100.0, 1000.0, -100.0, -1000.0]})
```

## Next Steps


---

*Source: test_pipe.py:48 | Complexity: Beginner | Last updated: 2026-06-02*
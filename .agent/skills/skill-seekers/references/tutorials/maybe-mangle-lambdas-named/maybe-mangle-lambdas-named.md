# How To: Maybe Mangle Lambdas Named

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Configuration example: test maybe mangle lambdas named

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.apply`


## Step-by-Step Guide

### Step 1: Assign func = value

```python
func = {'C': np.mean, 'D': {'foo': np.mean, 'bar': np.mean}}
```


## Complete Example

```python
# Workflow
func = {'C': np.mean, 'D': {'foo': np.mean, 'bar': np.mean}}
```

## Next Steps


---

*Source: test_aggregation.py:45 | Complexity: Beginner | Last updated: 2026-06-02*
# How To: Agg Relabel Multi Columns Multi Methods

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate agg: test agg relabel multi columns multi methods

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat.numpy`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign result = df.agg(...)

```python
result = df.agg(foo=('A', 'sum'), bar=('B', 'mean'), cat=('A', 'min'), dat=('B', 'max'), f=('A', 'max'), g=('C', 'min'))
```


## Complete Example

```python
# Workflow
result = df.agg(foo=('A', 'sum'), bar=('B', 'mean'), cat=('A', 'min'), dat=('B', 'max'), f=('A', 'max'), g=('C', 'min'))
```

## Next Steps


---

*Source: test_frame_apply_relabeling.py:29 | Complexity: Beginner | Last updated: 2026-06-02*
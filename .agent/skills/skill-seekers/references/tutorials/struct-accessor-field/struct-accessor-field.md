# How To: Struct Accessor Field

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: pytest

## Overview

Instantiate Series: test struct accessor field

## Prerequisites

**Required Modules:**
- `re`
- `pytest`
- `pandas.compat.pyarrow`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series([{'rice': 1.0, 'maize': -1, 'wheat': 'a'}, {'rice': 2.0, 'maize': 0, 'wheat': 'b'}, {'rice': 3.0, 'maize': 1, 'wheat': 'c'}], dtype=ArrowDtype(pa.struct([('rice', pa.float64()), ('maize', pa.int64()), ('wheat', pa.string())])), index=index)
```


## Complete Example

```python
# Workflow
ser = Series([{'rice': 1.0, 'maize': -1, 'wheat': 'a'}, {'rice': 2.0, 'maize': 0, 'wheat': 'b'}, {'rice': 3.0, 'maize': 1, 'wheat': 'c'}], dtype=ArrowDtype(pa.struct([('rice', pa.float64()), ('maize', pa.int64()), ('wheat', pa.string())])), index=index)
```

## Next Steps


---

*Source: test_struct_accessor.py:65 | Complexity: Beginner | Last updated: 2026-06-02*
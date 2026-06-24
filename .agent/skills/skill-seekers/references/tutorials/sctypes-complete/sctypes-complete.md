# How To: Sctypes Complete

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sctypes complete

## Prerequisites

**Required Modules:**
- `itertools`
- `sys`
- `pytest`
- `numpy`
- `numpy._core.numerictypes`
- `numpy._core.numerictypes`
- `numpy.testing`
- `numpy._core._rational_tests`


## Step-by-Step Guide


## Complete Example

```python
# Workflow
assert np.int32 in sctypes['int']
assert np.intc in sctypes['int']
assert np.int64 in sctypes['int']
assert np.uint32 in sctypes['uint']
assert np.uintc in sctypes['uint']
assert np.uint64 in sctypes['uint']
```

## Next Steps


---

*Source: test_numerictypes.py:479 | Complexity: Beginner | Last updated: 2026-06-02*
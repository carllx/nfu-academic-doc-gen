# How To: Is Sequence

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: test is sequence

## Prerequisites

**Required Modules:**
- `collections`
- `collections`
- `collections.abc`
- `datetime`
- `decimal`
- `fractions`
- `io`
- `itertools`
- `numbers`
- `re`
- `sys`
- `typing`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs`
- `pandas.compat.numpy`
- `pandas.core.dtypes`
- `pandas.core.dtypes.cast`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign is_seq = value

```python
is_seq = inference.is_sequence
```

**Verification:**
```python
assert is_seq((1, 2))
```


## Complete Example

```python
# Workflow
is_seq = inference.is_sequence
assert is_seq((1, 2))
assert is_seq([1, 2])
assert not is_seq('abcd')
assert not is_seq(np.int64)

class A:

    def __getitem__(self, item):
        return 1
assert not is_seq(A())
```

## Next Steps


---

*Source: test_inference.py:254 | Complexity: Beginner | Last updated: 2026-06-02*
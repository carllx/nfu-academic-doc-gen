# How To: Iterator Stop On Chunksize

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate DataFrame: test iterator stop on chunksize

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_parsers
```

## Step-by-Step Guide

### Step 1: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=['foo', 'bar', 'baz'], columns=['A', 'B', 'C'])
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
expected = DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=['foo', 'bar', 'baz'], columns=['A', 'B', 'C'])
```

## Next Steps


---

*Source: test_iterator.py:92 | Complexity: Beginner | Last updated: 2026-06-02*
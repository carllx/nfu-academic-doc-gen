# How To: Conflict Asdict With All Fields

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate Conflict: dataclasses.asdict(conflict) should produce a full, deep-copied mapping.

Mirrors the production serialization path (see ConflictDetector, which
emits ``asdict(c)`` for each conflict), rather than the shallow
``__dict__`` attribute view.

## Prerequisites

**Required Modules:**
- `dataclasses`
- `skill_seekers.cli.conflict_detector`


## Step-by-Step Guide

### Step 1: Assign conflict = Conflict(...)

```python
conflict = Conflict(type='signature_mismatch', severity='medium', api_name='my_api', docs_info={'params': ['a', 'b']}, code_info={'params': ['a', 'b', 'c']}, difference='code has extra param c', suggestion='add param c to docs')
```


## Complete Example

```python
# Workflow
conflict = Conflict(type='signature_mismatch', severity='medium', api_name='my_api', docs_info={'params': ['a', 'b']}, code_info={'params': ['a', 'b', 'c']}, difference='code has extra param c', suggestion='add param c to docs')
```

## Next Steps


---

*Source: test_conflict_detector.py:56 | Complexity: Beginner | Last updated: 2026-06-02*
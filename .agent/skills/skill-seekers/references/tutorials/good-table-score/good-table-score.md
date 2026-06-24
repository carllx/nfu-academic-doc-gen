# How To: Good Table Score

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate Table: Test quality score for good table.

## Prerequisites

**Required Modules:**
- `sys`
- `pytest`
- `skill_seekers.cli.parsers.extractors`
- `skill_seekers.cli.parsers.extractors`
- `skill_seekers.cli.parsers.extractors`
- `skill_seekers.cli.parsers.extractors`
- `skill_seekers.cli.parsers.extractors`


## Step-by-Step Guide

### Step 1: Assign good_table = Table(...)

```python
good_table = Table(rows=[['1', '2', '3'], ['4', '5', '6']], headers=['A', 'B', 'C'], caption='Good Table')
```


## Complete Example

```python
# Workflow
good_table = Table(rows=[['1', '2', '3'], ['4', '5', '6']], headers=['A', 'B', 'C'], caption='Good Table')
```

## Next Steps


---

*Source: test_unified_parsers.py:420 | Complexity: Beginner | Last updated: 2026-06-02*
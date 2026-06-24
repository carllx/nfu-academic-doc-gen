# How To: Highlight Between Inclusive

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: pytest

## Overview

Configuration example: test highlight between inclusive

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas.io.formats.style`

**Setup Required:**
```python
# Fixtures: styler, inclusive, expected
```

## Step-by-Step Guide

### Step 1: Assign kwargs = value

```python
kwargs = {'left': 0, 'right': 1, 'subset': IndexSlice[[0, 1], :]}
```


## Complete Example

```python
# Setup
# Fixtures: styler, inclusive, expected

# Workflow
kwargs = {'left': 0, 'right': 1, 'subset': IndexSlice[[0, 1], :]}
```

## Next Steps


---

*Source: test_highlight.py:166 | Complexity: Beginner | Last updated: 2026-06-02*
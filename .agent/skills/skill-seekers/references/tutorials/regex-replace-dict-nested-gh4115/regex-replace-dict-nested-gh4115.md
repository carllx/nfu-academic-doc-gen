# How To: Regex Replace Dict Nested Gh4115

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test regex replace dict nested gh4115

## Prerequisites

**Required Modules:**
- `__future__`
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'Type': Series(['Q', 'T', 'Q', 'Q', 'T'], dtype=object), 'tmp': 2})
```

### Step 2: Assign expected = DataFrame(...)

```python
expected = DataFrame({'Type': [0, 1, 0, 0, 1], 'tmp': 2})
```

### Step 3: Assign msg = 'Downcasting behavior in `replace`'

```python
msg = 'Downcasting behavior in `replace`'
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign result = df.replace(...)

```python
result = df.replace({'Type': {'Q': 0, 'T': 1}})
```


## Complete Example

```python
# Workflow
df = DataFrame({'Type': Series(['Q', 'T', 'Q', 'Q', 'T'], dtype=object), 'tmp': 2})
expected = DataFrame({'Type': [0, 1, 0, 0, 1], 'tmp': 2})
msg = 'Downcasting behavior in `replace`'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = df.replace({'Type': {'Q': 0, 'T': 1}})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_replace.py:291 | Complexity: Intermediate | Last updated: 2026-06-02*
# How To: Inplace Raises

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test inplace raises

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `operator`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: method, frame_only
```

## Step-by-Step Guide

### Step 1: Assign df = pd.DataFrame.set_flags(...)

```python
df = pd.DataFrame({'A': [0, 0], 'B': [1, 2]}).set_flags(allows_duplicate_labels=False)
```

### Step 2: Assign s = value

```python
s = df['A']
```

### Step 3: Assign s.flags.allows_duplicate_labels = False

```python
s.flags.allows_duplicate_labels = False
```

### Step 4: Assign msg = 'Cannot specify'

```python
msg = 'Cannot specify'
```

### Step 5: Call method()

```python
method(df)
```

### Step 6: Call method()

```python
method(s)
```


## Complete Example

```python
# Setup
# Fixtures: method, frame_only

# Workflow
df = pd.DataFrame({'A': [0, 0], 'B': [1, 2]}).set_flags(allows_duplicate_labels=False)
s = df['A']
s.flags.allows_duplicate_labels = False
msg = 'Cannot specify'
with pytest.raises(ValueError, match=msg):
    method(df)
if not frame_only:
    with pytest.raises(ValueError, match=msg):
        method(s)
```

## Next Steps


---

*Source: test_duplicate_labels.py:391 | Complexity: Intermediate | Last updated: 2026-06-02*
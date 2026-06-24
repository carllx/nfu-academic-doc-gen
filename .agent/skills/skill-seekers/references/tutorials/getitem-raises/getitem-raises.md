# How To: Getitem Raises

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test getitem raises

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
# Fixtures: getter, target
```

## Step-by-Step Guide

### Step 1: Assign df = pd.DataFrame.set_flags(...)

```python
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}, index=['a', 'b']).set_flags(allows_duplicate_labels=False)
```

### Step 2: Assign msg = 'Index has duplicates.'

```python
msg = 'Index has duplicates.'
```

### Step 3: Assign target = getattr(...)

```python
target = getattr(df, target)
```

### Step 4: Assign target = df

```python
target = df
```

### Step 5: Call getter()

```python
getter(target)
```


## Complete Example

```python
# Setup
# Fixtures: getter, target

# Workflow
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}, index=['a', 'b']).set_flags(allows_duplicate_labels=False)
if target:
    target = getattr(df, target)
else:
    target = df
msg = 'Index has duplicates.'
with pytest.raises(pd.errors.DuplicateLabelError, match=msg):
    getter(target)
```

## Next Steps


---

*Source: test_duplicate_labels.py:287 | Complexity: Intermediate | Last updated: 2026-06-02*
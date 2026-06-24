# How To: Check Label Or Level Ambiguity Df

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test check label or level ambiguity df

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas.core.dtypes.missing`
- `pandas`

**Setup Required:**
```python
# Fixtures: df_ambig, axis
```

## Step-by-Step Guide

### Step 1: Assign axis = df_ambig._get_axis_number(...)

```python
axis = df_ambig._get_axis_number(axis)
```

**Verification:**
```python
assert not df_ambig._check_label_or_level_ambiguity('L3', axis=axis)
```

### Step 2: Call df_ambig._check_label_or_level_ambiguity()

```python
df_ambig._check_label_or_level_ambiguity('L2', axis=axis)
```

**Verification:**
```python
assert not df_ambig._check_label_or_level_ambiguity('L3', axis=axis)
```

### Step 3: Assign df_ambig = value

```python
df_ambig = df_ambig.T
```

### Step 4: Assign msg = "'L1' is both a column level and an index label"

```python
msg = "'L1' is both a column level and an index label"
```

### Step 5: Assign msg = "'L1' is both an index level and a column label"

```python
msg = "'L1' is both an index level and a column label"
```

### Step 6: Call df_ambig._check_label_or_level_ambiguity()

```python
df_ambig._check_label_or_level_ambiguity('L1', axis=axis)
```


## Complete Example

```python
# Setup
# Fixtures: df_ambig, axis

# Workflow
axis = df_ambig._get_axis_number(axis)
if axis == 1:
    df_ambig = df_ambig.T
    msg = "'L1' is both a column level and an index label"
else:
    msg = "'L1' is both an index level and a column label"
with pytest.raises(ValueError, match=msg):
    df_ambig._check_label_or_level_ambiguity('L1', axis=axis)
df_ambig._check_label_or_level_ambiguity('L2', axis=axis)
assert not df_ambig._check_label_or_level_ambiguity('L3', axis=axis)
```

## Next Steps


---

*Source: test_label_or_level_utils.py:131 | Complexity: Intermediate | Last updated: 2026-06-02*
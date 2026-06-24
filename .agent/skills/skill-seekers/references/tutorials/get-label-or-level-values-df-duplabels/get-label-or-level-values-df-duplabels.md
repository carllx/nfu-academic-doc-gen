# How To: Get Label Or Level Values Df Duplabels

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get label or level values df duplabels

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas.core.dtypes.missing`
- `pandas`

**Setup Required:**
```python
# Fixtures: df_duplabels, axis
```

## Step-by-Step Guide

### Step 1: Assign axis = df_duplabels._get_axis_number(...)

```python
axis = df_duplabels._get_axis_number(axis)
```

**Verification:**
```python
assert_level_values(df_duplabels, ['L1'], axis=axis)
```

### Step 2: Call assert_level_values()

```python
assert_level_values(df_duplabels, ['L1'], axis=axis)
```

**Verification:**
```python
assert_label_values(df_duplabels, ['L3'], axis=axis)
```

### Step 3: Call assert_label_values()

```python
assert_label_values(df_duplabels, ['L3'], axis=axis)
```

**Verification:**
```python
assert_label_values(df_duplabels, ['L2'], axis=axis)
```

### Step 4: Assign df_duplabels = value

```python
df_duplabels = df_duplabels.T
```

### Step 5: Assign expected_msg = "The column label 'L2' is not unique"

```python
expected_msg = "The column label 'L2' is not unique"
```

### Step 6: Assign expected_msg = "The index label 'L2' is not unique"

```python
expected_msg = "The index label 'L2' is not unique"
```

### Step 7: Call assert_label_values()

```python
assert_label_values(df_duplabels, ['L2'], axis=axis)
```


## Complete Example

```python
# Setup
# Fixtures: df_duplabels, axis

# Workflow
axis = df_duplabels._get_axis_number(axis)
if axis == 1:
    df_duplabels = df_duplabels.T
assert_level_values(df_duplabels, ['L1'], axis=axis)
assert_label_values(df_duplabels, ['L3'], axis=axis)
if axis == 0:
    expected_msg = "The column label 'L2' is not unique"
else:
    expected_msg = "The index label 'L2' is not unique"
with pytest.raises(ValueError, match=expected_msg):
    assert_label_values(df_duplabels, ['L2'], axis=axis)
```

## Next Steps


---

*Source: test_label_or_level_utils.py:232 | Complexity: Intermediate | Last updated: 2026-06-02*
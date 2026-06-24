# How To: Join On Pass Vector

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test join on pass vector

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: target_source
```

## Step-by-Step Guide

### Step 1: Assign unknown = target_source

```python
target, source = target_source
```

### Step 2: Assign expected = target.join(...)

```python
expected = target.join(source, on='C')
```

### Step 3: Assign expected = expected.rename(...)

```python
expected = expected.rename(columns={'C': 'key_0'})
```

### Step 4: Assign expected = value

```python
expected = expected[['key_0', 'A', 'B', 'D', 'MergedA', 'MergedD']]
```

### Step 5: Assign join_col = target.pop(...)

```python
join_col = target.pop('C')
```

### Step 6: Assign result = target.join(...)

```python
result = target.join(source, on=join_col)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: target_source

# Workflow
target, source = target_source
expected = target.join(source, on='C')
expected = expected.rename(columns={'C': 'key_0'})
expected = expected[['key_0', 'A', 'B', 'D', 'MergedA', 'MergedD']]
join_col = target.pop('C')
result = target.join(source, on=join_col)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_join.py:238 | Complexity: Intermediate | Last updated: 2026-06-02*
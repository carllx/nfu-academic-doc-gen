# How To: Frame Equal Block Mismatch

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test frame equal block mismatch

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: by_blocks_fixture, obj_fixture
```

## Step-by-Step Guide

### Step 1: Assign obj = obj_fixture

```python
obj = obj_fixture
```

### Step 2: Assign msg = value

```python
msg = f'{obj}\\.iloc\\[:, 1\\] \\(column name="B"\\) are different\n\n{obj}\\.iloc\\[:, 1\\] \\(column name="B"\\) values are different \\(33\\.33333 %\\)\n\\[index\\]: \\[0, 1, 2\\]\n\\[left\\]:  \\[4, 5, 6\\]\n\\[right\\]: \\[4, 5, 7\\]'
```

### Step 3: Assign df1 = DataFrame(...)

```python
df1 = DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
```

### Step 4: Assign df2 = DataFrame(...)

```python
df2 = DataFrame({'A': [1, 2, 3], 'B': [4, 5, 7]})
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df1, df2, by_blocks=by_blocks_fixture, obj=obj_fixture)
```


## Complete Example

```python
# Setup
# Fixtures: by_blocks_fixture, obj_fixture

# Workflow
obj = obj_fixture
msg = f'{obj}\\.iloc\\[:, 1\\] \\(column name="B"\\) are different\n\n{obj}\\.iloc\\[:, 1\\] \\(column name="B"\\) values are different \\(33\\.33333 %\\)\n\\[index\\]: \\[0, 1, 2\\]\n\\[left\\]:  \\[4, 5, 6\\]\n\\[right\\]: \\[4, 5, 7\\]'
df1 = DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = DataFrame({'A': [1, 2, 3], 'B': [4, 5, 7]})
with pytest.raises(AssertionError, match=msg):
    tm.assert_frame_equal(df1, df2, by_blocks=by_blocks_fixture, obj=obj_fixture)
```

## Next Steps


---

*Source: test_assert_frame_equal.py:150 | Complexity: Intermediate | Last updated: 2026-06-02*
# How To: Group Apply Once Per Group2

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test group apply once per group2

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.groupby`

**Setup Required:**
```python
# Fixtures: capsys
```

## Step-by-Step Guide

### Step 1: Assign expected = 2

```python
expected = 2
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'group_by_column': [0, 0, 0, 0, 1, 1, 1, 1], 'test_column': ['0', '2', '4', '6', '8', '10', '12', '14']}, index=['0', '2', '4', '6', '8', '10', '12', '14'])
```

### Step 3: Assign msg = 'DataFrameGroupBy.apply operated on the grouping columns'

```python
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
```

### Step 4: Assign result = capsys.readouterr.out.count(...)

```python
result = capsys.readouterr().out.count('function_called')
```

**Verification:**
```python
assert result == expected
```

### Step 5: Call df.groupby.apply()

```python
df.groupby('group_by_column', group_keys=False).apply(lambda df: print('function_called'))
```


## Complete Example

```python
# Setup
# Fixtures: capsys

# Workflow
expected = 2
df = DataFrame({'group_by_column': [0, 0, 0, 0, 1, 1, 1, 1], 'test_column': ['0', '2', '4', '6', '8', '10', '12', '14']}, index=['0', '2', '4', '6', '8', '10', '12', '14'])
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
with tm.assert_produces_warning(FutureWarning, match=msg):
    df.groupby('group_by_column', group_keys=False).apply(lambda df: print('function_called'))
result = capsys.readouterr().out.count('function_called')
assert result == expected
```

## Next Steps


---

*Source: test_apply.py:234 | Complexity: Intermediate | Last updated: 2026-06-02*
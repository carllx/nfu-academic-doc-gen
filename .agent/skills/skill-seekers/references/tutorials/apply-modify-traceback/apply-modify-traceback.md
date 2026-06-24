# How To: Apply Modify Traceback

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test apply modify traceback

## Prerequisites

**Required Modules:**
- `itertools`
- `re`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign data = DataFrame(...)

```python
data = DataFrame({'A': ['foo', 'foo', 'foo', 'foo', 'bar', 'bar', 'bar', 'bar', 'foo', 'foo', 'foo'], 'B': ['one', 'one', 'one', 'two', 'one', 'one', 'one', 'two', 'two', 'two', 'one'], 'C': ['dull', 'dull', 'shiny', 'dull', 'dull', 'shiny', 'shiny', 'dull', 'shiny', 'shiny', 'shiny'], 'D': np.random.default_rng(2).standard_normal(11), 'E': np.random.default_rng(2).standard_normal(11), 'F': np.random.default_rng(2).standard_normal(11)})
```

### Step 2: Assign unknown = value

```python
data.loc[4, 'C'] = np.nan
```

### Step 3: Assign msg = "'float' object has no attribute 'startswith'"

```python
msg = "'float' object has no attribute 'startswith'"
```

### Step 4: Call data.apply()

```python
data.apply(transform, axis=1)
```

### Step 5: Assign unknown = 7

```python
row['D'] = 7
```


## Complete Example

```python
# Workflow
data = DataFrame({'A': ['foo', 'foo', 'foo', 'foo', 'bar', 'bar', 'bar', 'bar', 'foo', 'foo', 'foo'], 'B': ['one', 'one', 'one', 'two', 'one', 'one', 'one', 'two', 'two', 'two', 'one'], 'C': ['dull', 'dull', 'shiny', 'dull', 'dull', 'shiny', 'shiny', 'dull', 'shiny', 'shiny', 'shiny'], 'D': np.random.default_rng(2).standard_normal(11), 'E': np.random.default_rng(2).standard_normal(11), 'F': np.random.default_rng(2).standard_normal(11)})
data.loc[4, 'C'] = np.nan

def transform(row):
    if row['C'].startswith('shin') and row['A'] == 'foo':
        row['D'] = 7
    return row
msg = "'float' object has no attribute 'startswith'"
with pytest.raises(AttributeError, match=msg):
    data.apply(transform, axis=1)
```

## Next Steps


---

*Source: test_invalid_arg.py:152 | Complexity: Intermediate | Last updated: 2026-06-02*
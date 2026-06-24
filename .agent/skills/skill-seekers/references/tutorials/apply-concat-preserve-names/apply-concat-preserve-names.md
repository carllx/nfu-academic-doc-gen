# How To: Apply Concat Preserve Names

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test apply concat preserve names

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
# Fixtures: three_group
```

## Step-by-Step Guide

### Step 1: Assign grouped = three_group.groupby(...)

```python
grouped = three_group.groupby(['A', 'B'])
```

**Verification:**
```python
assert result.index.names == ('A', 'B', 'stat')
```

### Step 2: Assign msg = 'DataFrameGroupBy.apply operated on the grouping columns'

```python
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
```

**Verification:**
```python
assert result2.index.names == ('A', 'B', 'stat')
```

### Step 3: Assign msg = 'DataFrameGroupBy.apply operated on the grouping columns'

```python
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
```

**Verification:**
```python
assert result3.index.names == ('A', 'B', None)
```

### Step 4: Assign msg = 'DataFrameGroupBy.apply operated on the grouping columns'

```python
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
```

**Verification:**
```python
assert result3.index.names == ('A', 'B', None)
```

### Step 5: Assign result = group.describe(...)

```python
result = group.describe()
```

### Step 6: Assign result.index.name = 'stat'

```python
result.index.name = 'stat'
```

### Step 7: Assign result = group.describe(...)

```python
result = group.describe()
```

### Step 8: Assign result.index.name = 'stat'

```python
result.index.name = 'stat'
```

### Step 9: Assign result = value

```python
result = result[:len(group)]
```

### Step 10: Assign result = group.describe(...)

```python
result = group.describe()
```

### Step 11: Assign result.index.name = value

```python
result.index.name = f'stat_{len(group):d}'
```

### Step 12: Assign result = value

```python
result = result[:len(group)]
```

### Step 13: Assign result = grouped.apply(...)

```python
result = grouped.apply(desc)
```

### Step 14: Assign result2 = grouped.apply(...)

```python
result2 = grouped.apply(desc2)
```

### Step 15: Assign result3 = grouped.apply(...)

```python
result3 = grouped.apply(desc3)
```


## Complete Example

```python
# Setup
# Fixtures: three_group

# Workflow
grouped = three_group.groupby(['A', 'B'])

def desc(group):
    result = group.describe()
    result.index.name = 'stat'
    return result

def desc2(group):
    result = group.describe()
    result.index.name = 'stat'
    result = result[:len(group)]
    return result

def desc3(group):
    result = group.describe()
    result.index.name = f'stat_{len(group):d}'
    result = result[:len(group)]
    return result
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = grouped.apply(desc)
assert result.index.names == ('A', 'B', 'stat')
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result2 = grouped.apply(desc2)
assert result2.index.names == ('A', 'B', 'stat')
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result3 = grouped.apply(desc3)
assert result3.index.names == ('A', 'B', None)
```

## Next Steps


---

*Source: test_apply.py:366 | Complexity: Advanced | Last updated: 2026-06-02*
# How To: Logical Ops Invalid

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test logical ops invalid

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `operator`
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign df1 = DataFrame(...)

```python
df1 = DataFrame(1.0, index=[1], columns=['A'])
```

### Step 2: Assign df2 = DataFrame(...)

```python
df2 = DataFrame(True, index=[1], columns=['A'])
```

### Step 3: Assign msg = re.escape(...)

```python
msg = re.escape("unsupported operand type(s) for |: 'float' and 'bool'")
```

### Step 4: Assign df1 = DataFrame(...)

```python
df1 = DataFrame('foo', index=[1], columns=['A'])
```

### Step 5: Assign df2 = DataFrame(...)

```python
df2 = DataFrame(True, index=[1], columns=['A'])
```

### Step 6: df1 | df2

```python
df1 | df2
```

### Step 7: Assign msg = "operation 'or_' not supported for dtype 'str'"

```python
msg = "operation 'or_' not supported for dtype 'str'"
```

### Step 8: Assign msg = re.escape(...)

```python
msg = re.escape("unsupported operand type(s) for |: 'str' and 'bool'")
```

### Step 9: df1 | df2

```python
df1 | df2
```


## Complete Example

```python
# Setup
# Fixtures: using_infer_string

# Workflow
df1 = DataFrame(1.0, index=[1], columns=['A'])
df2 = DataFrame(True, index=[1], columns=['A'])
msg = re.escape("unsupported operand type(s) for |: 'float' and 'bool'")
with pytest.raises(TypeError, match=msg):
    df1 | df2
df1 = DataFrame('foo', index=[1], columns=['A'])
df2 = DataFrame(True, index=[1], columns=['A'])
if using_infer_string and df1['A'].dtype.storage == 'pyarrow':
    msg = "operation 'or_' not supported for dtype 'str'"
else:
    msg = re.escape("unsupported operand type(s) for |: 'str' and 'bool'")
with pytest.raises(TypeError, match=msg):
    df1 | df2
```

## Next Steps


---

*Source: test_logical_ops.py:99 | Complexity: Advanced | Last updated: 2026-06-02*
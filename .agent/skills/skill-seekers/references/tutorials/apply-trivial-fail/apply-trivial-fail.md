# How To: Apply Trivial Fail

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test apply trivial fail

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
# Fixtures: using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'key': ['a', 'a', 'b', 'b', 'a'], 'data': [1.0, 2.0, 3.0, 4.0, 5.0]}, columns=['key', 'data'])
```

### Step 2: Assign dtype = value

```python
dtype = 'str' if using_infer_string else 'object'
```

### Step 3: Assign expected = pd.concat(...)

```python
expected = pd.concat([df, df], axis=1, keys=['float64', dtype])
```

### Step 4: Assign msg = 'DataFrame.groupby with axis=1 is deprecated'

```python
msg = 'DataFrame.groupby with axis=1 is deprecated'
```

### Step 5: Assign result = gb.apply(...)

```python
result = gb.apply(lambda x: df)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign gb = df.groupby(...)

```python
gb = df.groupby([str(x) for x in df.dtypes], axis=1, group_keys=True)
```


## Complete Example

```python
# Setup
# Fixtures: using_infer_string

# Workflow
df = DataFrame({'key': ['a', 'a', 'b', 'b', 'a'], 'data': [1.0, 2.0, 3.0, 4.0, 5.0]}, columns=['key', 'data'])
dtype = 'str' if using_infer_string else 'object'
expected = pd.concat([df, df], axis=1, keys=['float64', dtype])
msg = 'DataFrame.groupby with axis=1 is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    gb = df.groupby([str(x) for x in df.dtypes], axis=1, group_keys=True)
result = gb.apply(lambda x: df)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_apply.py:142 | Complexity: Intermediate | Last updated: 2026-06-02*
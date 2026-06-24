# How To: Nan

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test nan

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas.io.formats.format`


## Step-by-Step Guide

### Step 1: Assign formatter = EngFormatter(...)

```python
formatter = EngFormatter(accuracy=1, use_eng_prefix=True)
```

**Verification:**
```python
assert result == 'NaN'
```

### Step 2: Assign result = formatter(...)

```python
result = formatter(np.nan)
```

**Verification:**
```python
assert 'NaN' in result
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1.5, 10.3, 20.5], 'b': [50.3, 60.67, 70.12], 'c': [100.2, 101.33, 120.33]})
```

### Step 4: Assign pt = df.pivot_table(...)

```python
pt = df.pivot_table(values='a', index='b', columns='c')
```

### Step 5: Call set_eng_float_format()

```python
set_eng_float_format(accuracy=1)
```

### Step 6: Assign result = pt.to_string(...)

```python
result = pt.to_string()
```

**Verification:**
```python
assert 'NaN' in result
```


## Complete Example

```python
# Workflow
formatter = EngFormatter(accuracy=1, use_eng_prefix=True)
result = formatter(np.nan)
assert result == 'NaN'
df = DataFrame({'a': [1.5, 10.3, 20.5], 'b': [50.3, 60.67, 70.12], 'c': [100.2, 101.33, 120.33]})
pt = df.pivot_table(values='a', index='b', columns='c')
set_eng_float_format(accuracy=1)
result = pt.to_string()
assert 'NaN' in result
```

## Next Steps


---

*Source: test_eng_formatting.py:230 | Complexity: Intermediate | Last updated: 2026-06-02*
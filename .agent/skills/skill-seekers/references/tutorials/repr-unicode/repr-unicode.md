# How To: Repr Unicode

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test repr unicode

## Prerequisites

**Required Modules:**
- `datetime`
- `io`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign uval = 'σσσσ'

```python
uval = 'σσσσ'
```

**Verification:**
```python
assert result.split('\n')[0].rstrip() == ex_top
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [uval, uval]})
```

**Verification:**
```python
assert result.split('\n')[0].rstrip() == ex_top
```

### Step 3: Assign result = repr(...)

```python
result = repr(df)
```

### Step 4: Assign ex_top = '      A'

```python
ex_top = '      A'
```

**Verification:**
```python
assert result.split('\n')[0].rstrip() == ex_top
```

### Step 5: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [uval, uval]})
```

### Step 6: Assign result = repr(...)

```python
result = repr(df)
```

**Verification:**
```python
assert result.split('\n')[0].rstrip() == ex_top
```


## Complete Example

```python
# Workflow
uval = 'σσσσ'
df = DataFrame({'A': [uval, uval]})
result = repr(df)
ex_top = '      A'
assert result.split('\n')[0].rstrip() == ex_top
df = DataFrame({'A': [uval, uval]})
result = repr(df)
assert result.split('\n')[0].rstrip() == ex_top
```

## Next Steps


---

*Source: test_repr.py:230 | Complexity: Intermediate | Last updated: 2026-06-02*
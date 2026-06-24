# How To: Truncate With Different Dtypes Multiindex

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test truncate with different dtypes multiindex

## Prerequisites

**Required Modules:**
- `datetime`
- `io`
- `pathlib`
- `re`
- `shutil`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas`
- `pandas`
- `pandas.io.formats`
- `pandas.io.formats.format`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'Vals': range(100)})
```

**Verification:**
```python
assert result.startswith(result2)
```

### Step 2: Assign frame = pd.concat(...)

```python
frame = pd.concat([df], keys=['Sweep'], names=['Sweep', 'Index'])
```

### Step 3: Assign result = repr(...)

```python
result = repr(frame)
```

### Step 4: Assign result2 = repr(...)

```python
result2 = repr(frame.iloc[:5])
```

**Verification:**
```python
assert result.startswith(result2)
```


## Complete Example

```python
# Workflow
df = DataFrame({'Vals': range(100)})
frame = pd.concat([df], keys=['Sweep'], names=['Sweep', 'Index'])
result = repr(frame)
result2 = repr(frame.iloc[:5])
assert result.startswith(result2)
```

## Next Steps


---

*Source: test_format.py:904 | Complexity: Intermediate | Last updated: 2026-06-02*
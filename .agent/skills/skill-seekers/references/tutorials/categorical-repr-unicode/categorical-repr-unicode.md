# How To: Categorical Repr Unicode

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test categorical repr unicode

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign cat = Categorical(...)

```python
cat = Categorical([County() for _ in range(61)])
```

### Step 2: Assign idx = Index(...)

```python
idx = Index(cat)
```

### Step 3: Assign ser = idx.to_series(...)

```python
ser = idx.to_series()
```

### Step 4: Call repr()

```python
repr(ser)
```

### Step 5: Call str()

```python
str(ser)
```

### Step 6: Assign name = 'San Sebastián'

```python
name = 'San Sebastián'
```

### Step 7: Assign state = 'PR'

```python
state = 'PR'
```


## Complete Example

```python
# Workflow
class County:
    name = 'San Sebastián'
    state = 'PR'

    def __repr__(self) -> str:
        return self.name + ', ' + self.state
cat = Categorical([County() for _ in range(61)])
idx = Index(cat)
ser = idx.to_series()
repr(ser)
str(ser)
```

## Next Steps


---

*Source: test_formats.py:294 | Complexity: Intermediate | Last updated: 2026-06-02*
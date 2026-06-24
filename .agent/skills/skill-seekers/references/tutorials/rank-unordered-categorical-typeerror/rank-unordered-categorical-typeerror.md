# How To: Rank Unordered Categorical Typeerror

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test rank unordered categorical typeerror

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign cat = pd.Categorical(...)

```python
cat = pd.Categorical([], ordered=False)
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(cat)
```

### Step 3: Assign df = ser.to_frame(...)

```python
df = ser.to_frame()
```

### Step 4: Assign msg = 'Cannot perform rank with non-ordered Categorical'

```python
msg = 'Cannot perform rank with non-ordered Categorical'
```

### Step 5: Assign gb = ser.groupby(...)

```python
gb = ser.groupby(cat, observed=False)
```

### Step 6: Assign gb2 = df.groupby(...)

```python
gb2 = df.groupby(cat, observed=False)
```

### Step 7: Call gb.rank()

```python
gb.rank()
```

### Step 8: Call gb2.rank()

```python
gb2.rank()
```


## Complete Example

```python
# Workflow
cat = pd.Categorical([], ordered=False)
ser = Series(cat)
df = ser.to_frame()
msg = 'Cannot perform rank with non-ordered Categorical'
gb = ser.groupby(cat, observed=False)
with pytest.raises(TypeError, match=msg):
    gb.rank()
gb2 = df.groupby(cat, observed=False)
with pytest.raises(TypeError, match=msg):
    gb2.rank()
```

## Next Steps


---

*Source: test_rank.py:16 | Complexity: Advanced | Last updated: 2026-06-02*
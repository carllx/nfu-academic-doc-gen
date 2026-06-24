# How To: Combine Generic

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test combine generic

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: float_frame
```

## Step-by-Step Guide

### Step 1: Assign df1 = float_frame

```python
df1 = float_frame
```

**Verification:**
```python
assert combined['D'].isna().all()
```

### Step 2: Assign df2 = value

```python
df2 = float_frame.loc[float_frame.index[:-5], ['A', 'B', 'C']]
```

**Verification:**
```python
assert combined2['D'].isna().all()
```

### Step 3: Assign combined = df1.combine(...)

```python
combined = df1.combine(df2, np.add)
```

### Step 4: Assign combined2 = df2.combine(...)

```python
combined2 = df2.combine(df1, np.add)
```

**Verification:**
```python
assert combined['D'].isna().all()
```

### Step 5: Assign chunk = value

```python
chunk = combined.loc[combined.index[:-5], ['A', 'B', 'C']]
```

### Step 6: Assign chunk2 = value

```python
chunk2 = combined2.loc[combined2.index[:-5], ['A', 'B', 'C']]
```

### Step 7: Assign exp = value

```python
exp = float_frame.loc[float_frame.index[:-5], ['A', 'B', 'C']].reindex_like(chunk) * 2
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(chunk, exp)
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(chunk2, exp)
```


## Complete Example

```python
# Setup
# Fixtures: float_frame

# Workflow
df1 = float_frame
df2 = float_frame.loc[float_frame.index[:-5], ['A', 'B', 'C']]
combined = df1.combine(df2, np.add)
combined2 = df2.combine(df1, np.add)
assert combined['D'].isna().all()
assert combined2['D'].isna().all()
chunk = combined.loc[combined.index[:-5], ['A', 'B', 'C']]
chunk2 = combined2.loc[combined2.index[:-5], ['A', 'B', 'C']]
exp = float_frame.loc[float_frame.index[:-5], ['A', 'B', 'C']].reindex_like(chunk) * 2
tm.assert_frame_equal(chunk, exp)
tm.assert_frame_equal(chunk2, exp)
```

## Next Steps


---

*Source: test_combine.py:30 | Complexity: Advanced | Last updated: 2026-06-02*
# How To: Join Overlap

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test join overlap

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.reshape.concat`

**Setup Required:**
```python
# Fixtures: float_frame
```

## Step-by-Step Guide

### Step 1: Assign df1 = value

```python
df1 = float_frame.loc[:, ['A', 'B', 'C']]
```

### Step 2: Assign df2 = value

```python
df2 = float_frame.loc[:, ['B', 'C', 'D']]
```

### Step 3: Assign joined = df1.join(...)

```python
joined = df1.join(df2, lsuffix='_df1', rsuffix='_df2')
```

### Step 4: Assign df1_suf = unknown.add_suffix(...)

```python
df1_suf = df1.loc[:, ['B', 'C']].add_suffix('_df1')
```

### Step 5: Assign df2_suf = unknown.add_suffix(...)

```python
df2_suf = df2.loc[:, ['B', 'C']].add_suffix('_df2')
```

### Step 6: Assign no_overlap = value

```python
no_overlap = float_frame.loc[:, ['A', 'D']]
```

### Step 7: Assign expected = df1_suf.join.join(...)

```python
expected = df1_suf.join(df2_suf).join(no_overlap)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(joined, expected.loc[:, joined.columns])
```


## Complete Example

```python
# Setup
# Fixtures: float_frame

# Workflow
df1 = float_frame.loc[:, ['A', 'B', 'C']]
df2 = float_frame.loc[:, ['B', 'C', 'D']]
joined = df1.join(df2, lsuffix='_df1', rsuffix='_df2')
df1_suf = df1.loc[:, ['B', 'C']].add_suffix('_df1')
df2_suf = df2.loc[:, ['B', 'C']].add_suffix('_df2')
no_overlap = float_frame.loc[:, ['A', 'D']]
expected = df1_suf.join(df2_suf).join(no_overlap)
tm.assert_frame_equal(joined, expected.loc[:, joined.columns])
```

## Next Steps


---

*Source: test_join.py:335 | Complexity: Advanced | Last updated: 2026-06-02*
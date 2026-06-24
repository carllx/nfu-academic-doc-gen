# How To: Moment Functions Zero Length Pairwise

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test moment functions zero length pairwise

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas`
- `pandas._testing`
- `pandas.core.algorithms`

**Setup Required:**
```python
# Fixtures: f
```

## Step-by-Step Guide

### Step 1: Assign df1 = DataFrame(...)

```python
df1 = DataFrame()
```

### Step 2: Assign df2 = DataFrame(...)

```python
df2 = DataFrame(columns=Index(['a'], name='foo'), index=Index([], name='bar'))
```

### Step 3: Assign unknown = unknown.astype(...)

```python
df2['a'] = df2['a'].astype('float64')
```

### Step 4: Assign df1_expected = DataFrame(...)

```python
df1_expected = DataFrame(index=MultiIndex.from_product([df1.index, df1.columns]))
```

### Step 5: Assign df2_expected = DataFrame(...)

```python
df2_expected = DataFrame(index=MultiIndex.from_product([df2.index, df2.columns], names=['bar', 'foo']), columns=Index(['a'], name='foo'), dtype='float64')
```

### Step 6: Assign df1_result = f(...)

```python
df1_result = f(df1)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df1_result, df1_expected)
```

### Step 8: Assign df2_result = f(...)

```python
df2_result = f(df2)
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df2_result, df2_expected)
```


## Complete Example

```python
# Setup
# Fixtures: f

# Workflow
df1 = DataFrame()
df2 = DataFrame(columns=Index(['a'], name='foo'), index=Index([], name='bar'))
df2['a'] = df2['a'].astype('float64')
df1_expected = DataFrame(index=MultiIndex.from_product([df1.index, df1.columns]))
df2_expected = DataFrame(index=MultiIndex.from_product([df2.index, df2.columns], names=['bar', 'foo']), columns=Index(['a'], name='foo'), dtype='float64')
df1_result = f(df1)
tm.assert_frame_equal(df1_result, df1_expected)
df2_result = f(df2)
tm.assert_frame_equal(df2_result, df2_expected)
```

## Next Steps


---

*Source: test_pairwise.py:201 | Complexity: Advanced | Last updated: 2026-06-02*
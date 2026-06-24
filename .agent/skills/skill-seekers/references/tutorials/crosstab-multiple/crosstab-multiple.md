# How To: Crosstab Multiple

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test crosstab multiple

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: df
```

## Step-by-Step Guide

### Step 1: Assign result = crosstab(...)

```python
result = crosstab(df['A'], [df['B'], df['C']])
```

### Step 2: Assign expected = df.groupby.size(...)

```python
expected = df.groupby(['A', 'B', 'C']).size()
```

### Step 3: Assign expected = expected.unstack.unstack.fillna.astype(...)

```python
expected = expected.unstack('B').unstack('C').fillna(0).astype(np.int64)
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign result = crosstab(...)

```python
result = crosstab([df['B'], df['C']], df['A'])
```

### Step 6: Assign expected = df.groupby.size(...)

```python
expected = df.groupby(['B', 'C', 'A']).size()
```

### Step 7: Assign expected = expected.unstack.fillna.astype(...)

```python
expected = expected.unstack('A').fillna(0).astype(np.int64)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: df

# Workflow
result = crosstab(df['A'], [df['B'], df['C']])
expected = df.groupby(['A', 'B', 'C']).size()
expected = expected.unstack('B').unstack('C').fillna(0).astype(np.int64)
tm.assert_frame_equal(result, expected)
result = crosstab([df['B'], df['C']], df['A'])
expected = df.groupby(['B', 'C', 'A']).size()
expected = expected.unstack('A').fillna(0).astype(np.int64)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_crosstab.py:75 | Complexity: Advanced | Last updated: 2026-06-02*
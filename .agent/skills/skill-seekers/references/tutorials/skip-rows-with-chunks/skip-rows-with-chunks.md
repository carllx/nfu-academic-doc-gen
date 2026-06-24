# How To: Skip Rows With Chunks

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test skip rows with chunks

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `io`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_parsers
```

## Step-by-Step Guide

### Step 1: Assign data = 'col_a\n10\n20\n30\n40\n50\n60\n70\n80\n90\n100\n'

```python
data = 'col_a\n10\n20\n30\n40\n50\n60\n70\n80\n90\n100\n'
```

### Step 2: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 3: Assign reader = parser.read_csv(...)

```python
reader = parser.read_csv(StringIO(data), engine=parser, skiprows=lambda x: x in [1, 4, 5], chunksize=4)
```

### Step 4: Assign df1 = next(...)

```python
df1 = next(reader)
```

### Step 5: Assign df2 = next(...)

```python
df2 = next(reader)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df1, DataFrame({'col_a': [20, 30, 60, 70]}))
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df2, DataFrame({'col_a': [80, 90, 100]}, index=[4, 5, 6]))
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
data = 'col_a\n10\n20\n30\n40\n50\n60\n70\n80\n90\n100\n'
parser = all_parsers
reader = parser.read_csv(StringIO(data), engine=parser, skiprows=lambda x: x in [1, 4, 5], chunksize=4)
df1 = next(reader)
df2 = next(reader)
tm.assert_frame_equal(df1, DataFrame({'col_a': [20, 30, 60, 70]}))
tm.assert_frame_equal(df2, DataFrame({'col_a': [80, 90, 100]}, index=[4, 5, 6]))
```

## Next Steps


---

*Source: test_skiprows.py:312 | Complexity: Intermediate | Last updated: 2026-06-02*
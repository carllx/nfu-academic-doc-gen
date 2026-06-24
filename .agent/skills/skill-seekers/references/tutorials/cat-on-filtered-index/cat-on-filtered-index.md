# How To: Cat On Filtered Index

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test cat on filtered index

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(index=MultiIndex.from_product([[2011, 2012], [1, 2, 3]], names=['year', 'month']))
```

**Verification:**
```python
assert str_both.loc[1] == '2011 2'
```

### Step 2: Assign df = df.reset_index(...)

```python
df = df.reset_index()
```

**Verification:**
```python
assert str_multiple.loc[1] == '2011 2 2'
```

### Step 3: Assign df = value

```python
df = df[df.month > 1]
```

### Step 4: Assign str_year = df.year.astype(...)

```python
str_year = df.year.astype('str')
```

### Step 5: Assign str_month = df.month.astype(...)

```python
str_month = df.month.astype('str')
```

### Step 6: Assign str_both = str_year.str.cat(...)

```python
str_both = str_year.str.cat(str_month, sep=' ')
```

**Verification:**
```python
assert str_both.loc[1] == '2011 2'
```

### Step 7: Assign str_multiple = str_year.str.cat(...)

```python
str_multiple = str_year.str.cat([str_month, str_month], sep=' ')
```

**Verification:**
```python
assert str_multiple.loc[1] == '2011 2 2'
```


## Complete Example

```python
# Workflow
df = DataFrame(index=MultiIndex.from_product([[2011, 2012], [1, 2, 3]], names=['year', 'month']))
df = df.reset_index()
df = df[df.month > 1]
str_year = df.year.astype('str')
str_month = df.month.astype('str')
str_both = str_year.str.cat(str_month, sep=' ')
assert str_both.loc[1] == '2011 2'
str_multiple = str_year.str.cat([str_month, str_month], sep=' ')
assert str_multiple.loc[1] == '2011 2 2'
```

## Next Steps


---

*Source: test_cat.py:386 | Complexity: Intermediate | Last updated: 2026-06-02*
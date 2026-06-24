# How To: Categorical Concat Gh7864

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test categorical concat gh7864

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'id': [1, 2, 3, 4, 5, 6], 'raw_grade': list('abbaae')})
```

### Step 2: Assign unknown = Categorical(...)

```python
df['grade'] = Categorical(df['raw_grade'])
```

### Step 3: Call unknown.cat.set_categories()

```python
df['grade'].cat.set_categories(['e', 'a', 'b'])
```

### Step 4: Assign df1 = value

```python
df1 = df[0:3]
```

### Step 5: Assign df2 = value

```python
df2 = df[3:]
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(df['grade'].cat.categories, df1['grade'].cat.categories)
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(df['grade'].cat.categories, df2['grade'].cat.categories)
```

### Step 8: Assign dfx = pd.concat(...)

```python
dfx = pd.concat([df1, df2])
```

### Step 9: Call tm.assert_index_equal()

```python
tm.assert_index_equal(df['grade'].cat.categories, dfx['grade'].cat.categories)
```

### Step 10: Assign dfa = df1._append(...)

```python
dfa = df1._append(df2)
```

### Step 11: Call tm.assert_index_equal()

```python
tm.assert_index_equal(df['grade'].cat.categories, dfa['grade'].cat.categories)
```


## Complete Example

```python
# Workflow
df = DataFrame({'id': [1, 2, 3, 4, 5, 6], 'raw_grade': list('abbaae')})
df['grade'] = Categorical(df['raw_grade'])
df['grade'].cat.set_categories(['e', 'a', 'b'])
df1 = df[0:3]
df2 = df[3:]
tm.assert_index_equal(df['grade'].cat.categories, df1['grade'].cat.categories)
tm.assert_index_equal(df['grade'].cat.categories, df2['grade'].cat.categories)
dfx = pd.concat([df1, df2])
tm.assert_index_equal(df['grade'].cat.categories, dfx['grade'].cat.categories)
dfa = df1._append(df2)
tm.assert_index_equal(df['grade'].cat.categories, dfa['grade'].cat.categories)
```

## Next Steps


---

*Source: test_categorical.py:202 | Complexity: Advanced | Last updated: 2026-06-02*
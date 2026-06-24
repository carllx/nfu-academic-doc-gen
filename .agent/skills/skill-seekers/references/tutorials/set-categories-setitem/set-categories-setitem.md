# How To: Set Categories Setitem

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test set categories setitem

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.categorical`
- `pandas.core.indexes.accessors`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'Survived': [1, 0, 1], 'Sex': [0, 1, 1]}, dtype='category')
```

**Verification:**
```python
assert list(df['Sex']) == ['female', 'male', 'male']
```

### Step 2: Assign unknown = unknown.cat.rename_categories(...)

```python
df['Survived'] = df['Survived'].cat.rename_categories(['No', 'Yes'])
```

**Verification:**
```python
assert list(df['Survived']) == ['Yes', 'No', 'Yes']
```

### Step 3: Assign unknown = unknown.cat.rename_categories(...)

```python
df['Sex'] = df['Sex'].cat.rename_categories(['female', 'male'])
```

**Verification:**
```python
assert list(df['Sex']) == ['female', 'male', 'male']
```

### Step 4: Assign unknown = Categorical(...)

```python
df['Sex'] = Categorical(df['Sex'], categories=['female', 'male'], ordered=False)
```

**Verification:**
```python
assert list(df['Survived']) == ['Yes', 'No', 'Yes']
```

### Step 5: Assign unknown = Categorical(...)

```python
df['Survived'] = Categorical(df['Survived'], categories=['No', 'Yes'], ordered=False)
```

**Verification:**
```python
assert list(df['Sex']) == ['female', 'male', 'male']
```


## Complete Example

```python
# Workflow
df = DataFrame({'Survived': [1, 0, 1], 'Sex': [0, 1, 1]}, dtype='category')
df['Survived'] = df['Survived'].cat.rename_categories(['No', 'Yes'])
df['Sex'] = df['Sex'].cat.rename_categories(['female', 'male'])
assert list(df['Sex']) == ['female', 'male', 'male']
assert list(df['Survived']) == ['Yes', 'No', 'Yes']
df['Sex'] = Categorical(df['Sex'], categories=['female', 'male'], ordered=False)
df['Survived'] = Categorical(df['Survived'], categories=['No', 'Yes'], ordered=False)
assert list(df['Sex']) == ['female', 'male', 'male']
assert list(df['Survived']) == ['Yes', 'No', 'Yes']
```

## Next Steps


---

*Source: test_cat_accessor.py:230 | Complexity: Intermediate | Last updated: 2026-06-02*
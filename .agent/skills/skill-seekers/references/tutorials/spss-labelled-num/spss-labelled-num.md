# How To: Spss Labelled Num

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test spss labelled num

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `pathlib`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.util.version`
- `pandas.arrays`

**Setup Required:**
```python
# Fixtures: path_klass, datapath
```

## Step-by-Step Guide

### Step 1: Assign fname = path_klass(...)

```python
fname = path_klass(datapath('io', 'data', 'spss', 'labelled-num.sav'))
```

### Step 2: Assign df = pd.read_spss(...)

```python
df = pd.read_spss(fname, convert_categoricals=True)
```

### Step 3: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'VAR00002': 'This is one'}, index=[0])
```

### Step 4: Assign unknown = pd.Categorical(...)

```python
expected['VAR00002'] = pd.Categorical(expected['VAR00002'])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```

### Step 6: Assign df = pd.read_spss(...)

```python
df = pd.read_spss(fname, convert_categoricals=False)
```

### Step 7: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'VAR00002': 1.0}, index=[0])
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```


## Complete Example

```python
# Setup
# Fixtures: path_klass, datapath

# Workflow
fname = path_klass(datapath('io', 'data', 'spss', 'labelled-num.sav'))
df = pd.read_spss(fname, convert_categoricals=True)
expected = pd.DataFrame({'VAR00002': 'This is one'}, index=[0])
expected['VAR00002'] = pd.Categorical(expected['VAR00002'])
tm.assert_frame_equal(df, expected)
df = pd.read_spss(fname, convert_categoricals=False)
expected = pd.DataFrame({'VAR00002': 1.0}, index=[0])
tm.assert_frame_equal(df, expected)
```

## Next Steps


---

*Source: test_spss.py:19 | Complexity: Advanced | Last updated: 2026-06-02*
# How To: Spss Labelled Str

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test spss labelled str

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
# Fixtures: datapath
```

## Step-by-Step Guide

### Step 1: Assign fname = datapath(...)

```python
fname = datapath('io', 'data', 'spss', 'labelled-str.sav')
```

### Step 2: Assign df = pd.read_spss(...)

```python
df = pd.read_spss(fname, convert_categoricals=True)
```

### Step 3: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'gender': ['Male', 'Female']})
```

### Step 4: Assign unknown = pd.Categorical(...)

```python
expected['gender'] = pd.Categorical(expected['gender'])
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
expected = pd.DataFrame({'gender': ['M', 'F']})
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```


## Complete Example

```python
# Setup
# Fixtures: datapath

# Workflow
fname = datapath('io', 'data', 'spss', 'labelled-str.sav')
df = pd.read_spss(fname, convert_categoricals=True)
expected = pd.DataFrame({'gender': ['Male', 'Female']})
expected['gender'] = pd.Categorical(expected['gender'])
tm.assert_frame_equal(df, expected)
df = pd.read_spss(fname, convert_categoricals=False)
expected = pd.DataFrame({'gender': ['M', 'F']})
tm.assert_frame_equal(df, expected)
```

## Next Steps


---

*Source: test_spss.py:53 | Complexity: Advanced | Last updated: 2026-06-02*
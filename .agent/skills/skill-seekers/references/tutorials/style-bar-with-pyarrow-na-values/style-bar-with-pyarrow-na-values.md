# How To: Style Bar With Pyarrow Na Values

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test style bar with pyarrow NA values

## Prerequisites

**Required Modules:**
- `io`
- `numpy`
- `pytest`
- `pandas`


## Step-by-Step Guide

### Step 1: Call pytest.importorskip()

```python
pytest.importorskip('pyarrow')
```

**Verification:**
```python
assert expected_substring in html_output
```

### Step 2: Assign data = 'name,age,test1,test2,teacher\n        Adam,15,95.0,80,Ashby\n        Bob,16,81.0,82,Ashby\n        Dave,16,89.0,84,Jones\n        Fred,15,,88,Jones'

```python
data = 'name,age,test1,test2,teacher\n        Adam,15,95.0,80,Ashby\n        Bob,16,81.0,82,Ashby\n        Dave,16,89.0,84,Jones\n        Fred,15,,88,Jones'
```

### Step 3: Assign df = read_csv(...)

```python
df = read_csv(io.StringIO(data), dtype_backend='pyarrow')
```

### Step 4: Assign expected_substring = 'style type='

```python
expected_substring = 'style type='
```

### Step 5: Assign html_output = df.style.bar.to_html(...)

```python
html_output = df.style.bar(subset='test1').to_html()
```

**Verification:**
```python
assert expected_substring in html_output
```


## Complete Example

```python
# Workflow
pytest.importorskip('pyarrow')
data = 'name,age,test1,test2,teacher\n        Adam,15,95.0,80,Ashby\n        Bob,16,81.0,82,Ashby\n        Dave,16,89.0,84,Jones\n        Fred,15,,88,Jones'
df = read_csv(io.StringIO(data), dtype_backend='pyarrow')
expected_substring = 'style type='
html_output = df.style.bar(subset='test1').to_html()
assert expected_substring in html_output
```

## Next Steps


---

*Source: test_bar.py:349 | Complexity: Intermediate | Last updated: 2026-06-02*
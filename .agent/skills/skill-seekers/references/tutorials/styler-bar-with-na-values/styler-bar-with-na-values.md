# How To: Styler Bar With Na Values

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test styler bar with NA values

## Prerequisites

**Required Modules:**
- `io`
- `numpy`
- `pytest`
- `pandas`


## Step-by-Step Guide

### Step 1: Assign df1 = DataFrame(...)

```python
df1 = DataFrame({'A': [1, 2, NA, 4]})
```

**Verification:**
```python
assert expected_substring in html_output1
```

### Step 2: Assign df2 = DataFrame(...)

```python
df2 = DataFrame([[NA, NA], [NA, NA]])
```

**Verification:**
```python
assert expected_substring in html_output2
```

### Step 3: Assign expected_substring = 'style type='

```python
expected_substring = 'style type='
```

### Step 4: Assign html_output1 = df1.style.bar.to_html(...)

```python
html_output1 = df1.style.bar(subset='A').to_html()
```

### Step 5: Assign html_output2 = df2.style.bar.to_html(...)

```python
html_output2 = df2.style.bar(align='left', axis=None).to_html()
```

**Verification:**
```python
assert expected_substring in html_output1
```


## Complete Example

```python
# Workflow
df1 = DataFrame({'A': [1, 2, NA, 4]})
df2 = DataFrame([[NA, NA], [NA, NA]])
expected_substring = 'style type='
html_output1 = df1.style.bar(subset='A').to_html()
html_output2 = df2.style.bar(align='left', axis=None).to_html()
assert expected_substring in html_output1
assert expected_substring in html_output2
```

## Next Steps


---

*Source: test_bar.py:339 | Complexity: Intermediate | Last updated: 2026-06-02*
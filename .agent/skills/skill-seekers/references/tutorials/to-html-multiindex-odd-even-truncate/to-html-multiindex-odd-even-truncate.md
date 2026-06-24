# How To: To Html Multiindex Odd Even Truncate

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test to html multiindex odd even truncate

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `io`
- `itertools`
- `re`
- `textwrap`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.io.formats.format`

**Setup Required:**
```python
# Fixtures: max_rows, expected, datapath
```

## Step-by-Step Guide

### Step 1: Assign index = MultiIndex.from_product(...)

```python
index = MultiIndex.from_product([[100, 200, 300], [10, 20, 30], [1, 2, 3, 4, 5, 6, 7]], names=['a', 'b', 'c'])
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'n': range(len(index))}, index=index)
```

### Step 3: Assign result = df.to_html(...)

```python
result = df.to_html(max_rows=max_rows)
```

### Step 4: Assign expected = expected_html(...)

```python
expected = expected_html(datapath, expected)
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Setup
# Fixtures: max_rows, expected, datapath

# Workflow
index = MultiIndex.from_product([[100, 200, 300], [10, 20, 30], [1, 2, 3, 4, 5, 6, 7]], names=['a', 'b', 'c'])
df = DataFrame({'n': range(len(index))}, index=index)
result = df.to_html(max_rows=max_rows)
expected = expected_html(datapath, expected)
assert result == expected
```

## Next Steps


---

*Source: test_to_html.py:226 | Complexity: Intermediate | Last updated: 2026-06-02*
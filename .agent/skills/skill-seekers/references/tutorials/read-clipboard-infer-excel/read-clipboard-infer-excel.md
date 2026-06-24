# How To: Read Clipboard Infer Excel

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test read clipboard infer excel

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `textwrap`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.io.clipboard`
- `pandas.arrays`

**Setup Required:**
```python
# Fixtures: clipboard
```

## Step-by-Step Guide

### Step 1: Assign clip_kwargs = value

```python
clip_kwargs = {'engine': 'python'}
```

**Verification:**
```python
assert df.iloc[1, 1] == 'Harry Carney'
```

### Step 2: Assign text = dedent(...)

```python
text = dedent('\n            John James\tCharlie Mingus\n            1\t2\n            4\tHarry Carney\n            '.strip())
```

### Step 3: Call clipboard.setText()

```python
clipboard.setText(text)
```

### Step 4: Assign df = read_clipboard(...)

```python
df = read_clipboard(**clip_kwargs)
```

**Verification:**
```python
assert df.iloc[1, 1] == 'Harry Carney'
```

### Step 5: Assign text = dedent(...)

```python
text = dedent('\n            a\t b\n            1  2\n            3  4\n            '.strip())
```

### Step 6: Call clipboard.setText()

```python
clipboard.setText(text)
```

### Step 7: Assign res = read_clipboard(...)

```python
res = read_clipboard(**clip_kwargs)
```

### Step 8: Assign text = dedent(...)

```python
text = dedent('\n            a  b\n            1  2\n            3  4\n            '.strip())
```

### Step 9: Call clipboard.setText()

```python
clipboard.setText(text)
```

### Step 10: Assign exp = read_clipboard(...)

```python
exp = read_clipboard(**clip_kwargs)
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, exp)
```


## Complete Example

```python
# Setup
# Fixtures: clipboard

# Workflow
clip_kwargs = {'engine': 'python'}
text = dedent('\n            John James\tCharlie Mingus\n            1\t2\n            4\tHarry Carney\n            '.strip())
clipboard.setText(text)
df = read_clipboard(**clip_kwargs)
assert df.iloc[1, 1] == 'Harry Carney'
text = dedent('\n            a\t b\n            1  2\n            3  4\n            '.strip())
clipboard.setText(text)
res = read_clipboard(**clip_kwargs)
text = dedent('\n            a  b\n            1  2\n            3  4\n            '.strip())
clipboard.setText(text)
exp = read_clipboard(**clip_kwargs)
tm.assert_frame_equal(res, exp)
```

## Next Steps


---

*Source: test_clipboard.py:242 | Complexity: Advanced | Last updated: 2026-06-02*
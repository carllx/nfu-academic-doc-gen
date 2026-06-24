# How To: Emoji Tokenizer

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test a string that contains Emoji ZWJ Sequences and skin tone modifier

## Prerequisites

**Required Modules:**
- `typing`
- `pytest`
- `nltk.tokenize`
- `nltk.tokenize.simple`
- `nltk.corpus`


## Step-by-Step Guide

### Step 1: '\n        Test a string that contains Emoji ZWJ Sequences and skin tone modifier\n        '

```python
'\n        Test a string that contains Emoji ZWJ Sequences and skin tone modifier\n        '
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign tokenizer = TweetTokenizer(...)

```python
tokenizer = TweetTokenizer()
```

**Verification:**
```python
assert result == expected
```

### Step 3: Assign test1 = '👨\u200d👩\u200d👧\u200d👧'

```python
test1 = '👨\u200d👩\u200d👧\u200d👧'
```

**Verification:**
```python
assert result == expected
```

### Step 4: Assign expected = value

```python
expected = ['👨\u200d👩\u200d👧\u200d👧']
```

**Verification:**
```python
assert result == expected
```

### Step 5: Assign result = tokenizer.tokenize(...)

```python
result = tokenizer.tokenize(test1)
```

**Verification:**
```python
assert result == expected
```

### Step 6: Assign test2 = '👨🏿'

```python
test2 = '👨🏿'
```

**Verification:**
```python
assert result == expected
```

### Step 7: Assign expected = value

```python
expected = ['👨🏿']
```

### Step 8: Assign result = tokenizer.tokenize(...)

```python
result = tokenizer.tokenize(test2)
```

**Verification:**
```python
assert result == expected
```

### Step 9: Assign test3 = '🤔 🙈 me así, se😌 ds 💕👭👙 hello 👩🏾\u200d🎓 emoji hello 👨\u200d👩\u200d👦\u200d👦 how are 😊 you today🙅🏽🙅🏽'

```python
test3 = '🤔 🙈 me así, se😌 ds 💕👭👙 hello 👩🏾\u200d🎓 emoji hello 👨\u200d👩\u200d👦\u200d👦 how are 😊 you today🙅🏽🙅🏽'
```

### Step 10: Assign expected = value

```python
expected = ['🤔', '🙈', 'me', 'así', ',', 'se', '😌', 'ds', '💕', '👭', '👙', 'hello', '👩🏾\u200d🎓', 'emoji', 'hello', '👨\u200d👩\u200d👦\u200d👦', 'how', 'are', '😊', 'you', 'today', '🙅🏽', '🙅🏽']
```

### Step 11: Assign result = tokenizer.tokenize(...)

```python
result = tokenizer.tokenize(test3)
```

**Verification:**
```python
assert result == expected
```

### Step 12: Assign test4 = '🇦🇵🇵🇱🇪'

```python
test4 = '🇦🇵🇵🇱🇪'
```

### Step 13: Assign expected = value

```python
expected = ['🇦🇵', '🇵🇱', '🇪']
```

### Step 14: Assign result = tokenizer.tokenize(...)

```python
result = tokenizer.tokenize(test4)
```

**Verification:**
```python
assert result == expected
```

### Step 15: Assign test5 = 'Hi 🇨🇦, 😍!!'

```python
test5 = 'Hi 🇨🇦, 😍!!'
```

### Step 16: Assign expected = value

```python
expected = ['Hi', '🇨🇦', ',', '😍', '!', '!']
```

### Step 17: Assign result = tokenizer.tokenize(...)

```python
result = tokenizer.tokenize(test5)
```

**Verification:**
```python
assert result == expected
```

### Step 18: Assign test6 = '<3 🇨🇦 🤝 🇵🇱 <3'

```python
test6 = '<3 🇨🇦 🤝 🇵🇱 <3'
```

### Step 19: Assign expected = value

```python
expected = ['<3', '🇨🇦', '🤝', '🇵🇱', '<3']
```

### Step 20: Assign result = tokenizer.tokenize(...)

```python
result = tokenizer.tokenize(test6)
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Workflow
'\n        Test a string that contains Emoji ZWJ Sequences and skin tone modifier\n        '
tokenizer = TweetTokenizer()
test1 = '👨\u200d👩\u200d👧\u200d👧'
expected = ['👨\u200d👩\u200d👧\u200d👧']
result = tokenizer.tokenize(test1)
assert result == expected
test2 = '👨🏿'
expected = ['👨🏿']
result = tokenizer.tokenize(test2)
assert result == expected
test3 = '🤔 🙈 me así, se😌 ds 💕👭👙 hello 👩🏾\u200d🎓 emoji hello 👨\u200d👩\u200d👦\u200d👦 how are 😊 you today🙅🏽🙅🏽'
expected = ['🤔', '🙈', 'me', 'así', ',', 'se', '😌', 'ds', '💕', '👭', '👙', 'hello', '👩🏾\u200d🎓', 'emoji', 'hello', '👨\u200d👩\u200d👦\u200d👦', 'how', 'are', '😊', 'you', 'today', '🙅🏽', '🙅🏽']
result = tokenizer.tokenize(test3)
assert result == expected
test4 = '🇦🇵🇵🇱🇪'
expected = ['🇦🇵', '🇵🇱', '🇪']
result = tokenizer.tokenize(test4)
assert result == expected
test5 = 'Hi 🇨🇦, 😍!!'
expected = ['Hi', '🇨🇦', ',', '😍', '!', '!']
result = tokenizer.tokenize(test5)
assert result == expected
test6 = '<3 🇨🇦 🤝 🇵🇱 <3'
expected = ['<3', '🇨🇦', '🤝', '🇵🇱', '<3']
result = tokenizer.tokenize(test6)
assert result == expected
```

## Next Steps


---

*Source: test_tokenize.py:356 | Complexity: Advanced | Last updated: 2026-06-02*
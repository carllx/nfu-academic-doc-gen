# How To: Tokenize

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: unittest, mock, workflow, integration

## Overview

Workflow: test tokenize

## Prerequisites

**Required Modules:**
- `unittest`
- `unittest.mock`
- `pytest`
- `nltk.parse`
- `nltk.tree`


## Step-by-Step Guide

### Step 1: Assign corenlp_tokenizer = corenlp.CoreNLPParser(...)

```python
corenlp_tokenizer = corenlp.CoreNLPParser()
```

### Step 2: Assign api_return_value = value

```python
api_return_value = {'sentences': [{'index': 0, 'tokens': [{'after': ' ', 'before': '', 'characterOffsetBegin': 0, 'characterOffsetEnd': 4, 'index': 1, 'originalText': 'Good', 'word': 'Good'}, {'after': ' ', 'before': ' ', 'characterOffsetBegin': 5, 'characterOffsetEnd': 12, 'index': 2, 'originalText': 'muffins', 'word': 'muffins'}, {'after': ' ', 'before': ' ', 'characterOffsetBegin': 13, 'characterOffsetEnd': 17, 'index': 3, 'originalText': 'cost', 'word': 'cost'}, {'after': '', 'before': ' ', 'characterOffsetBegin': 18, 'characterOffsetEnd': 19, 'index': 4, 'originalText': '$', 'word': '$'}, {'after': '\n', 'before': '', 'characterOffsetBegin': 19, 'characterOffsetEnd': 23, 'index': 5, 'originalText': '3.88', 'word': '3.88'}, {'after': ' ', 'before': '\n', 'characterOffsetBegin': 24, 'characterOffsetEnd': 26, 'index': 6, 'originalText': 'in', 'word': 'in'}, {'after': ' ', 'before': ' ', 'characterOffsetBegin': 27, 'characterOffsetEnd': 30, 'index': 7, 'originalText': 'New', 'word': 'New'}, {'after': '', 'before': ' ', 'characterOffsetBegin': 31, 'characterOffsetEnd': 35, 'index': 8, 'originalText': 'York', 'word': 'York'}, {'after': '  ', 'before': '', 'characterOffsetBegin': 35, 'characterOffsetEnd': 36, 'index': 9, 'originalText': '.', 'word': '.'}]}, {'index': 1, 'tokens': [{'after': ' ', 'before': '  ', 'characterOffsetBegin': 38, 'characterOffsetEnd': 44, 'index': 1, 'originalText': 'Please', 'word': 'Please'}, {'after': ' ', 'before': ' ', 'characterOffsetBegin': 45, 'characterOffsetEnd': 48, 'index': 2, 'originalText': 'buy', 'word': 'buy'}, {'after': '\n', 'before': ' ', 'characterOffsetBegin': 49, 'characterOffsetEnd': 51, 'index': 3, 'originalText': 'me', 'word': 'me'}, {'after': ' ', 'before': '\n', 'characterOffsetBegin': 52, 'characterOffsetEnd': 55, 'index': 4, 'originalText': 'two', 'word': 'two'}, {'after': ' ', 'before': ' ', 'characterOffsetBegin': 56, 'characterOffsetEnd': 58, 'index': 5, 'originalText': 'of', 'word': 'of'}, {'after': '', 'before': ' ', 'characterOffsetBegin': 59, 'characterOffsetEnd': 63, 'index': 6, 'originalText': 'them', 'word': 'them'}, {'after': '\n', 'before': '', 'characterOffsetBegin': 63, 'characterOffsetEnd': 64, 'index': 7, 'originalText': '.', 'word': '.'}]}, {'index': 2, 'tokens': [{'after': '', 'before': '\n', 'characterOffsetBegin': 65, 'characterOffsetEnd': 71, 'index': 1, 'originalText': 'Thanks', 'word': 'Thanks'}, {'after': '', 'before': '', 'characterOffsetBegin': 71, 'characterOffsetEnd': 72, 'index': 2, 'originalText': '.', 'word': '.'}]}]}
```

### Step 3: Assign corenlp_tokenizer.api_call = MagicMock(...)

```python
corenlp_tokenizer.api_call = MagicMock(return_value=api_return_value)
```

### Step 4: Assign input_string = 'Good muffins cost $3.88\nin New York.  Please buy me\ntwo of them.\nThanks.'

```python
input_string = 'Good muffins cost $3.88\nin New York.  Please buy me\ntwo of them.\nThanks.'
```

### Step 5: Assign expected_output = value

```python
expected_output = ['Good', 'muffins', 'cost', '$', '3.88', 'in', 'New', 'York', '.', 'Please', 'buy', 'me', 'two', 'of', 'them', '.', 'Thanks', '.']
```

### Step 6: Assign tokenized_output = list(...)

```python
tokenized_output = list(corenlp_tokenizer.tokenize(input_string))
```

### Step 7: Call corenlp_tokenizer.api_call.assert_called_once_with()

```python
corenlp_tokenizer.api_call.assert_called_once_with('Good muffins cost $3.88\nin New York.  Please buy me\ntwo of them.\nThanks.', properties={'annotators': 'tokenize,ssplit'})
```

### Step 8: Call self.assertEqual()

```python
self.assertEqual(expected_output, tokenized_output)
```


## Complete Example

```python
# Workflow
corenlp_tokenizer = corenlp.CoreNLPParser()
api_return_value = {'sentences': [{'index': 0, 'tokens': [{'after': ' ', 'before': '', 'characterOffsetBegin': 0, 'characterOffsetEnd': 4, 'index': 1, 'originalText': 'Good', 'word': 'Good'}, {'after': ' ', 'before': ' ', 'characterOffsetBegin': 5, 'characterOffsetEnd': 12, 'index': 2, 'originalText': 'muffins', 'word': 'muffins'}, {'after': ' ', 'before': ' ', 'characterOffsetBegin': 13, 'characterOffsetEnd': 17, 'index': 3, 'originalText': 'cost', 'word': 'cost'}, {'after': '', 'before': ' ', 'characterOffsetBegin': 18, 'characterOffsetEnd': 19, 'index': 4, 'originalText': '$', 'word': '$'}, {'after': '\n', 'before': '', 'characterOffsetBegin': 19, 'characterOffsetEnd': 23, 'index': 5, 'originalText': '3.88', 'word': '3.88'}, {'after': ' ', 'before': '\n', 'characterOffsetBegin': 24, 'characterOffsetEnd': 26, 'index': 6, 'originalText': 'in', 'word': 'in'}, {'after': ' ', 'before': ' ', 'characterOffsetBegin': 27, 'characterOffsetEnd': 30, 'index': 7, 'originalText': 'New', 'word': 'New'}, {'after': '', 'before': ' ', 'characterOffsetBegin': 31, 'characterOffsetEnd': 35, 'index': 8, 'originalText': 'York', 'word': 'York'}, {'after': '  ', 'before': '', 'characterOffsetBegin': 35, 'characterOffsetEnd': 36, 'index': 9, 'originalText': '.', 'word': '.'}]}, {'index': 1, 'tokens': [{'after': ' ', 'before': '  ', 'characterOffsetBegin': 38, 'characterOffsetEnd': 44, 'index': 1, 'originalText': 'Please', 'word': 'Please'}, {'after': ' ', 'before': ' ', 'characterOffsetBegin': 45, 'characterOffsetEnd': 48, 'index': 2, 'originalText': 'buy', 'word': 'buy'}, {'after': '\n', 'before': ' ', 'characterOffsetBegin': 49, 'characterOffsetEnd': 51, 'index': 3, 'originalText': 'me', 'word': 'me'}, {'after': ' ', 'before': '\n', 'characterOffsetBegin': 52, 'characterOffsetEnd': 55, 'index': 4, 'originalText': 'two', 'word': 'two'}, {'after': ' ', 'before': ' ', 'characterOffsetBegin': 56, 'characterOffsetEnd': 58, 'index': 5, 'originalText': 'of', 'word': 'of'}, {'after': '', 'before': ' ', 'characterOffsetBegin': 59, 'characterOffsetEnd': 63, 'index': 6, 'originalText': 'them', 'word': 'them'}, {'after': '\n', 'before': '', 'characterOffsetBegin': 63, 'characterOffsetEnd': 64, 'index': 7, 'originalText': '.', 'word': '.'}]}, {'index': 2, 'tokens': [{'after': '', 'before': '\n', 'characterOffsetBegin': 65, 'characterOffsetEnd': 71, 'index': 1, 'originalText': 'Thanks', 'word': 'Thanks'}, {'after': '', 'before': '', 'characterOffsetBegin': 71, 'characterOffsetEnd': 72, 'index': 2, 'originalText': '.', 'word': '.'}]}]}
corenlp_tokenizer.api_call = MagicMock(return_value=api_return_value)
input_string = 'Good muffins cost $3.88\nin New York.  Please buy me\ntwo of them.\nThanks.'
expected_output = ['Good', 'muffins', 'cost', '$', '3.88', 'in', 'New', 'York', '.', 'Please', 'buy', 'me', 'two', 'of', 'them', '.', 'Thanks', '.']
tokenized_output = list(corenlp_tokenizer.tokenize(input_string))
corenlp_tokenizer.api_call.assert_called_once_with('Good muffins cost $3.88\nin New York.  Please buy me\ntwo of them.\nThanks.', properties={'annotators': 'tokenize,ssplit'})
self.assertEqual(expected_output, tokenized_output)
```

## Next Steps


---

*Source: test_corenlp.py:37 | Complexity: Advanced | Last updated: 2026-06-02*
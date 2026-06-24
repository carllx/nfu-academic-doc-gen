# How To: Ner Tagger

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: unittest, mock, workflow, integration

## Overview

Workflow: test ner tagger

## Prerequisites

**Required Modules:**
- `unittest`
- `unittest.mock`
- `pytest`
- `nltk.parse`
- `nltk.tree`


## Step-by-Step Guide

### Step 1: Assign corenlp_tagger = corenlp.CoreNLPParser(...)

```python
corenlp_tagger = corenlp.CoreNLPParser(tagtype='ner')
```

### Step 2: Assign api_return_value = value

```python
api_return_value = {'sentences': [{'index': 0, 'tokens': [{'after': ' ', 'before': '', 'characterOffsetBegin': 0, 'characterOffsetEnd': 4, 'index': 1, 'lemma': 'Rami', 'ner': 'PERSON', 'originalText': 'Rami', 'pos': 'NNP', 'word': 'Rami'}, {'after': ' ', 'before': ' ', 'characterOffsetBegin': 5, 'characterOffsetEnd': 8, 'index': 2, 'lemma': 'Eid', 'ner': 'PERSON', 'originalText': 'Eid', 'pos': 'NNP', 'word': 'Eid'}, {'after': ' ', 'before': ' ', 'characterOffsetBegin': 9, 'characterOffsetEnd': 11, 'index': 3, 'lemma': 'be', 'ner': 'O', 'originalText': 'is', 'pos': 'VBZ', 'word': 'is'}, {'after': ' ', 'before': ' ', 'characterOffsetBegin': 12, 'characterOffsetEnd': 20, 'index': 4, 'lemma': 'study', 'ner': 'O', 'originalText': 'studying', 'pos': 'VBG', 'word': 'studying'}, {'after': ' ', 'before': ' ', 'characterOffsetBegin': 21, 'characterOffsetEnd': 23, 'index': 5, 'lemma': 'at', 'ner': 'O', 'originalText': 'at', 'pos': 'IN', 'word': 'at'}, {'after': ' ', 'before': ' ', 'characterOffsetBegin': 24, 'characterOffsetEnd': 29, 'index': 6, 'lemma': 'Stony', 'ner': 'ORGANIZATION', 'originalText': 'Stony', 'pos': 'NNP', 'word': 'Stony'}, {'after': ' ', 'before': ' ', 'characterOffsetBegin': 30, 'characterOffsetEnd': 35, 'index': 7, 'lemma': 'Brook', 'ner': 'ORGANIZATION', 'originalText': 'Brook', 'pos': 'NNP', 'word': 'Brook'}, {'after': ' ', 'before': ' ', 'characterOffsetBegin': 36, 'characterOffsetEnd': 46, 'index': 8, 'lemma': 'University', 'ner': 'ORGANIZATION', 'originalText': 'University', 'pos': 'NNP', 'word': 'University'}, {'after': ' ', 'before': ' ', 'characterOffsetBegin': 47, 'characterOffsetEnd': 49, 'index': 9, 'lemma': 'in', 'ner': 'O', 'originalText': 'in', 'pos': 'IN', 'word': 'in'}, {'after': '', 'before': ' ', 'characterOffsetBegin': 50, 'characterOffsetEnd': 52, 'index': 10, 'lemma': 'NY', 'ner': 'O', 'originalText': 'NY', 'pos': 'NNP', 'word': 'NY'}]}]}
```

### Step 3: Assign corenlp_tagger.api_call = MagicMock(...)

```python
corenlp_tagger.api_call = MagicMock(return_value=api_return_value)
```

### Step 4: Assign input_tokens = unknown.split(...)

```python
input_tokens = 'Rami Eid is studying at Stony Brook University in NY'.split()
```

### Step 5: Assign expected_output = value

```python
expected_output = [('Rami', 'PERSON'), ('Eid', 'PERSON'), ('is', 'O'), ('studying', 'O'), ('at', 'O'), ('Stony', 'ORGANIZATION'), ('Brook', 'ORGANIZATION'), ('University', 'ORGANIZATION'), ('in', 'O'), ('NY', 'O')]
```

### Step 6: Assign tagged_output = corenlp_tagger.tag(...)

```python
tagged_output = corenlp_tagger.tag(input_tokens)
```

### Step 7: Call corenlp_tagger.api_call.assert_called_once_with()

```python
corenlp_tagger.api_call.assert_called_once_with('Rami Eid is studying at Stony Brook University in NY', properties={'ssplit.isOneSentence': 'true', 'annotators': 'tokenize,ssplit,ner', 'tokenize.whitespace': 'true', 'ner.useSUTime': 'false'})
```

### Step 8: Call self.assertEqual()

```python
self.assertEqual(expected_output, tagged_output)
```


## Complete Example

```python
# Workflow
corenlp_tagger = corenlp.CoreNLPParser(tagtype='ner')
api_return_value = {'sentences': [{'index': 0, 'tokens': [{'after': ' ', 'before': '', 'characterOffsetBegin': 0, 'characterOffsetEnd': 4, 'index': 1, 'lemma': 'Rami', 'ner': 'PERSON', 'originalText': 'Rami', 'pos': 'NNP', 'word': 'Rami'}, {'after': ' ', 'before': ' ', 'characterOffsetBegin': 5, 'characterOffsetEnd': 8, 'index': 2, 'lemma': 'Eid', 'ner': 'PERSON', 'originalText': 'Eid', 'pos': 'NNP', 'word': 'Eid'}, {'after': ' ', 'before': ' ', 'characterOffsetBegin': 9, 'characterOffsetEnd': 11, 'index': 3, 'lemma': 'be', 'ner': 'O', 'originalText': 'is', 'pos': 'VBZ', 'word': 'is'}, {'after': ' ', 'before': ' ', 'characterOffsetBegin': 12, 'characterOffsetEnd': 20, 'index': 4, 'lemma': 'study', 'ner': 'O', 'originalText': 'studying', 'pos': 'VBG', 'word': 'studying'}, {'after': ' ', 'before': ' ', 'characterOffsetBegin': 21, 'characterOffsetEnd': 23, 'index': 5, 'lemma': 'at', 'ner': 'O', 'originalText': 'at', 'pos': 'IN', 'word': 'at'}, {'after': ' ', 'before': ' ', 'characterOffsetBegin': 24, 'characterOffsetEnd': 29, 'index': 6, 'lemma': 'Stony', 'ner': 'ORGANIZATION', 'originalText': 'Stony', 'pos': 'NNP', 'word': 'Stony'}, {'after': ' ', 'before': ' ', 'characterOffsetBegin': 30, 'characterOffsetEnd': 35, 'index': 7, 'lemma': 'Brook', 'ner': 'ORGANIZATION', 'originalText': 'Brook', 'pos': 'NNP', 'word': 'Brook'}, {'after': ' ', 'before': ' ', 'characterOffsetBegin': 36, 'characterOffsetEnd': 46, 'index': 8, 'lemma': 'University', 'ner': 'ORGANIZATION', 'originalText': 'University', 'pos': 'NNP', 'word': 'University'}, {'after': ' ', 'before': ' ', 'characterOffsetBegin': 47, 'characterOffsetEnd': 49, 'index': 9, 'lemma': 'in', 'ner': 'O', 'originalText': 'in', 'pos': 'IN', 'word': 'in'}, {'after': '', 'before': ' ', 'characterOffsetBegin': 50, 'characterOffsetEnd': 52, 'index': 10, 'lemma': 'NY', 'ner': 'O', 'originalText': 'NY', 'pos': 'NNP', 'word': 'NY'}]}]}
corenlp_tagger.api_call = MagicMock(return_value=api_return_value)
input_tokens = 'Rami Eid is studying at Stony Brook University in NY'.split()
expected_output = [('Rami', 'PERSON'), ('Eid', 'PERSON'), ('is', 'O'), ('studying', 'O'), ('at', 'O'), ('Stony', 'ORGANIZATION'), ('Brook', 'ORGANIZATION'), ('University', 'ORGANIZATION'), ('in', 'O'), ('NY', 'O')]
tagged_output = corenlp_tagger.tag(input_tokens)
corenlp_tagger.api_call.assert_called_once_with('Rami Eid is studying at Stony Brook University in NY', properties={'ssplit.isOneSentence': 'true', 'annotators': 'tokenize,ssplit,ner', 'tokenize.whitespace': 'true', 'ner.useSUTime': 'false'})
self.assertEqual(expected_output, tagged_output)
```

## Next Steps


---

*Source: test_corenlp.py:590 | Complexity: Advanced | Last updated: 2026-06-02*
# HW#32 Solution

## Introduce module "text_sklearn_model.py" with class TextModel containing the following

### constructor (**init**) taking string with sentences separated by dot

### method getAnswers(self, question: str, nAnswers: int)->list[str]

takes string with question sentence and number of relevant answers<br>
returns list of strings-answers (maximal number of strings is the given nAnswers value) sorted by similarity (relevance) to the answer in the descending order<br>

### Note: result should contain only sentences with non-zero similarity. If no such sentences, the empty list should be returned

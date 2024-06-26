# Report for Assignment 1

## Project chosen

Name: Shapely

URL: https://github.com/shapely/shapely

Number of lines of code and the tool used to count it: 25027 tokei

Programming language: Python

## Coverage measurement

### Existing tool - coverage.py

The coverage tool executed on the project is [coverage.py](https://coverage.readthedocs.io/en/latest/index.html).

The tool can be executed through the following steps (note that you need Python 3.x installed):

1. **Clone the repository**
```bash
git clone https://github.com/Papajo-boban/shapely.git
cd shapely
```
2. **Create a virtual environment**
```bash
python3 -m venv .venv
```
3. **Activate virtual environment**
```bash
source .venv/bin/activate # for Unix/macOS
.venv\Scripts\activate.bat # for windows
```
4. **Install project and test dependencies**
```bash
pip install -e .
pip install pytest coverage matplotlib # matplotlib was needed as some tests were automatically skipped without it
```
5. **Run the tests using coverage.py**
```bash
coverage run -m pytest
```
6. **Create html coverage information and open it in your browser**
```bash
coverage html
```

7. **Result**

### Your own coverage tool

#### 3. Barnabas Kalmar

 Function 1: git_get_keywords
 
 Function 2: render_pep440_branch

 Coverage results:
 

 ![alt text](<Screenshots/Screenshot 2024-06-22 155237.png>)
 The coverage is 0 for both functions

## Coverage improvement

### Individual tests

#### 3. Barnabas Kalmar

Test 1 : test_git_get_keywords_all,test_git_get_keywords_none

Test 2 :  test_render_pep440_branch_clean,test_render_pep440_branch_dirty, test_render_pep440_branch_no_tags_clean,
 test_render_pep440_no_tags_dirty

 
 Test 1

 ![alt text](<Screenshots/Screenshot 2024-06-22 160350.png>)

 Test 2

 ![alt text](<Screenshots/Screenshot 2024-06-22 160417.png>)

 Before:

 ![alt text](<Screenshots/Screenshot 2024-06-22 155237.png>)

 After:

 ![alt text](<Screenshots/Screenshot 2024-06-22 143359.png>)

  The coverage improved from 0 to 86% for both test functions



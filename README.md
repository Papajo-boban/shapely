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

<img width="1355" alt="Screenshot 2024-06-07 at 15 30 43" src="https://github.com/Papajo-boban/shapely/assets/134519958/f66d2f91-a251-4718-880d-c556f777512e">

### Your own coverage tool

<The following is supposed to be repeated for each group member>

<Group member name>

<Function 1 name>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements>

<Provide a screenshot of the coverage results output by the instrumentation>

<Function 2 name>

<Provide the same kind of information provided for Function 1>

## Coverage improvement

### Individual tests

<The following is supposed to be repeated for each group member>

<Group member name>

<Test 1>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test>

<Provide a screenshot of the old coverage results (the same as you already showed above)>

<Provide a screenshot of the new coverage results>

<State the coverage improvement with a number and elaborate on why the coverage is improved>

<Test 2>

<Provide the same kind of information provided for Test 1>

### Overall

<Provide a screenshot of the old coverage results by running an existing tool (the same as you already showed above)>

<Provide a screenshot of the new coverage results by running the existing tool using all test modifications made by the group>

## Statement of individual contributions

<Write what each group member did>

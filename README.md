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

#### 1. Levente Szabó

* Function 1: `versions_from_parent_dir`

* Function 2: `get_versions` 

Commit [3f36a45](https://github.com/Papajo-boban/shapely/commit/3f36a4572a07c086d23f273623df349281e9176d) creates the CoverageTracker class, and commit [a7b54e6](https://github.com/Papajo-boban/shapely/commit/a7b54e625f1406bc9cb63f64b2b8b080ace2444c) instruments both functions. The coverage tool can be executed by running the `cov_info.sh` script located in the `shapely/cov_tracker_levi/` directory.

Coverage results:

<img width="426" alt="Screenshot 2024-06-08 at 17 32 05" src="https://github.com/Papajo-boban/shapely/assets/134519958/b9a489d6-374a-4526-959a-1bf6bcd0d99a">

## Coverage improvement

### Individual tests

#### 1. Levente Szabó

>***Note:*** *I misunderstood and thought we had to write tests that cover all branches of the 2 chosen functions, that's why I created more than 2 tests.*

**Test 1**: `test_versions_from_parentdir_success`, `test_versions_from_parentdir_fail`, `test_versions_from_parentdir_verbose`

Commit [f004d92](https://github.com/Papajo-boban/shapely/commit/f004d9242c0590f7a7f914dcec1f1a53c8bdd2b9) contains these changes.

The coverage of this function improved from 0 to 100% as none of the function branches were covered by the existing tests.

**Test 2**: `test_get_versions_name_error`, `test_get_versions_not_this_method`, `test_get_versions_parentdir_success`

Commit [e80fbc4](https://github.com/Papajo-boban/shapely/commit/e80fbc43450f6ead5a4e37aaae273e39492d7afe) contains these changes.

The coverage of this function improved from 33% (40% according to coverage.py) to 100% as some of the exceptions and branches were not covered by the existing tests before. Specifically, the NameError exception, the second NotThisMethod exception, and the last try catch block and return statement were not covered as can be seen on the following screenshot from coverage.py:

<img width="462" alt="Screenshot 2024-06-08 at 19 06 38" src="https://github.com/Papajo-boban/shapely/assets/134519958/763bcf9e-07f2-4f72-8272-5662019f3464">


The three test cases cover these branches.

**Coverage results**
* Before
 
  <img width="426" alt="Screenshot 2024-06-08 at 17 32 05" src="https://github.com/Papajo-boban/shapely/assets/134519958/b9a489d6-374a-4526-959a-1bf6bcd0d99a">
  
* After
  
  <img width="428" alt="Screenshot 2024-06-08 at 19 42 12" src="https://github.com/Papajo-boban/shapely/assets/134519958/1c3449f9-e1f1-4a99-bd04-c23210ae79c2">


### Overall

<Provide a screenshot of the old coverage results by running an existing tool (the same as you already showed above)>

<Provide a screenshot of the new coverage results by running the existing tool using all test modifications made by the group>

## Statement of individual contributions

<Write what each group member did>

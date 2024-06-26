import os

dir_path = os.path.dirname(os.path.realpath(__file__))

class CoverageTracker:
    def __init__(self):
       self.coverage = {}
    
    def clear_coverage(self):
        self.coverage = {}

    def add_coverage(self, function_name: str, branch_count: int):
        self.coverage[function_name] = {i: False for i in range(branch_count)}

    def mark_branch(self, function_name: str, branch_id: int):
        self.coverage[function_name][branch_id] = True
        self.save_coverage()

    def save_coverage(self, path: str = 'coverage.txt'):
        with open(os.path.join(dir_path, path), 'w') as f:
            for function_name, coverage in self.coverage.items():
                for id, covered in coverage.items():
                    f.write(f'{function_name} Branch {id}: {covered}\n')

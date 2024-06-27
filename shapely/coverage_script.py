branch_coverage = {
    "git_get_keywords_1": False,  # if branch for git_refnames
    "git_get_keywords_2": False,  # if branch for git_full
    "git_get_keywords_3": False,   # if branch for git_date
    "git_get_keywords_4": False,  # e if branch for mo in git_refnames
    "git_get_keywords_5": False,   # if branch for mo in git_full
    "git_get_keywords_6": False,   # if branch for mo in git_date
    "git_get_keywords_7": False,   # if branch for except
    "render_pep440_branch_1": False,  # if branch for closest-tag
    "render_pep440_branch_2": False,  # if branch for distance or dirty
    "render_pep440_branch_3": False,  # if branch for not master (inside closest-tag)
    "render_pep440_branch_4": False,  # if branch for dirty (inside closest-tag)
    "render_pep440_branch_5": False,  # else branch (exception #1)
    "render_pep440_branch_6": False,  # if branch for not master (inside exception #1)
    "render_pep440_branch_7": False   # if branch for dirty (inside exception #1)
    }

def save_coverage():
    with open("/tmp/test_coverage.txt", "w") as file:
        for branch, hit in branch_coverage.items():
            file.write(f"{branch}: {'True' if hit else 'False'}\n")

save_coverage()

render_git_describe_branches = [False] * 5
def save_git_render_branches(render_git_describe_branches):
    with open ("render_git_describe_coverage.txt", "w") as file:
        for i in range(len(render_git_describe_branches)):
            file.write(f"branch {i}: {render_git_describe_branches[i]}\n")

save_git_render_branches(render_git_describe_branches)

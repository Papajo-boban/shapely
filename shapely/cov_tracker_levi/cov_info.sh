#!/bin/bash

CURRENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
COV_FILE="$CURRENT_DIR"/coverage.txt 

declare -a funcs
declare -a branch_counts
declare -a covered_branches
declare -a ratios

while IFS= read -r line || [ -n "$line" ]; do
  func=$(echo "$line" | cut -d' ' -f1)
  covered=$(echo "$line" | cut -d' ' -f4)

  if echo "${funcs[@]}" | grep -q "$func"; then
    # get the index of the array element: https://superuser.com/questions/434507/how-to-find-the-index-of-a-word-in-a-string-in-bash/778840#778840
    index=$(echo ${funcs[@]/"$func"//} | cut -d/ -f1 | wc -w | tr -d ' ')
    branch_counts[$index]=$((${branch_counts[$index]} + 1))
    if [[ "$covered" == "True" ]]; then
      covered_branches[$index]=$((${covered_branches[$index]} + 1))
    fi
    ratios[$index]=$(echo "scale=2; ${covered_branches[$index]} / ${branch_counts[$index]}" | bc)
  else
    funcs+=("$func")
    branch_counts+=("1")
    if [[ "$covered" == "True" ]]; then
      covered_branches+=("1")
    else
      covered_branches+=("0")
    fi
    last_index=$((${#funcs[@]} - 1))
    ratios+=("$(echo "scale=2; ${covered_branches[$last_index]} / ${branch_counts[$last_index]}" | bc)")
  fi
done < "$COV_FILE"

printf "%-30s %-10s %-10s %-10s\n" "Function" "Branches" "Covered" "Ratio"
printf "%-30s %-10s %-10s %-10s\n" "--------" "--------" "-------" "-----"
for i in "${!funcs[@]}"; do
  printf "%-30s %-10s %-10s %-10s\n" "${funcs[$i]}" "${branch_counts[$i]}" "${covered_branches[$i]}" "${ratios[$i]}"
done

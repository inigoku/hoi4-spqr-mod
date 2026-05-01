#!/usr/bin/env bash
set -euo pipefail

MOD="/Users/inigobarrerabarcelo/Documents/Paradox Interactive/Hearts of Iron IV/mod/spqr"
HOI4="/Users/inigobarrerabarcelo/Library/Application Support/Steam/steamapps/common/Hearts of Iron IV"
KEEP_IDS=(2 16 41 47 103 106 115 157 162 184 186 339 458 510 552 553 849 907)

should_keep() {
  local target="$1"
  local keep
  for keep in "${KEEP_IDS[@]}"; do
    if [[ "$keep" == "$target" ]]; then
      return 0
    fi
  done
  return 1
}

for src in "$HOI4"/history/states/*.txt; do
  base=$(basename "$src")
  id=${base%%-*}

  if should_keep "$id"; then
    continue
  fi

  dest="$MOD/history/states/$base"

  awk '
    BEGIN {
      in_history = 0
      history_depth = 0
    }

    {
      line = $0

      if (!in_history) {
        if (line ~ /^[[:space:]]*impassable[[:space:]]*=/) {
          next
        }

        if (line ~ /^[[:space:]]*history[[:space:]]*=\{/ || line ~ /^[[:space:]]*history=\{/) {
          print ""
          print "        history = {"
          print "                owner = WLD"
          print "                controller = WLD"
          print "                add_core_of = WLD"
          print "        }"

          in_history = 1
          history_depth = gsub(/\{/, "{", line) - gsub(/\}/, "}", line)
          next
        }

        print line
        next
      }

      opens = gsub(/\{/, "{", line)
      closes = gsub(/\}/, "}", line)
      history_depth += opens - closes

      if (history_depth <= 0) {
        in_history = 0
      }
    }
  ' "$src" > "$dest"
done

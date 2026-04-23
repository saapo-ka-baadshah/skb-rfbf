#!/usr/bin/env bash

# Finds the repository root from a given directory. 
# 	Throws: RootMarkerNotFound error
find_project_root() {
  local marker=".git" # Change this to package.json, etc.
  local current_dir="$PWD"

  while [[ "$current_dir" != "/" ]]; do
    if [[ -e "$current_dir/$marker" ]]; then
      echo "$current_dir"
      return 0
    fi
    current_dir="$(dirname "$current_dir")"
  done

  echo "[ERR_RootMarkerNotFound] Root marker not found ($marker)" >&2
  return 1
}


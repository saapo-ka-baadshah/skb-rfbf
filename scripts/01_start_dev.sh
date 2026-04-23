#!/usr/bin/env bash

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &> /dev/null && pwd)

echo "SCRIPT_DIR: $SCRIPT_DIR"

source $SCRIPT_DIR/common.sh

# Also activate the development environment
REPO_ROOT=$(find_project_root)

source $REPO_ROOT/0_setup.sh

# Start the backend development server
BE_SRC=$REPO_ROOT/src
FE_SRC=$REPO_ROOT/front/app

(cd $BE_SRC && uvicorn app.main:app --reload) &
(cd $FE_SRC && npm run dev) &
wait $!

trap - SIGINT
echo "Stopping the development servers ..."
sleep 3
echo "Stopped!"

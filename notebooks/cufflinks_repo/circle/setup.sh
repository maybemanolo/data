#!/bin/bash

echo "running setup routine with python versions:"
for version in ${PLOTLY_PYTHON_VERSIONS[@]}; do
    echo "    ${version}"
done

PROGNAME=$(basename $0)
function error_exit
{
    echo -e "${PROGNAME}: ${1:-"Unknown Error"}\n" 1>&2
    exit 1
}

# PYENV shims need to be infront of the rest of the path to work!
echo "adding pyenv shims to the beginning of the path in this shell"
export PATH="/home/ubuntu/.pyenv/shims:$PATH"

# for each version we want, setup a functional virtual environment
for version in ${PLOTLY_PYTHON_VERSIONS[@]}; do
    echo Setting up Python ${version}

    # exporting this variable (in this scope) chooses the python version
    export PYENV_VERSION=${version}
    echo "Using pyenv version $(pyenv version)"

    # this was a major issue previously, sanity check that we're using the
    # version we *think* we're using (that pyenv is pointing to)
    echo "python -c 'import sys; print(sys.version)'"
    python -c 'import sys; print(sys.version)'

    # install core requirements all versions need
    pip install -r ${CORE_REQUIREMENTS_FILE} ||
        error_exit "${LINENO}: can't install core reqs for Python ${version}"

    # install some test tools
    pip install nose coverage ||
        error_exit "${LINENO}: can't install test tools for Python ${version}"

done

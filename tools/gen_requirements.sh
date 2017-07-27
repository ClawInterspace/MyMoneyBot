#!/usr/bin/env bash

dir=$( cd "$(dirname "${BASH_SOURCE}")" ; pwd -P )
parent_path=$(cd "$(dirname "${dir}")" ; pwd -P)
pip install pipreqs -q
pipreqs --force $parent_path --savepath $parent_path/requirements.txt
#!/bin/bash

set -x

time python sample.py multiprocessing "$@"
time python sample.py threading "$@"
time python sample.py gevent "$@"

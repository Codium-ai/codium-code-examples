#!/usr/bin/env bash
set -x

# --nobeep - by default, pytest-watch beeps whenever a test fails.
#   This is nice if you save files manually or only occasionaly, but if you're
#   saving on every keystrokes, then tests fail constantly whenever you're writing
#   code, and this becomes extremely annoying instead of beeing useful...
# -rP - display extra information on all non-passing tests. See:
#   https://docs.pytest.org/en/6.2.x/reference.html#command-line-flags
# pytest-watch - re-run tests on file changes
#   Needed pip installation of pytest-watch
# testmon - only run tests that can be impacted by the code that was changed.
#   (so you typically only run a small portion of the tests)
#   Needed pip installation of pytest-testmon
# ignore tmp_test_artifacts - we automatically write tests there, and if we don't 
#   ignore this directory, pytest-watch will think that something changed and it
#   will re-run the last test.
# -n 4 - running tests in parallel. Assumes we installed pytest-xdist.
# rm .testmondata - when we start watching, we delete the testmon cache,
#   meaning we'll run all the tests once. We want this because it means that to clear
#   the cache, all we need to do is stop the tests and re-run them, and this is more
#   common than the need to avoid running all the tests when restarting the watch.
rm .testmondata
pipenv run pytest-watch --nobeep --ignore tmp_test_artifacts -- --testmon -rp -n 4

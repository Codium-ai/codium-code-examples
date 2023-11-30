# Why another bank_account example?
This is a variation of the bank account, where it was divided to several files, so it won't be as easy to get
the context.
Specifically, it's for testing extend-suite, which currently doesn't know how to bring in context for things that the
CUT uses - so we need to add the context manually.

The functionality has also been greatly reduced, so we'll always get relevant tests.
Specifically - the premium account has 3 attributes - commision size, max deposit and max balance.
And the values of all these attributes are in the separate file - so no matter what, we'll always
have tests that check for them and have the wrong values if we don't manually add the context.

There's a top-level-functions test file and a class-test file, so we can test both.

# Workflow

The workflow of importing a new version is:

0. Sync the current port in git with ports tree
1. update Makefile's DISTVERSION to new version
2. check Telegram/ThirdParty and update Makefile
3. make makesum
4. create a new branch from last patched branch
   This needs to be done in all repos (tdesktop, libtgvoip, lib\_base, ...)
5. git fetch upstream && git pull upstream {new version tag}
   * For tdesktop: version tag is "vX.X.X".
   * For libtgvoip: version tag is usually "tdesktop". Make sure that tdesktop's
     last commit matches the commit referenced in ThirdParty.
7. resolve conflicts & git commit
6. Update libtgvoip's version in sync-patch.sh with upstream version.
8. git diff {new version tag}..HEAD > patch
9. remove old patches
10. make extract
11. apply patch
12. make makepatch
13. test & fix problems. repeat steps 8..12
14. remove unnecessary diff in patch with check-diff.py

Steps 8..12 are implemented in sync-patch.sh.

# Troubleshooting

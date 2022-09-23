# How to Create Projekts in this languages!

### This shows you how to make projects if you forget about it:

#### C++
- [cpp](c_cpp/)

#### C#
- [c#](csharp/)

#### Python
- [python](python/)

# Git Commands
```git
git init                                     # initialize new local repository
git clone <remote-location>                  # clone/copy remote repository
git config -l                                # list git config
git config [--global] user.name="<username>" # set <username>
git config [--global] user.email="<email"    # set <email>
git config [--global] core.editor="code"     # use vs-code as git editor
git checkout <branch-name>                   # switch to (local) <branch-name>
git checkout -b <branch-name>                # generate new local branch and
                                             # switch to it
git add <path>                               # stage <path>
git commit -m "<message>"                    # commit staged changes with
                                             # <message>
git push                                     # push current branch to remote
git push origin <branch-name>                # push current branch into remote
                                             # <branch-name>
git push --force                             # push current branch to remote and
                                             # override in case of conflicts
git push --force-with-lease                  # push current branch to remote and
                                             # override in case of conflicts, as
                                             # long as there are no new commits
                                             # on remote
git pull                                     # pulls current branch from remote
git pull origin <branch-name>                # pull remote <branch-name> into
                                             # current branch
git merge <branch-name>                      # merege <branch-name> into current
                                             # branch
git rebase <branch-name/commit-hash>         # rebase onto
                                             # <branch-name/commit-hash>
git rebase -i <beanch-name/commit-hash>      # interactive rebase onto
                                             # <branch-name/commit-hash>
```

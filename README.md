# BoardgamersNetwork
Repository for the project of "Design of WWW Services" course
Testing some new things


Some git commands:

1. Get new updates (pull)
    [ git fetch ]                                   -> to update changes in every branches & get new branches
    [ git checkout <branch-name> ]                  -> switch to new branch
    [ git pull origin <branch-name> ]               -> get the new code from online repository

2. Push updates to server:
    [ git status ]                                  -> check what have been done
        #if you delete files
            [ git add --all . ]                     -> add all the new modified file to the "stage", including removed files
        #if not
            [ git add . ]                           -> add all the new modified file to the "stage"
    [ git commit -m "Your message" ]                -> commit the changes to local repository
    [ git push origin master ]                      -> push the new code to online repository

    #if you want to reset the change in a specific file
        [ git reset HEAD <file-path> ]

3. Other command
    [ git checkout <branch-name> ]                  -> switch into another branch
    [ git checkout -b <branch-name> ]               -> create new branch
    [ git merge <branch-name> ]                     -> merge current branch with the code from other branch


(NOTES: Pulling code before modifying files & pushing to avoid error)
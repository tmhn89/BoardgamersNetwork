# BoardgamersNetwork
Repository for the project of "Design of WWW Services" course

### Changelogs

##### 10/11/2015
- Merge fea_map_makers into dev
- Merge fea_games into dev. install the following:
    - pip install requests
    - pip install xmltodict

##### 3/11/2015

- Update model as discussed on Nov 2nd
    - remove friendship
    - add guild
    - change location stored from string to lat & long

##### 8/10/2015

- Add all users view. Accessible from `http://localhost:8000/users` (if you use port 8000 for server)
- Fix project structure for static files (including css, js, images)
    - now they will be stored in `bgn/static-assets`
    - calling them from templates: 
        - `{% load staticfiles %}` from the beginning of the file
        - link to file using `{% static 'file-name' %}` e.g `{% static 'profile_pic.png' %}`
    - the folder `bgn_app/templates` now store html files only

### Some git commands:

1. Get new updates (pull)

    `git fetch` -> to update changes in every branches & get new branches
    
    `git checkout branch-name` -> switch to new branch
    
    `git pull origin branch-name` -> get the new code from online repository

2. Push updates to server (NOTES: Pulling code before modifying files & pushing to avoid error)

    `git status` -> check what have been done
        
    - if you delete files: `git add --all .` -> add all the new modified file to the "stage", including removed files
    - if not: `git add .`  -> add all the new modified file to the "stage"
            
    `git commit -m "Your message"` -> commit the changes to local repository
    
    `git push origin master` -> push the new code to online repository

3. Other command

    `git checkout branch-name` -> switch into another branch
    
    `git checkout -b branch-name` -> create new branch
    
    `git merge branch-name` -> merge current branch with the code from other branch
    
    `git reset HEAD file-path` -> discard changes in a specific file

4. Move the modified files to another branches

    `git stash` -> take the modified files to a "temporary storage"
    
    `git checkout branch-name` -> swtich into another branch
    
    `git stash pop` -> put the modified from stash to the current branch

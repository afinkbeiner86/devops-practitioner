# Module 2 - Version Control with Git

<details>
<summary>Exercise 1: Clone and create new repository </summary>
 <br />

**steps:**
```sh

# clone repository & change into project dir
git clone git@gitlab.com:twn-deveops-bootcamp/exercises/git-project.git
cd git-project

# remove remote repo reference and create your own local repository
rm -rf .git
git init
git add .
git commit -m "Initial commit"

# create git repository on Gitlab and push your newly created local repository to it
git remote add origin git@gitlab.com:{gitlab-user}/{gitlab-repo}.git
git push -u origin master

```

</details>

******

<details>
<summary>Exercise 2: .gitignore </summary>
 <br />

**create .gitignore file with following entries**
```sh
.idea 
.DS_Store
out 
build
```

**remove cached commited files and commit .gitignore file**
```sh
git rm --cached .DS_Store

# -r for directories
git rm -r --cached .idea
git rm -r --cached out
git rm -r --cached build

# commit & push the changes
git add .
git commit -m "remove ignored files"
git push
```

</details>

******

<details>
<summary>Exercise 3: Feature branch </summary>
 <br />

**steps**
```sh
# create feature branch
git checkout -b feature/changes

# in build.gradle file, line 18, locate the "logstash-logback-encoder" library 
# change version from '5.2' to '7.3'
compile group: 'net.logstash.logback', name: 'logstash-logback-encoder', version: '7.3'

# locate index.html file in src/main/webapp folder
# on line 9, add the image url with 
<img src="https://www.careeraddict.com/uploads/article/58721/illustration-group-people-team-meeting.jpg" width="" />

# check and commit  changes
git diff
git add .
git commit -m "Upgrade logback library and add image url"

# push your changes to remote
git push
```

</details>

******

<details>
<summary>Exercise 4: Bugfix branch </summary>
 <br />

**steps**
```sh
# create bugfix branch
git checkout -b bugfix/changes

# in Application.java file in src/main/java/com, line 22, fix the spelling error
log.info("Java app started");

# check and commit  changes
git diff
git add .
git commit -m "Fix spelling error"

# push your changes to remote
git push
```

</details>

******

<details>
<summary>Exercise 5: Merge request </summary>
 <br />

**steps**
```sh
# merge feature branch into master. Alternatively do the merge from Gitlab UI
git checkout master
git merge feature/changes 

# push the merge to remote master
git push
```

</details>

******

<details>
<summary>Exercise 6: Fix Merge conflict </summary>
 <br />

**steps**
```sh
# switch to bugfix branch
git checkout bugfix/changes

# in build.gradle file, line 18, locate the "logstash-logback-encoder" library 
# change version from '5.2' to '7.2'
compile group: 'net.logstash.logback', name: 'logstash-logback-encoder', version: '7.2'

# commit change locally
git add .
git commit -m "upgrade logger library version"

# bring bugfix branch uptodate with master branch. Alternatively do the merge from Gitlab UI
git merge master

# you will get a merge conflict here for build.gradle file, like 18, logback library version 

# fix merge conflict and when done check the state
git status

# if all fixed, you can commit and push the merge into your bugfix branch
git push

```

</details>

******

<details>
<summary>Exercise 7: Revert commit </summary>
 <br />

**steps**
```sh
# on bugfix branch

# locate index.html in src/main/webapp, line 11 & fix spelling error
<li>Sarah - Full stack devloper</li>

# commit change locally
git add .
git commit -m "Fix spelling error"

# locate index.html in src/main/webapp, line 9 & set image url
<img src="https://www.tameday.com/wp-content/uploads/2018/10/effective-meetings.jpg" width="" />

# commit change locally
git add .
git commit -m "Set image url"

# push both commits to remote
git push

# revert last commit and push the revertion into remote repo
git revert HEAD
git push

```

</details>

******

<details>
<summary>Exercise 8: Reset commit </summary>
 <br />

**steps**
```sh
# on bugfix branch

# locate index.html in src/main/webapp, line 15 & make change
<li>Bruno - DevOps engineer</li>

# commit change locally
git add .
git commit -m "Adjust employee role description"

# reset the last local commit, meaning move to the previous commit
git reset --hard HEAD~

```

</details>

******

<details>
<summary>Exercise 9: Merge </summary>
 <br />

**steps**
```sh
# merge bugfix branch into master
git checkout master
git merge bugfix/changes

```

</details>

******

<details>
<summary>Exercise 10: Delete Branches </summary>
 <br />

**steps**
```sh
# delete branches remotely via Gitlab UI

# delete branches locally with CLI
git branch -D bugfix/changes
git branch -D feature/changes

```

</details>

******

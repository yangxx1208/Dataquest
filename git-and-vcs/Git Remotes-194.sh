## 1. Introduction to Remote Repositories ##

/home/dq$ git clone /dataquest/user/git/chatbot

## 2. Making Changes to Cloned Repositories ##

/home/dq/chatbot$ git commit -m "Updated README.md"

## 3. Overview of the Master Branch ##

/home/dq/chatbot$ git branch

## 4. Pushing Changes to the Remote ##

/home/dq/chatbot$ git push origin master

## 5. Viewing Individual Commits ##

/home/dq/chatbot$ git show 5ee0c94fea6e4f5a27ecf5941eef7960fc78c129

## 6. Commits and the Working Directory ##

/home/dq/chatbot$ git diff

## 7. Switching to a Specific Commit ##

/home/dq/chatbot$ git reset 97ff7caafd86e308ed69b8613b59984d681f7d1e

## 8. Pulling From a Remote Repo ##

/home/dq/chatbot$ git pull

## 9. Referring to the Most Recent Commit ##

/home/dq/chatbot$ git reset --hard HEAD~1
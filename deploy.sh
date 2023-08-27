#!/bin/bash
git config --global user.email "pro.belhkoumali.mounaim@gmail.com"
git config --global user.name "Mounaim"

git remote add origin https://github.com/belkhoumali-Ahmed-Abdelmounaim/Data_Sage.git   # if origin already exists, skip this line


git add .

git commit -m "Updates"

git push -u origin main 

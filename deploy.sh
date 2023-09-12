#!/bin/bash
git config --global user.email "ahmed_abd_el_mounaim.belkhoumali@g.enp.edu.dz"
git config --global user.name "belkhoumali-Ahmed-Abdelmounaim"

git remote add origin https://github.com/belkhoumali-Ahmed-Abdelmounaim/Data_Sage.git   # if origin already exists, skip this line


git add .

git commit -m "Updates"

git push -u origin main 

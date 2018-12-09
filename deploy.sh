#!/bin/bash
curTime="`date +%Y-%m-%d,%H:%m:%s`"
git add .
git commit -m "$curTime"
proxychains4 git push origin hexo
hexo g -d


#!/bin/bash

REPO_URL="http://139.59.141.95:8081/service/rest/v1/components?repository={my-npm}&sort=version"
USERNAME=
PASSWORD=

curl -u $USERNAME:$PASSWORD -X GET $REPO_URL | jq "." > artifact.json

artifactDownloadUrl=$(jq '.items[].assets[].downloadUrl' artifact.json --raw-output)
artifactFileName=$(jq '.items[].assets[].path' artifact.json --raw-output | awk -F/ '{print $NF}')

curl -u $USERNAME:$PASSWORD "$artifactDownloadUrl" -O

tar xzfv $artifactFileName

npm --prefix ./package install ./package
node ./package/server.js &

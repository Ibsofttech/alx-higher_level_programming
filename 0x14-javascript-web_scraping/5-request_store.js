#!/usr/bin/node
const fs = require('fs');
const rqst = require('request');
rqst(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));

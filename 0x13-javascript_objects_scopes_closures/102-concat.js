#!/usr/bin/node

const fs = require('fs');

function concatFiles (file1, file2, dest) {
  const data1 = fs.readFileSync(file1);
  const data2 = fs.readFileSync(file2);
  const data = Buffer.concat([data1, data2]);
  fs.writeFileSync(dest, data);
}

concatFiles('file1.txt', 'file2.txt', 'dest.txt');

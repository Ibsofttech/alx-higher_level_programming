#!/usr/bin/node

exports.esrever = function (list) {
  const myList = [];
  let len = list.length;
  while (len > 0) {
    myList.push(list[len - 1]);
    len--;
  }
  return myList;
};

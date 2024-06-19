#!/usr/bin/node

exports.esrever = function (list) {
  const revsVersion = [];
  for (let i = list.length - 1; i >= 0; i--) {
    revsVersion.push(list[i]);
  }
  return revsVersion;
};

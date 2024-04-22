#!/usr/bin/node
exports.callmemody = function (x, callback) {
  for (let i = 0; i < x; i++);
  callback();
};

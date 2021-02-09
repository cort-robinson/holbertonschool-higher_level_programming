#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let nb = 0;
  for (const item of list) {
    if (item === searchElement) {
      nb++;
    }
  }
  return (nb);
};

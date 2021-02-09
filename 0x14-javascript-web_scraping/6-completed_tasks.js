#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, res, body) => {
  tasks = JSON.parse(body).filter(task => task.completed === true);
  console.log(tasks);
  let dict = {};
  for (const task of tasks) {
    if (dict[task.userId] === undefined) {
      dict[task.userId] = 1;
    } else {
      dict[task.userId] += 1;
    }
  }
  console.log(dict);
});

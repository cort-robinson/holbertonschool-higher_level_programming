#!/usr/bin/node

const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], (error, response, body) => {
  if (error) console.log(error);

  const parsedBody = JSON.parse(body);
  console.log(parsedBody.title);
});

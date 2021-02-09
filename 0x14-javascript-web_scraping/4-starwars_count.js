#!/usr/bin/node

const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (error) console.log(error);

  const data = JSON.parse(body).results;
  const films = data.filter(film => film.characters.includes(
    'https://swapi-api.hbtn.io/api/people/18/'));
  console.log(films.length);
});

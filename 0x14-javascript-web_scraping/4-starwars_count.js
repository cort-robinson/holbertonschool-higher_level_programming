#!/usr/bin/node

const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (error) console.log(error);

  const data = JSON.parse(body).results;
  const films = data.filter(film => {
    for (character of film.characters) {
      if (character.includes('18')) return (true);
    }
  })
  console.log(films.length);
});

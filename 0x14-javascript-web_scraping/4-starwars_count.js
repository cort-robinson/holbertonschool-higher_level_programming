#!/usr/bin/node

const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (error) console.log(error);

  const data = JSON.parse(body).results;
  const films = data.filter(film => {
    for (const character of film.characters) {
      if (character.includes('18')) return (true);
    }
    return (false);
  });
  console.log(films.length);
});

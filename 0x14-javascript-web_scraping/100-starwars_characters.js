#!/usr/bin/node

const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], (error, response, body) => {
  if (error) console.log(error);

  const characterIds = JSON.parse(body).characters;
  for (const characterId of characterIds) {
    request(characterId, (error, response, body) => {
      if (error) console.log(error);

      const character = JSON.parse(body);
      console.log(character.name);
    });
  }
});

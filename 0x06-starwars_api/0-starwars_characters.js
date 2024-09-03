#!/usr/bin/node
// Parsingc command line arguments
// Request module though it's depracated
// url = https://swapi-api.alx-tools.com/api/films/{process.argv[1]}/
// response = ["url1", "url2", ...]
// url1 = https://swapi-api.alx-tools.com/api/people/1/
// response =  {"name": "<name>"}
const request = require('../../../../../../usr/local/lib/node_modules/request');
const process = require('process');

if (process.argv.length !== 3) {
  console.error('Usage 0-starwars_characters <id>');
} else {
  const id = process.argv[2];
  const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;

  request(url, function (error, response, body) {
    if (!error && response.statusCode === 200) {
      try {
        const data = JSON.parse(body);
        data.characters.forEach((url) => {
          getCharacterName(url);
        });
      } catch (e) {
        console.error('Error parsing JSON:', e);
      }
    } else {
      console.error('Request failed:', error);
    }
  });
}

function getCharacterName (url) {
  request(url, function (error, response, body) {
    if (!error && response.statusCode === 200) {
      try {
        const data = JSON.parse(body);
        console.log(data.name);
      } catch (e) {
        console.log(e);
      }
    } else {
      console.log(response.statusCode);
    }
  });
}

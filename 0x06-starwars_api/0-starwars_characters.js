#!/usr/bin/node
// Parsing command line arguments
// Request module though it's depracated
// url = https://swapi-api.alx-tools.com/api/films/{process.argv[1]}/
// response = ["url1", "url2", ...]
// url1 = https://swapi-api.alx-tools.com/api/people/1/
// response =  {"name": "<name>"}

const request = require('request');
const process = require('process');

async function getCharacterUrls (url) {
  const promise = new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode === 200 && !error) {
        try {
          const data = JSON.parse(body);
          resolve(data.characters);
        } catch (e) {
          reject(e);
        }
      } else {
        reject(error);
      }
    });
  });

  try {
    const characters = await promise;
    return characters;
  } catch (e) {
    console.error(new Error('Error fetching URLS'));
  }
}

async function getCharacters () {
  // call a function to get the character urls
  // create promises for each member of the list
  // after all promises resolve, print the return value.
  if (process.argv.length !== 3) {
    console.error('Usage: 0-starwars_characters <filmid>');
    return;
  }

  const filmId = process.argv[2];
  const url = `https://swapi-api.alx-tools.com/api/films/${filmId}/`;
  const urls = await getCharacterUrls(url);
  const promises = urls.map((url) => {
    return new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (!error && response.statusCode === 200) {
          try {
            const characterData = JSON.parse(body);
            resolve(characterData.name);
          } catch (e) {
            reject(e);
          }
        } else {
          reject(error);
        }
      });
    });
  });

  const charNames = await Promise.all(promises);
  charNames.forEach((element) => {
    console.log(element);
  });
}

getCharacters();

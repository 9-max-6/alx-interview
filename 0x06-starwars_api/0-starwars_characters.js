#!/usr/bin/node
// Parsingc command line arguments
// Request module though it's depracated
// url = https://swapi-api.alx-tools.com/api/films/{process.argv[1]}/
// response = ["url1", "url2", ...]
// url1 = https://swapi-api.alx-tools.com/api/people/1/
// response =  {"name": "<name>"}

const process = require("process");

if (process.argv.length !== 3) {
  console.error("Usage 0-starwars_characters <id>");
} else {
  id = process.argv[2];
  url = `https://swapi-api.alx-tools.com/api/${id}/`;
  console.log(url);
}

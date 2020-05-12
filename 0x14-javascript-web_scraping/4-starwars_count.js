#!/usr/bin/node

const request = require('request');

request(`${process.argv[2]}`, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    let info = JSON.parse(body).results;
    let count = 0; info.forEach(function (element) {
      element.characters.forEach(function (character) {
        if (character.includes('18')) { count++; }
      });
    });
    console.log(count);
  }
});

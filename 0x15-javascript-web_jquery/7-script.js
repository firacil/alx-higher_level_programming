/* global $ */
$(document).ready(function () {
  // by using get method we will fetch data in the provided url
  // then display in our page
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
    const characterName = data.name;
    $('#character').text(characterName);
  });
});

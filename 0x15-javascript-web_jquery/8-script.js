// fetching all titles of the movie from url by using get method
$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    data.results.forEach(function (d) {
      $('#list_movies').append('<li>' + d.title + '</li>');
    });
  });
});

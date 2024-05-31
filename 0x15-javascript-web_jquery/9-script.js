// retrieving data from the url using get method
/* global $ */
$(document).ready(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    $('#hello').text(data.hello);
  });
});

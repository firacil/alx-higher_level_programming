// script to add class red to header
/* global $ */
$(document).ready(function () {
  // select the elements and adding click event
  $('#red_header').click(function () {
    // add class red to header
    $('header').addClass('red');
  });
});

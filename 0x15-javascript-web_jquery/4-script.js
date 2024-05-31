// script that update class of the header
/* global $ */
$(document).ready(function () {
  // select elements using jquery and set click event
  $('#toggle_header').click(function () {
    // check if class is red or green
    if ($('header').hasClass('green')) { $('header').removeClass('green').addClass('red'); } else { $('header').removeClass('red').addClass('green'); }
  });
});

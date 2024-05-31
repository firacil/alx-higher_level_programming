// script to update text in header on click of element of id 'update_header'
$(document).ready(function () {
  // select element and add click event using jquery
  $('#update_header').click(function () {
    // update text in header
    $('header').text('New Header!!!');
  });
});

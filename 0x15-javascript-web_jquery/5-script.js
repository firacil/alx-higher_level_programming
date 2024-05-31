// adding new item using jquery
/* global $ */
$(document).ready(function () {
  // select element and add click event
  $('#add_item').click(function () {
    // create variable to hold element
    const newItem = $('<li>Item</li>');

    // add new item to ul
    $('ul.my_list').append(newItem);
  });
});

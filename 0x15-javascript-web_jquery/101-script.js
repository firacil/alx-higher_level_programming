// script to add, remove and clear list
$(document).ready(function () {
  // add item to list
  $('#add_item').click(function () {
    const newItem = $('<li>Item</li>');
    $('ul.my_list').append(newItem);
  });

  // remove single list from the last
  $('#remove_item').click(function () {
    $('ul.my_list li:last-child').remove();
  });

  // clear all item from the list
  $('#clear_list').click(function () {
    $('ul.my_list').empty();
  });
});

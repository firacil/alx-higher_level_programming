$(document).ready(function () {
  // Select the elements using doc.query
  // Add a click event listner using jquery
  const redHeader = document.querySelector('#red_header');
  const head = document.querySelector('header');
  $(redHeader).click(function () {
    // change color on click of what is in  redHeader
    $(head).css('color', '#FF0000');
  });
});

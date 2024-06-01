$(document).ready(function () {
  $('#btn_translate').click(fetchTranslation);
  $('#language_code').keyup(function (event) {
    if (event.keyCode === 13) {
      fetchTranslation();
    }
  });

  function fetchTranslation () {
    const langCode = $('#language_code').val();
    $.getJSON(`https://www.fourtonfish.com/hellosalut/hello/?lang=${langCode}`, function (data) {
      $('#hello').text(data.hello);
    });
  }
});

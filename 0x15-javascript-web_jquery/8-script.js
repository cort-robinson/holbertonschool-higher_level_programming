$(document).ready(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', data => {
    $.each(data.results, (index, film) => $('UL#list_movies').append('<li>' + film.title + '</li>'));
  });
});

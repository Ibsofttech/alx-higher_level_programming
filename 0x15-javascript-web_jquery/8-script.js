$.get("https://swapi-api.alx-tools.com/api/films/?format=json", function(data) {
	// Loop through the results and display the data
	$(data.results).each(function() {
	  $("UL#list_movies").append("<li>" + this.title + "</li>");
	});
  });
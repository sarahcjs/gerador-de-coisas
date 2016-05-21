$("#botao").click(function() {

  $.getJSON("/coisa", function(data) {
    $("#porta-coisas").text(data['coisa']);
  });
});
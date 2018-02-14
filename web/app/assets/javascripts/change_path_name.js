$(document).ready(function(){
  $(document).on('click', '.cartouche', function(e) {
    number = $(this).data('mydata');
    element = document.getElementById("inp-" + number);
    $(element).show();
  });

  $(document).on('click', '.button2', function(e) {
    number = $(this).data('mydata');
    id = $(this).data('track');
    $.post("/api/tracker/" + id + "/change_group",
    {
        group_name: document.getElementById("input_name" + number).value
    });
  }, null, 'js');
});

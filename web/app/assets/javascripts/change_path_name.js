$(document).ready(function(){

  var tracker_id;
  var name;

  $(document).on('click', '.button2', function(e) {
    $.post("/api/tracker/" + tracker_id + "/change_group",
    {
        group_name: document.getElementById("input_name").value
    });
  }, null, 'js');

  $('#myModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget);
    tracker_id = button.data('tracker');
    name = button.data('name');
    var modal = $(this);
    modal.find('.modal-body input').val(name);
  })
});

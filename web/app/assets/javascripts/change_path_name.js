$(document).ready(function(){

  $(document).on('click', '.button2', function(e) {
    number = $(this).data('mydata');
    id = $(this).data('track');
    $.post("/api/tracker/" + id + "/change_group",
    {
        group_name: document.getElementById("input_name" + number).value
    });
  }, null, 'js');

  $('#myModal').on('show.bs.modal', function (event) {
    alert(1);
    var button = $(event.relatedTarget)
    var info = button.data('iter')
    alert(info);
    var modal = $(this);
    modal.find('.modal-body input').val(info);
  })
});

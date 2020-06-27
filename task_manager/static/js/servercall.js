$(document).ready(function(){
    console.log("11111111111")
    $("#id_assign_to").click(function () {
          console.log("2222222222222ppppp")
          var form = $(this).closest("form");
          console.log("2222222222222",form)
          $.ajax({
            url: form.attr("validate_workers_selection-url"),
            data: form.serialize(),
            dataType: 'json',
            success: function (data) {
              if (data.user_warn) {
                alert(data.user_warn);
              }
            }
          });

        });
});
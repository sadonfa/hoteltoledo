// $( function() {
//     $( "#datepicker" ).datepicker();
//   } );
$(function () {
    $.datepicker.setDefaults($.datepicker.regional["es"]);
    $(".datepicker").datepicker({
        minDate: "08/04/2023",
        maxDate: "12/07/2023"
    });
});



$(function () {
    $.datepicker.setDefaults($.datepicker.regional["es"]);
    $("#datepicker").datepicker({
        minDate: "15/04/2013",
        maxDate: "15/05/2013"
    });
});
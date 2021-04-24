$( document ).ready(function() {
    var select = $("#type_vehicle" ).val()
    EnableInputs(select)
});

// se usa jquery para bloquear algunos campos dependiendo el tipo de vehiculo
function EnableInputs(select){
    if ( select == 1){
        // si es automovil
        $("#cylinder_capacity").attr('disabled','disabled');
        $("#gears").attr('disabled','disabled');

        $("#doors_number").removeAttr('disabled');
        $("#vehicle_model").removeAttr('disabled');

    }else if(select == 2){
        // si es moto
        $("#cylinder_capacity").removeAttr('disabled');
        $("#gears").removeAttr('disabled');

        $("#doors_number").attr('disabled','disabled');
        $("#vehicle_model").attr('disabled','disabled');

    }else{
        // si es bicicleta
        $("#cylinder_capacity").attr('disabled','disabled');
        $("#gears").attr('disabled','disabled');

        $("#doors_number").attr('disabled','disabled');
        $("#vehicle_model").attr('disabled','disabled');
    }
}

$("#type_vehicle" ).change(function() {
    var select = $("#type_vehicle" ).val()
    EnableInputs(select)
});
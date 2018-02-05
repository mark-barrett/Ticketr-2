/**
 * Created by markbarrett on 05/02/2018.
 */

// For the resell options on the create event page
$(document).ready(function() {

    allow_resell = $('select[name=allow_resell]').val();

    if(allow_resell == 'Y') {
        $('#div_id_when_resell').show();
    } else {
        $('#div_id_when_resell').hide();
    }
});

// Update when resell according to the allow resell
$('select[name=allow_resell]').change(function() {
    allow_resell = $(this).val();

    if(allow_resell == 'Y') {
        $('#div_id_when_resell').show();
    } else {
        $('#div_id_when_resell').hide();
    }
});

// This will hide the amount of tickets needed to resell at the start if not chosen
$(document).ready(function() {

    when_resell = $('select[name=when_resell]').val();

    if(when_resell == 'A') {
        $('#div_id_amount_resell').show();
    } else {
        $('#div_id_amount_resell').hide();
    }
});

// This will update the amount of tickets needed to resell if the when resell is changed
$('select[name=when_resell]').change(function() {
    when_resell = $(this).val();

    if(when_resell == 'A') {
        $('#div_id_amount_resell').show();
    } else {
        $('#div_id_amount_resell').hide();
    }
});
/**
 * Created by markbarrett on 31/01/2018.
 */
/* Code for dynamic form fields */
var counter = 1;
var limit = 10;
function addInput(divName){
    if (counter == limit)  {
        alert("You have reached the limit of adding " + counter + " options.");
    }
    else {
        var newdiv = document.createElement('div');

        if(counter > 1) {
            newdiv.innerHTML = "<br/><div class='row'>" +
                "<div class='col-md-6'><input type='text' name='name' class='form-control'></div>" +
                "<div class='col-md-3'><input type='text' name='quantity' class='form-control'></div>" +
                "<div class='col-md-3'><div class='input-group mb-2'><div class='input-group-prepend'><div class='input-group-text'><i class='fa fa-eur' aria-hidden='true'></i></div></div><input type='number' step='any' name='price' class='form-control'></div>" +
                "</div>";
        } else {
            newdiv.innerHTML = "<div class='row'>" +
                "<div class='col-md-6'>Name<input type='text' name='name' class='form-control'></div>" +
                "<div class='col-md-3'>Quantity<input type='text' name='quantity' class='form-control'></div>" +
                "<div class='col-md-3'>Price<div class='input-group mb-2'><div class='input-group-prepend'><div class='input-group-text'><i class='fa fa-eur' aria-hidden='true'></i></div></div><input type='number' step='any' name='price' class='form-control'></div>" +
                "</div>";
        }
        document.getElementById(divName).appendChild(newdiv);
        counter++;
    }
}
"use strict";

function _typeof(obj) { if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }; } return _typeof(obj); }

/*! jQuery Validation Plugin - v1.19.1 - 6/15/2019
 * https://jqueryvalidation.org/
 * Copyright (c) 2019 Jörn Zaefferer; Licensed MIT */
!function (a) {
  "function" == typeof define && define.amd ? define(["jquery", "../jquery.validate.min"], a) : "object" == (typeof module === "undefined" ? "undefined" : _typeof(module)) && module.exports ? module.exports = a(require("jquery")) : a(jQuery);
}(function (a) {
  return a.extend(a.validator.messages, {
    required: "Šis lauks ir obligāts.",
    remote: "Lūdzu, pārbaudiet šo lauku.",
    email: "Lūdzu, ievadiet derīgu e-pasta adresi.",
    url: "Lūdzu, ievadiet derīgu URL adresi.",
    date: "Lūdzu, ievadiet derīgu datumu.",
    dateISO: "Lūdzu, ievadiet derīgu datumu (ISO).",
    number: "Lūdzu, ievadiet derīgu numuru.",
    digits: "Lūdzu, ievadiet tikai ciparus.",
    creditcard: "Lūdzu, ievadiet derīgu kredītkartes numuru.",
    equalTo: "Lūdzu, ievadiet to pašu vēlreiz.",
    extension: "Lūdzu, ievadiet vērtību ar derīgu paplašinājumu.",
    maxlength: a.validator.format("Lūdzu, ievadiet ne vairāk kā {0} rakstzīmes."),
    minlength: a.validator.format("Lūdzu, ievadiet vismaz {0} rakstzīmes."),
    rangelength: a.validator.format("Lūdzu ievadiet {0} līdz {1} rakstzīmes."),
    range: a.validator.format("Lūdzu, ievadiet skaitli no {0} līdz {1}."),
    max: a.validator.format("Lūdzu, ievadiet skaitli, kurš ir mazāks vai vienāds ar {0}."),
    min: a.validator.format("Lūdzu, ievadiet skaitli, kurš ir lielāks vai vienāds ar {0}.")
  }), a;
});
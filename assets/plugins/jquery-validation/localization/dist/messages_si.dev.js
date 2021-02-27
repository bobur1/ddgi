"use strict";

function _typeof(obj) { if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }; } return _typeof(obj); }

(function (factory) {
  if (typeof define === "function" && define.amd) {
    define(["jquery", "../jquery.validate"], factory);
  } else if ((typeof module === "undefined" ? "undefined" : _typeof(module)) === "object" && module.exports) {
    module.exports = factory(require("jquery"));
  } else {
    factory(jQuery);
  }
})(function ($) {
  /*
   * Translated default messages for the jQuery validation plugin.
   * Locale: SI (Slovenian)
   */
  $.extend($.validator.messages, {
    required: "To polje je obvezno.",
    remote: "Vpis v tem polju ni v pravi obliki.",
    email: "Prosimo, vnesite pravi email naslov.",
    url: "Prosimo, vnesite pravi URL.",
    date: "Prosimo, vnesite pravi datum.",
    dateISO: "Prosimo, vnesite pravi datum (ISO).",
    number: "Prosimo, vnesite pravo številko.",
    digits: "Prosimo, vnesite samo številke.",
    creditcard: "Prosimo, vnesite pravo številko kreditne kartice.",
    equalTo: "Prosimo, ponovno vnesite enako vsebino.",
    extension: "Prosimo, vnesite vsebino z pravo končnico.",
    maxlength: $.validator.format("Prosimo, da ne vnašate več kot {0} znakov."),
    minlength: $.validator.format("Prosimo, vnesite vsaj {0} znakov."),
    rangelength: $.validator.format("Prosimo, vnesite od {0} do {1} znakov."),
    range: $.validator.format("Prosimo, vnesite vrednost med {0} in {1}."),
    max: $.validator.format("Prosimo, vnesite vrednost manjšo ali enako {0}."),
    min: $.validator.format("Prosimo, vnesite vrednost večjo ali enako {0}.")
  });
  return $;
});
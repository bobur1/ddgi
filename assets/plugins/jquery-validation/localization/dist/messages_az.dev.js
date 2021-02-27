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
   * Locale: Az (Azeri; azərbaycan dili)
   */
  $.extend($.validator.messages, {
    required: "Bu xana mütləq doldurulmalıdır.",
    remote: "Zəhmət olmasa, düzgün məna daxil edin.",
    email: "Zəhmət olmasa, düzgün elektron poçt daxil edin.",
    url: "Zəhmət olmasa, düzgün URL daxil edin.",
    date: "Zəhmət olmasa, düzgün tarix daxil edin.",
    dateISO: "Zəhmət olmasa, düzgün ISO formatlı tarix daxil edin.",
    number: "Zəhmət olmasa, düzgün rəqəm daxil edin.",
    digits: "Zəhmət olmasa, yalnız rəqəm daxil edin.",
    creditcard: "Zəhmət olmasa, düzgün kredit kart nömrəsini daxil edin.",
    equalTo: "Zəhmət olmasa, eyni mənanı bir daha daxil edin.",
    extension: "Zəhmət olmasa, düzgün genişlənməyə malik faylı seçin.",
    maxlength: $.validator.format("Zəhmət olmasa, {0} simvoldan çox olmayaraq daxil edin."),
    minlength: $.validator.format("Zəhmət olmasa, {0} simvoldan az olmayaraq daxil edin."),
    rangelength: $.validator.format("Zəhmət olmasa, {0} - {1} aralığında uzunluğa malik simvol daxil edin."),
    range: $.validator.format("Zəhmət olmasa, {0} - {1} aralığında rəqəm daxil edin."),
    max: $.validator.format("Zəhmət olmasa, {0} və ondan kiçik rəqəm daxil edin."),
    min: $.validator.format("Zəhmət olmasa, {0} və ondan böyük rəqəm daxil edin")
  });
  return $;
});
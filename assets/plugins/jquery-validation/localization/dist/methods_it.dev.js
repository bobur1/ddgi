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
   * Localized default methods for the jQuery validation plugin.
   * Locale: IT
   */
  $.extend($.validator.methods, {
    date: function date(value, element) {
      return this.optional(element) || /^\d\d?\-\d\d?\-\d\d\d?\d?$/.test(value);
    },
    number: function number(value, element) {
      return this.optional(element) || /^-?(?:\d+|\d{1,3}(?:\.\d{3})+)(?:,\d+)?$/.test(value);
    }
  });
  return $;
});
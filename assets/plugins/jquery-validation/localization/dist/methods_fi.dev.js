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
   * Locale: FI
   */
  $.extend($.validator.methods, {
    date: function date(value, element) {
      return this.optional(element) || /^\d{1,2}\.\d{1,2}\.\d{4}$/.test(value);
    },
    number: function number(value, element) {
      return this.optional(element) || /^-?(?:\d+)(?:,\d+)?$/.test(value);
    }
  });
  return $;
});
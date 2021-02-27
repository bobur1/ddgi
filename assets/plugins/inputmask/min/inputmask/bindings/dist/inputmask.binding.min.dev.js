"use strict";

function _typeof(obj) { if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }; } return _typeof(obj); }

/*!
* bindings/inputmask.binding.min.js
* https://github.com/RobinHerbots/Inputmask
* Copyright (c) 2010 - 2019 Robin Herbots
* Licensed under the MIT license (http://www.opensource.org/licenses/mit-license.php)
* Version: 4.0.9
*/
(function (factory) {
  if (typeof define === "function" && define.amd) {
    define(["jquery", "../inputmask", "../global/window"], factory);
  } else if ((typeof exports === "undefined" ? "undefined" : _typeof(exports)) === "object") {
    module.exports = factory(require("jquery"), require("../inputmask"), require("../global/window"));
  } else {
    factory(jQuery, window.Inputmask, window);
  }
})(function ($, Inputmask, window) {
  $(window.document).ajaxComplete(function (event, xmlHttpRequest, ajaxOptions) {
    if ($.inArray("html", ajaxOptions.dataTypes) !== -1) {
      $(".inputmask, [data-inputmask], [data-inputmask-mask], [data-inputmask-alias]").each(function (ndx, lmnt) {
        if (lmnt.inputmask === undefined) {
          Inputmask().mask(lmnt);
        }
      });
    }
  }).ready(function () {
    $(".inputmask, [data-inputmask], [data-inputmask-mask], [data-inputmask-alias]").each(function (ndx, lmnt) {
      if (lmnt.inputmask === undefined) {
        Inputmask().mask(lmnt);
      }
    });
  });
});